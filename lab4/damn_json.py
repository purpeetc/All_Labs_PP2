import json
import os

# Получаем путь к директории, где находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем путь к файлу sample-data.json
file_path = os.path.join(script_dir, "sample-data.json")

with open(file_path, "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 50)
print("DN".ljust(50) + "Description".ljust(20) + "Speed".ljust(10) + "MTU")
print("-" * 90)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"] if "speed" in attributes else "inherit"
    mtu = attributes["mtu"] if "mtu" in attributes else "9150"

    print(dn.ljust(50) + "".ljust(20) + speed.ljust(10) + mtu)