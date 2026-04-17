from ipaddress import *
for m in range(33):
    net = ip_network('193.18.135.201/'+str(m),0)
    if net.num_addresses>=105:
        for i in net:
            s=f'{i:b}'
            if s.count('1')==19:
                print(net)
                break