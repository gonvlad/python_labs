import re

def parse(filename):
    with open(filename) as f:
        data = f.read()

    regex = r'(\S+[\d/]+) +([\d.]+|unassigned) +YES (?:manual|unset  administratively) +(up|down) +(up|down)'
    output = re.findall(regex, data)

    return output


print(parse('sh_ip_int_br_2.txt'))
data = parse('sh_ip_int_br_2.txt')

def return_match(filename, reg_e):
    with open(filename) as f:
        file = f.read()
        print(re.findall(reg_e, file))


return_match('sh_ip_int_br.txt', r'\d+\.\d+\.\d+\.\d+')

def parse_cfg(filename):
    output = []

    reg_e = r'\d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+'

    with open(filename) as f:
        file = f.read()
    data = re.findall(reg_e, file)

    for i in data:
        output.append(tuple(i.split()))

    return output


print(parse_cfg('config_r1.txt'))


def parse_cfg_1(filename):
    output = []

    reg_e = r'\d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+'

    with open(filename) as f:
        file = f.read()
    data = re.findall(reg_e, file)

    for i in data:
        output.append(tuple(i.split()))

    return output


print(parse_cfg_1('config_r1.txt'))

def parse_cfg_2(filename):
    output = {}

    with open(filename) as f:
        file = f.read()
    data = re.findall(r'interface Ethernet[\s\S]*?!', file)

    for string in data:
        name = re.search(r'interface (Ethernet\d/\d)', string)[1]

        string = re.search(r'ip address (?P<ip>[\d.]{7,}) (?P<mac>[\d.]{7,})', string)

        if string:
            ip = string['ip']
            mac = string['mac']
            output[name] = (ip, mac)
        else:
            output[name] = None

    return output


print(parse_cfg_2('config_r1.txt'))


def parse_cfg_3(filename):
    output = {}

    with open(filename) as f:
        file = f.read()
    data = re.findall(r'interface Ethernet[\s\S]*?!', file)

    for string in data:
        name = re.search(r'interface (Ethernet\d/\d)', string)[1]

        string = re.search(r'ip address (?P<ip>[\d.]{7,}) (?P<mac>[\d.]{7,})', string)

        if string:
            ip = string['ip']
            mac = string['mac']
            output[name] = (ip, mac)
        else:
            output[name] = None

    return output


print(parse_cfg_3('config_r1.txt'))

def parse_cfg_3b(filename):
    output = {}

    with open(filename) as f:
        file = f.read()
    data = re.findall(r'interface Ethernet[\s\S]*?!', file)

    for string in data:
        name = re.search(r'interface (Ethernet\d/\d)', string)[1]
        string = re.findall(r'ip address ([\d.]{7,}) ([\d.]{7,})', string)
        output[name] = string if string else None

    return output


print(parse_cfg('config_r2.txt'))


def parse_sh_ip_int_br(filename):
    with open(filename) as f:
        data = f.read()

    regex = r'(\S+[\d/]+) +([\d.]+|unassigned) +YES (?:manual|unset  administratively) +(up|down) +(up|down)'
    output = re.findall(regex, data)

    return output


print(parse_sh_ip_int_br('sh_ip_int_br_2.txt'))
data = parse_sh_ip_int_br('sh_ip_int_br_2.txt')

fields = ['Intrface', 'IP-Address', 'Status', 'Protocol']


def convert_to_dict(fields: list, data: list):

    output = []

    for i in data:
        output.append(dict(zip(fields, i)))

    return output


print(convert_to_dict(fields, data))