# 7.1
print("{:=^20}".format("7.1"))

access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}

def ap_config_1(access):
    out = []

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport	nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    for k, v in access.items():
        out.append('interface ' + k)
        for i in access_template:
            if i == access_template[1]:
                out.append(f'{i} {v}')
            else:
                out.append(i)

    return out

print(ap_config_1(access_dict))

print()

# 7.1a
print("{:=^20}".format("7.1a"))

def ap_config_2(access: dict, psecurity: bool = False) -> list:
    out = []

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport	nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    for k, v in access.items():
        out.append('interface ' + k)
        for i in access_template + port_security:
            if i == access_template[1]:
                out.append(f'{i} {v}')
            else:
                out.append(i)

    return out


print(ap_config_2(access_dict))

print()

# 7.1b
print("{:=^20}".format("7.1b"))
def ac_config_gen(access):
    out = dict()

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport	nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    for k, v in access.items():
        out[k] = []
        out[k].append('interface ' + k)
        for i in access_template + port_security:
            if i == access_template[1]:
                out[k].append(f'{i} {v}')
            else:
                out[k].append(i)

    return out

print(ac_config_gen(access_dict))

print()

# 7.2
print("{:=^20}".format("7.2"))
trunk = {'FastEthernet0/1': [10, 20],
         'FastEthernet0/2': [11, 30],
         'FastEthernet0/4': [17]}


def tp_config_gen(trunk):
    out = []

    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for k, v in trunk.items():
        out.append('interface ' + k)
        for i in trunk_template:
            if i == trunk_template[-1]:
                out.append(f'{i} {str(v).replace("[", "").replace("]", "")}')
            else:
                out.append(i)
    return out


print(tp_config_gen(trunk))

print()

# 7.2a
print("{:=^20}".format("7.2a"))
trunk = {'FastEthernet0/1': [10, 20],
         'FastEthernet0/2': [11, 30],
         'FastEthernet0/4': [17]}


def tp_config_gen_2(trunk):
    out = dict()

    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for k, v in trunk.items():
        out[k] = []
        out[k].append('interface ' + k)
        for i in trunk_template:
            if i == trunk_template[-1]:
                out[k].append(f'{i} {str(v).replace("[", "").replace("]", "")}')
            else:
                out[k].append(i)
    return out


print(tp_config_gen_2(trunk))

print()

# 7.3
print("{:=^20}".format("7.3"))
def gvid(file_name):

    access = dict()
    trunk = dict()

    with open(file_name, 'r') as f:
        file = f.read().split('!')
        #print(file)
    for i in file:
        if 'Ethernet' in i:
            #print(i)
            if 'access' in i:
                access['Fast'+i.split()[1]] = i[i.index('vlan')+1:][0]
            elif 'trunk' in i:
                i = i.split()
                trunk['Fast'+i[1]] = i[i.index('vlan')+1:][0]
    
    return access, trunk


print(gvid('config_sw1.txt'))

print()

# 7.3a
print("{:=^20}".format("7.3a"))
def gvid_2(file_name):

    access = dict()
    trunk = dict()

    with open(file_name, 'r') as f:
        file = f.read().split('!')
        #print(file)
    for i in file:
        if 'Ethernet' in i:
            #print(i)
            if 'access' in i:
                access['Fast'+i.split()[1]] = i[i.index('vlan')+1:][0]
            elif 'trunk' in i:
                i = i.split()
                trunk['Fast'+i[1]] = i[i.index('vlan')+1:][0]
            elif 'duplex auto' in i:
                access['Fast'+i.split()[1]] = 1
    
    return access, trunk


print(gvid_2('config_sw1.txt'))

print()

# 7.4
print("{:=^20}".format("7.4"))

ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore = ignore):
    for word in ignore:
        if word in command:
            return True
    return False

def config_to_dict(config):

    text = []
    output = dict()

    with open(config) as f:
        file = f.readlines()
        for i in file:
            if not ignore_command(i) and '!' not in i and i != '\n':
                i = i.replace('\n', '')
                text.append(i)
    
    name = ''
    for i in text:
        if i[0] != ' ':
            name = i
            output[name] = []
        else:
            output[name].append(i)


    return output

print(config_to_dict('config_sw1.txt'))

print()

# 7.4a
print("{:=^20}".format("7.4a"))

ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command_2(command, ignore = ignore):
    for word in ignore:
        if word in command:
            return True
    return False

def config_to_dict_2(config):

    text = []
    output = dict()

    with open(config) as f:
        file = f.readlines()
        for i in file:
            if not ignore_command_2(i) and '!' not in i and i != '\n':
                i = i.replace('\n', '')
                text.append(i)
    
    name = ''
    second_name = ''
    for i in text:
        if i[0] != ' ':
            name = i
            output[name] = {}
        elif i[0] == ' ' and i[1] != ' ':
            second_name = i
            output[name][second_name] = []
        elif i[0] == ' ' and i[1] == ' ':
            output[name][second_name].append(i)


    return output

print(config_to_dict_2('config_sw1.txt'))