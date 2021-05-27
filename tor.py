from config import *
from definieren import *
def tor():
        counter = 0
        while counter < 10:

                host = "ifconfig.me"

                with TorClient() as tor:
                    with tor.create_circuit(3) as circ:
                        with circ.create_stream((host, 80)) as stream:
                            stream.send(b'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host.encode())
                            ret = recv_all(stream).decode()
                            print("Proxy Ip >> " + ret)
                            time.sleep(1)
        counter += 1
        print(counter)
