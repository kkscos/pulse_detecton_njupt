import socket
def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个本地信息
    localaddr = ("172.20.10.5", 8080)
    udp_socket.bind(localaddr)
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        # 打印接收到的数据
        print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))

    # 关闭套接字
    udp_socket.close()



if __name__ == "__main__":
    main()
