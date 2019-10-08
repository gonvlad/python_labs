# 3.6
print("{:=^20}".format("3.6"))
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'.split()
print("Protocol:{:>20}\nPrefix:{:>30}".format("OSPF", ospf_route[1]))
print("AD/Metric:{:>21}\nNext-Hop{:>26}".format(ospf_route[2][1:-1], ospf_route[4][:-1]))
print("Last update:{:>18}\nOutbound Interface:{:>21}".format(ospf_route[5][:-1], ospf_route[6]), end = "\n\n")


# 3.7
print("{:=^20}".format("3.7"))
MAC = 'AAAA:BBBB:CCCC'.split(":")
print(bin(int(MAC[0], 16))[2:] + bin(int(MAC[1], 16))[2:] + bin(int(MAC[2], 16))[2:], end = "\n\n")

# 3.8
print("{:=^20}".format("3.8"))
IP = [int(i) for i in '192.168.3.1'.split(".")]
print("{:<10} {:<10} {:<10} {:<10}".format(IP[0], IP[1], IP[2], IP[3]))
print(format(IP[0], '010b'), format(IP[1], '010b'), format(IP[2], '010b'), format(IP[3], '010b'), end = "\n\n")

# 3.9
print("{:=^20}".format("3.9"))
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
num_list.reverse()
word_list.reverse()
print(len(num_list) - num_list.index(10) - 1)
print(len(word_list) - word_list.index('ruby') - 1)
