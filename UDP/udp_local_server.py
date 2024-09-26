import socket

server_port = 21060
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', server_port))

print ("Server is listening......")

message, address = server_socket.recvfrom(65535)
print ("Client sent: {}".format(message.decode("utf8")))

msg = "Sed molestie lorem non tristique fermentum. Etiam tempus venenatis tellus, a euismod mauris euismod at. Nulla at facilisis massa.\
    Aliquam rhoncus dolor vitae nisl elementum blandit. Duis condimentum, orci vel varius ullamcorper, magna dui dignissim lorem,\
        nec eleifend massa justo id risus. Aliquam erat volutpat. Cras sit amet feugiat dui. Nulla rhoncus elit quis fringilla vehicula.\
            Curabitur commodo tortor sed enim tempus imperdiet. Maecenas leo metus, mattis quis venenatis non, vulputate bibendum elit.\
                Vivamus sagittis at massa eget efficitur. Pellentesque ultricies lectus vel ipsum lobortis, a egestas ipsum faucibus.\
                    Morbi placerat magna vitae dui viverra posuere. Fusce euismod ligula fermentum hendrerit eleifend. Curabitur eu felis ullamcorper, aliquet leo in, egestas urna.\
                        Maecenas fermentum enim vitae augue gravida rutrum."
server_socket.sendto(bytes(msg, encoding='utf8'), address)
server_socket.close()
print("Server closed!")