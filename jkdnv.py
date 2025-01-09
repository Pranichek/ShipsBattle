# # получить свой айпишник
# # import socket
# # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # s.connect(("8.8.8.8", 80))
# # print(s.getsockname()[0])
# # s.close()

# import p


# class Network(object):
#     def __init__(self, ip=''):
#         self.ip = input("Введите IP-адрес (оставьте пустым для сети 192.168.1.1/24):\n")

#     def networkscanner(self):
#         if len(self.ip) == 0:
#             network = '192.168.1.1/24'
#         else:
#             network = self.ip + "/24"

#         print("Сканирование сети...")
#         nm = nmap.PortScanner()
#         nm.scan(hosts=network, arguments='-sn')
#         host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
#         for host, status in host_list:
#             print(f"Хост: {host}, Статус: {status}")


# D = Network()
# D.networkscanner()

