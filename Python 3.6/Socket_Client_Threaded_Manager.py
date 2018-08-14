def manage_client(new_client, notification_event, message_queue, stop_flag):
    connected = True
    stream = ''
    while connected and not stop_flag:
        r, w, e = select([new_client, ], [], [], 0.01)
        for c in r:
            data = c.recv(1024)
            if len(data) == 0:
                connected = False
                try:
                    c.shutdown(socket.SHUT_RDWR)
                finally:
                    pass
                try:
                    c.close()
                finally:
                    pass
                continue
            stream += data.decode('utf-8')
            while '\n' in stream and not stop_flag:
                message, stream = stream.split('\n')
                put_in_queue = False
                while not put_in_queue and not stop_flag:
                    try:
                        message_queue.put(message, timeout=0.01)
                    except Full:
                        pass
                    except Exception as e:
                        logging.error(e)
                    else:
                        put_in_queue = True
                notification_event.set()
