import math
import random

def list_float_create():
    list_data_float = []
    for _ in range(6):
        list_data_float.append(random.uniform(-20, 20))
    print(list_data_float)
    list_data_int = []
    for _ in range(3):
        list_data_int.append(random.randint(1,10))
    print(list_data_int)
    print(round(list_data_float[0]))
    print(math.ceil(list_data_float[1]))
    print(math.floor(list_data_float[2]))
    print(pow(list_data_float[3], list_data_int[0]))
    print(math.pow(list_data_float[4], list_data_int[1]))
    print(list_data_float[5] ** list_data_int[2])


def gather_data():
    name = input("Podaj imie i nazwisko: ")
    name.lstrip()
    name.rstrip()
    data = name.split()
    sentence = f"Nazywam się {data[0]} a nazwisko to {data[1]}"
    print(sentence)


def colours():
    colors_fav = input("Podaj ulubione kolory: ")
    blue_exist = colors_fav.find("blue")
    if blue_exist == -1:
        print(f"blue not exist")
    else:
        print(f"blue exists")



def gather_data_format():
    name = input("Podaj imie i nazwisko: ")
    name.lstrip()
    name.rstrip()
    data = name.split()
    sentence = "Nazywam się {} a nazwisko to {}".format(data[0], data[1])
    print(sentence)


def compreh():
    divided_3 = [number for number in range(30) if number % 3 == 0]
    print(divided_3)
    divided_5 = [number for number in range(30) if number % 5 == 0]
    print(divided_5)
    divided_5.extend(divided_3)
    print(divided_5)

def sports_fav():
    print("Podaj ulubione sporty: ")
    lista_sport=[]
    while True:
        sport = input("Podaj ulubiony lub X: ")
        if sport == "X":
            break
        lista_sport.append(sport)
    print(lista_sport)
    print(lista_sport[1::2])


if __name__ == '__main__':
    sports_fav()