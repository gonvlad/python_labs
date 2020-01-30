import sys

# 6.1
print("{:=^20}".format("6.1"))
file = open("ospf.txt", "r")
for line in file:
    ospf_route = line.split()
    print("Protocol:{:>20}\nPrefix:{:>30}".format("OSPF", ospf_route[1]))
    print("AD/Metric:{:>21}\nNext-Hop{:>26}".format(ospf_route[2][1:-1],
                                                    ospf_route[4][:-1]))
    print("Last update:{:>18}\nOutbound Interface:{:>21}\n".format(
                        ospf_route[5][:-1], ospf_route[6]), end = "\n\n")
file.close()

# 6.2 - 6.2a
print("{:=^20}".format("6.2"))
ignore =  ['duplex', 'alias', 'Current configuration']
file = open(sys.argv[1], "r")
for line in file:
    if line.startswith("!") or line.startswith("\n"):
        continue
    else:
        for i in ignore:
            if i in line:
                break
        else:
            print(line.rstrip())
file.close()
print()

# 6.2b
print("{:=^20}".format("6.2b"))
ignore =  ['duplex', 'alias', 'Current configuration']
file_I = open(sys.argv[1], "r")
file_O = open(sys.argv[2], "w")
for line in file_I:
    for i in ignore:
        if i in line:
            break
    else:
        file_O.write(line)
else:
    print("Filtered!")

file_I.close()
file_O.close()
print()

# 6.3
print("{:=^20}".format("6.3"))
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
file_I = open("CAM_table.txt", "r")

for line in file_I:
    if len(line) != 1:
        if line[1] in digits:
            row_data = line.rstrip().split()
            del row_data[2]
            print("\t".join(row_data))

file_I.close()
print()

# 6.3a
print("{:=^20}".format("6.3a"))
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
table_data = []
file_I = open("CAM_table.txt", "r")

for line in file_I:
    if len(line) != 1:
        if line[1] in digits:
            table_data.append(line.rstrip().split())
file_I.close()

table_data.sort()
for row in table_data:
    del row[2]
    print("\t".join(row))
print()

# 6.3b
print("{:=^20}".format("6.3b"))
vlan = input("Enter vlan number: ")
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
file_I = open("CAM_table.txt", "r")

for line in file_I:
    if len(line) != 1:
        if line[1] in digits:
            row_data = line.rstrip().split()
            if row_data[0] == vlan:
                del row_data[2]
                print("\t".join(row_data))

file_I.close()
