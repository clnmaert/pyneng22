# Task 4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = nat.replace('Fast', 'Gigabit')
print(nat)

# Task 4.2
mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':', '.')
print(mac)

# Task 4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans_prepare = config[30:]
vlans = vlans_prepare.split(',')
print(vlans)

# или одной строчкой, без введения новой переменной
vlans = (config[(config.find('1')):]).split(',')
print(vlans)

# Task 4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = sorted(list(set(vlans)))
print(result)
# расшифровка изнутри наружу: создаем множество из списка vlans и оно дедуплицирует данные
# затем из этого множества создаем обратно список
# сортируем список по возрастанию

# Task 4.5
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1_list = command1[(command1.find('1')):]
command2_list = command2[(command2.find('1')):]
result = set(command1_list) & set(
    command2_list)  # хрен понял почему в множествах появляется дополнительно запятая как значение...
result.discard(',')
result = sorted(list(result))
print(result)

# Task 4.6
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = "Prefix                {}\nAD/Metric             {}\nNext-Hop              {}\nLast update           {}\nOutbound Interface    {}"
print(template.format(ospf_route[7:19], ospf_route[21:27], ospf_route[33:42], ospf_route[44:49], ospf_route[51:]))

# Task 4.7
mac = "AAAA:BBBB:CCCC"
mac = bin(int(mac.replace(':', ''), 16))
print(mac[2:])


# Task 4.8
ip = "192.168.3.1"
ip = ip.split('.')
print(f"{ip[0]:<10}{ip[1]:<10}{ip[2]:<10}{ip[3]:<10}\n{int(ip[0], 10):08b}  {int(ip[1], 10):08b}  {int(ip[2], 10):08b}  {int(ip[3], 10):08b}")
# ох блин это было больно для мозга

