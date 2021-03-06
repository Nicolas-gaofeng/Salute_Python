#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : 03-循环发送数据.py
@author     : zgf
@brief      : 03-循环发送数据
@attention  : life is short,I need python
"""

import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:

        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        # 可以使用套接字收发数据
        # udp_socket.sendto("hahahah", 对方的ip以及port)
        # udp_socket.sendto(b"hahahah------1----", ("192.168.33.53", 8080))
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.33.53", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
