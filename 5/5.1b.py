# Task 5.1b
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
params = ', '.join(london_co.keys())
input_device = input(f'Введите имя устройства ({params}): ')
params = ', '.join(london_co[input_device].keys())
input_parameter = input(f'А теперь введите искомый параметр ({params}): ')
print(london_co[input_device][input_parameter])
#Сам не решил. Подсмотрел. хер ума дам, что значит вот это params = ', '.join   что это за запятая в скобках такая.
