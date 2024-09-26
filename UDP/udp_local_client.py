import time
import socket

server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client connected with server")


msg = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sapien elit, efficitur in ornare et, iaculis in massa.\
        Ut sed lectus pharetra, molestie arcu sit amet, faucibus ex. Proin fermentum tincidunt turpis, sit amet fringilla justo faucibus non.\
        Nam finibus augue libero, sagittis sodales ligula feugiat vel. Quisque eget sem tristique massa dignissim molestie rhoncus sit amet odio.\
        Pellentesque semper vulputate velit, ac iaculis nisi. Sed non dictum odio, ut rutrum massa. Nulla at enim ut augue dapibus scelerisque.\
        Vestibulum fermentum urna at lorem posuere sagittis. Donec scelerisque nulla risus, id volutpat augue dapibus vitae.'

start = time.time()
client_socket.sendto(bytes(msg, encoding ="utf8"), ("127.0.0.1", server_port))
server_response, address = client_socket.recvfrom(65535)
print ("Server replied: {}".format(server_response.decode("utf8")))
end = time.time()
print(f"Time elapsed from sending to receiving the message: {end - start}")
print("Client closing...")
time.sleep(3)
client_socket.close()
print("Client closed!")