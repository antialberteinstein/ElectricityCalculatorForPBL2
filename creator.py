import random as rd
import datetime as dt
import json
import os

# Unit: kWh.
# This program will init the electricity consumption of a dormitory.
# This time I don't have any data, so I will use random number to simulate 
#    the data for my other project.
#     Thanks.


def count_energy_consumption_per_day_of_a_person() -> float:
    return (10.0 + rd.uniform(0.0, 20.0))/30.0

def count_energy_consumption_per_day_of_a_room() -> float:
    energy_consumption_per_day = 0.0
    number_of_people = rd.randint(3, 5)  # Reality: 0-6.
    for i in range(number_of_people):
        energy_consumption_per_day += \
            count_energy_consumption_per_day_of_a_person()
    return energy_consumption_per_day

energy_consumption = dict()
last_month_energy_consumption = dict()
current_month_energy_consumption = dict()

for block in ['A', 'B', 'C', 'D', 'E', 'F']:
    for floor in range(1, 6):
        for room in range(1, 25):
            room_name = block + str(floor * 100 + room)
            energy_consumption[room_name] = 0.0
            last_month_energy_consumption[room_name] = 0.0
            current_month_energy_consumption[room_name] = 0.0

try:
    with open('energy_consumption.json', 'r') as f:
        energy_consumption = json.load(f)
except FileNotFoundError:
    pass
try:
    with open('last_month_energy_consumption.json', 'r') as f:
        last_month_energy_consumption = json.load(f)
except FileNotFoundError:
    pass
try:
    with open('current_month_energy_consumption.json', 'r') as f:
        current_month_energy_consumption = json.load(f)
except FileNotFoundError:
    pass


def loop():
    global energy_consumption

    _today = dt.datetime.now()

    for room in energy_consumption:
        energy_consumption[room] +=\
            count_energy_consumption_per_day_of_a_room()
        print("Energy consumption to", _today, " at room:", room,
            ":", energy_consumption[room])
    with open('energy_consumption.json', 'w') as f:
        json.dump(energy_consumption, f)

    # Create a data for a month.
    if _today.day == 25:
        for room in energy_consumption:
            current_month_energy_consumption[room] = \
                energy_consumption[room] - last_month_energy_consumption[room]
            last_month_energy_consumption[room] = energy_consumption[room]
            print("Current month energy consumption for room:", room, " : ",
                current_month_energy_consumption[room])
        with open('current_month_energy_consumption.json', 'w') as f:
            json.dump(current_month_energy_consumption, f)
        with open('last_month_energy_consumption.json', 'w') as f:
            json.dump(last_month_energy_consumption, f)

if __name__ == '__main__':
    loop()
