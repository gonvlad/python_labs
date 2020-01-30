print("{:=^21}".format("5.1"))
while(True):
    IP = [int(i) for i in input("Enter IP:").split(".")]
    if 0 <= IP[0] <= 255 and 0 <= IP[1] <= 255 and 0 <= IP[2] <= 255 and 0 <= IP[3] <= 255:
        break
    else:
        print("Incorrect IPv4 address")

print("Class => ", end = "")
if IP[0] == IP[1] == IP[2] == IP[3] == 0:
    print("unassigned")
elif IP[0] >= 0 and IP[0] <= 223:
    print("unicast")
elif IP[0] >= 224 and IP[0] <= 239:
    print("multicast")
elif IP[0] == IP[1] == IP[2] == IP[3] == 255:
    print("local broadcast")
else:
    print("unused")

print("\n{:=^21}".format("5.2"))
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = [i.replace(":", ".") for i in mac]
print(mac_cisco)

print("\n{:=^21}".format("5.3"))
access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']
fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

print()
for port, action in fast_int['trunk'].items():
    print('Port: ' + port)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if action[0] == 'add':
                print(' {} '.format(command), end="")
                for i in action:
                    print(i, end=" ")
                print()
            elif action[0] == 'only':
                print(' {} '.format(command), end="")
                for i in action[1:]:
                    print(i, end=" ")
                print()
            else:
                print(' {} remove '.format(command), end="")
                for i in action[1:]:
                    print(i, end=" ")
                print()
        else:
            print(' {}'.format(command))
