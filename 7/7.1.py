#Задание 7.1
'''
Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
output = '\n{:25} {}' * 5
with open('ospf.txt') as f:
    for line in f:
        line = line.split()
        prefix = line[1]
        metric = line[2].strip('[]')
        nexthop = line[4].strip(',')
        lastupdate = line[5].strip(',')
        outboundif = line[6]
        #print('Prefix                {:23}\nAD/Metric             {:23}\nNext-Hop              {:23}\nLast update           {:23}\nOutbound interface    {:23}\n'.format(prefix, metric, nexthop, lastupdate, outboundif))
        print(output.format("Prefix", prefix, "AD/Metric", metric, "Next-Hop", nexthop, "Last update", lastupdate,
                            "Outbound interface", outboundif))
