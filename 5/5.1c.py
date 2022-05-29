london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device = input("Введите имя устройства: ")
params = ", ".join(london_co[device].keys())
parameter = input(f"Введите имя параметра ({params}): ")

print(london_co[device].get(parameter, "Такого параметра нет"))
# начисто не понимаю, как это работает. Скопировал ответ и всё равно не понимаю последнюю строку
# не понимаю что такое  get

