# age = input("Podaj ile masz lat: ")
# age_month = int(age) * 12
# print("masz", age_month, "miesięcy")

# b_price_apple = float(input("Podaj cene jablek w b: "))
# l_price_apple = float(input("Podaj cene jablek w l: "))
# z_price_apple = float(input("Podaj cene jablek w z: "))
#
# lowest_price = min(b_price_apple, l_price_apple, z_price_apple)
# print("najnizsza cena to: ", lowest_price)

# amount = 1200
# percentage = 1.04
# lokata = float(amount / percentage)
# print(f"Twoja kwota to {lokata:.2f}")

# name = input("Podaj imie: ")
# name_len = len(name)
# print(name_len)

# place = input("Podaj gdzie mieszkasz: ")
# name_len = place.title()
# print(f"Jak milo ze mieszkasz w: {name_len}")

# ford = "ab100100"
# audi = "EEE 123123"
#
# ford = ford.upper()
# audi = audi.replace(' ', '')
# print(ford, audi)

# favourite_sports = ["volleyball", "football", "fitness"]
# most_favorite = favourite_sports[2]
# less_favourite = favourite_sports[1]
# print(f"The most I like is: {most_favorite}, the less I like is {less_favourite}")
# favourite_sports[1] = "basketball"
# print(favourite_sports)
#
# favorite_dishes = input("Please enter 3 favourite dishes: ")
# fav_dish_list = favorite_dishes.split(',')
# print(fav_dish_list)

# phone_num = input("Please give phone num: ")
# phone_num_public = phone_num[:6]
# print(phone_num_public)
# phone_num_len = len(phone_num) - 6
# phone_num_hid = "-" * phone_num_len
# print(phone_num_hid)
# anonymous_numer = f"{phone_num_public}{phone_num_hid}"
# print(anonymous_numer)



# school_dict = {"math" : 4,
#                "pol" : 5,
#                "biol" : 3}
# print(school_dict)

# my_family = {"Name":"Joanna", "Surename":"Piekarska", "Age":29, "Parents":[{"Name":"Adam","Surename":"Piekarski", "Age":63}, {"Name":"Ewa", "Surename":"Lipska", "Age":54}]}
# print(my_family)
#
# jedz = float(input("Ile wydajesz na jedz: "))
# rozr = float(input("Ile wydajesz na rozr: "))
# opl = float(input("Ile wydajesz na opl: "))
# inne = float(input("Ile wydajesz na inne: "))
#
# all_costs = jedz+rozr+opl+inne
#
# wyd_dict = {"jedz": jedz, "rozr": rozr, "opl":opl, "inne": inne}
# jedz_proc = wyd_dict["jedz"]/all_costs * 100
# rozr_proc = wyd_dict["rozr"]/all_costs * 100
# opl_proc = wyd_dict["opl"]/all_costs * 100
# inne_proc = wyd_dict["inne"]/all_costs * 100
#
# wyd_dict = {"jedz": jedz_proc, "rozr": rozr_proc, "opl":opl_proc, "inne": inne_proc}
#
# selected_cath = input("Podaj kategorie: ")
# print(f"Na {selected_cath} wydajesz {wyd_dict[selected_cath]}")
#
# biggest_cost = max(jedz_proc, rozr_proc,opl_proc,inne_proc)
#
# if biggest_cost == jedz_proc:
#     print(f"You have the biggest cost in {jedz_proc}")
# if biggest_cost == rozr_proc:
#     print(f"You have the biggest cost in {rozr_proc}")
# if biggest_cost == opl_proc:
#     print(f"You have the biggest cost in {opl_proc}")
# if biggest_cost == inne_proc:
#     print(f"You have the biggest cost in {inne_proc}")


# math_note = int(input("Please enter math note: "))
# pol_note = int(input("Please enter pol note: "))
# biol_note = int(input("Please enter biol note: "))
# hist_note = int(input("Please enter hist note: "))
#
# medium_note = float((math_note+pol_note+biol_note+hist_note)/4)
# if (math_note == 1 or pol_note == 1 or biol_note == 1 or hist_note == 1) and medium_note > 3.5:
#     print(f"You go to next class")
# elif math_note != 1 and pol_note != 1 and biol_note != 1 and hist_note != 1:
#     print(f"You go to next class")
# else:
#     print("You cant go to next class")
#
# name = input("Podaj imie: ")
# last_char = name[-1]
# if last_char == 'a' and name != 'Kuba':
#     print(f"{name} to kobieta")
# elif last_char != 'a' or name == 'Kuba':
#     print(f"{name} to mężczyzna")

# kwotę kredytu
# oprocentowanie kredytu
# wartość wkładu własnego
# czas kredytowania w latach
# przychód miesięczny
# sumę miesięcznych wydatków

# kw_kredyt = float(input("Podaj kwote kredytu: "))
# oproc_kredytu = float(input("Podaj oproc kredytu: "))
# wart_wkl_wlas = float(input("Podaj wartosc wkładu wlasnego: "))
# czas_kred_w_latach = float(input("Podaj czas kred w latach: "))
# przych_mies = float(input("Podaj przych mies: "))
# sum_mies_wyd = float(input("Podaj sume miesiecznych wyd: "))

# (kwota kredytu * oprocentowanie / 100) / 12 + kwota kredytu / (liczba lat * 12)

# rata_kred = float((kw_kredyt * oproc_kredytu / 100)/12 + kw_kredyt/(czas_kred_w_latach * 12))
#
# dost_srodki = przych_mies - sum_mies_wyd
# wart_nieruchomosci = float(wart_wkl_wlas + kw_kredyt)
#
# if wart_wkl_wlas > 1.2 * wart_nieruchomosci and dost_srodki == rata_kred + 1000:
#     print(f"You ve got credit with rate equal: {rata_kred}")
# elif wart_wkl_wlas >= 1.1 * wart_nieruchomosci and wart_wkl_wlas <= 1.2 * wart_nieruchomosci  and dost_srodki == rata_kred + 2000:
#     print(f"You ve got credit with rate equal: {rata_kred}")
# elif wart_wkl_wlas < 1.1 * wart_nieruchomosci:
#     print(f"You ve NOT got credit")

# lista_zakupów = input("Podaj liste: ")
# lista_zakupów = lista_zakupów.split(",")
# # gender = input("Podaj plec: ")
# # wynik= input("Podaj wynik: ")
#
# if "seler" in lista_zakupów or "bulki" in lista_zakupów:
#     print("List contains seler")


# num_tel = input("Podaj nu, tel: ")
# if "0" in num_tel:
#     print("Num tel conrtains one zero")

# value = 1
# if value is not None:
#     print("Value is nine")
# if value is True:
#     print("Value is true")
# if value == True:
#     print("Value is equal true")

# num = int(input("Podaj liczbe parzysta: "))
# count = 1
# num_odd = num % 2
# while count < 10:
#     num = int(input("Podaj liczbe parzysta: "))
#     count += 1
#     num_odd = num % 2
#     if num_odd == 0:
#         print(f"Liczba parzsta to {num}")
#         exit()
# print(f"Przekroczyłes 10 prób")

# index = 0
# tel = input("Podaj tel: ")
# tel = tel.replace("-", "")
# tel_len = len(tel)
# while index < tel_len:
#     cotrzeci = index % 3
#     if cotrzeci == 0:
#         tel_part = tel[:3]

# note = 0
# notes = []
# while note != 'X':
#     note = input("Please enter subject note or finish by pasting X: ")
#     if note != 'X':
#         note = int(note)
#         notes.append(note)
# note_sum = 0
# for item in notes:
#  #+
#  # item = int(item)
#     note_sum = note_sum + item
# note_avg = note_sum/len(notes)
# print(f"Avarage note is {note_avg}")

# index = 0
# tel = input("Podaj tel: ")
# tel = tel.replace("-", "")
# tel_len = len(tel)
# for index, character in enumerate(tel):
# #while index < tel_len:
#     cotrzeci = index % 3
#     if cotrzeci == 0:
#         tel_part = tel[:3]
# print(f"{tel_part}")


# tel = input("Podaj tel:")
# tel = tel.replace("-", "")
# tel_len = len(tel)
# for el in range(1, 10):
#     el_amount = tel.count(str(el))
#     print(f"{el} exists {el_amount} times")


# credit_total = float(input("Please input total amount credit:"))
# percent_credit = float(input("Paste percentage of credit:"))
# duration_time = int(input("Enter duration time: "))
# cost_start = float(input("Enter cost start: "))
# percentage_for_bank = duration_time*percent_credit*credit_total
# amount_for_bank = credit_total+cost_start+percentage_for_bank
#
# duration_time_month = 12*duration_time
# fund_per_month = credit_total / duration_time * 12
#
#
# for el in range(1, duration_time_month+1):
#     rest_fund = credit_total - ((el - 1) * fund_per_month)
#     rate = (rest_fund*percent_credit/100)/12 +fund_per_month
#     print(f"Rata w miesiącu {el} wynosi {rate}")
#
# print(f"Koszt całkowity to {amount_for_bank}")

# note_table = []
# math_note = int(input("Please enter math note: "))
# pol_note = int(input("Please enter pol note: "))
# biol_note = int(input("Please enter biol note: "))
# hist_note = int(input("Please enter hist note: "))
#
# note_table = [math_note, pol_note,biol_note,hist_note]
# for note in note_table:
#     if note < 2:
#         print("You don't pass to next class")
#         break
# else:
#     print("Congrat, you pass to next class")
# wydatki= []
# expedit = input("Podaj wydatki:")
# wydatki.append(expedit)
# while True:
#     expedit = input("Podaj wydatki:")
#     for exped in wydatki:
#         if exped != expedit:
#             wydatki.append(expedit)
#         else:
#             print("Ten wydatek juz istnieje")
#             break
#     # else:
#     #     wydatki.append(expedit)
# print(f"{wydatki}")

#
# liczby = [1,2,13,14,18,20,23,44,56,87,98,78]
# for value in liczby:
#     if value % 2 != 0:
#         print(f"This {value} is not odd")
#         continue

# a = int(input("Podaj długosc boku a:"))
# b = int(input("Podaj długosc boku b:"))
# def rectangle_field(a,b):
#     field = a*b
#     return field
# print(f"Pole figury to {rectangle_field(a,b)}")


def speed_calc(dist,time):
    speed = dist/time
    print(f"Speed was {speed:.2f}")
    return speed

def avg_sprint_bike_car(type):
    if type == 'sprint':
        dist = int(input("Podaj przebyta odległosc pieszo:"))
        time = int(input("Podaj czas podrózy:"))
        speed = speed_calc(dist,time)
    if type == 'bike':
        dist = int(input("Podaj przebyta odległosc rowerem:"))
        time = int(input("Podaj czas podrózy:"))
        speed= speed_calc(dist,time)
    if type == 'car':
        dist = int(input("Podaj przebyta odległosc samochodem:"))
        time = int(input("Podaj czas podrózy:"))
        speed= speed_calc(dist,time)
    return speed

# type = input("Podaj typ podrózy: sprint, bike, car")
# #avg_sprint_bike_car(type)
# print(f"ta podróz była z predkoscią: {avg_sprint_bike_car(type)}")


# Zmodyfikuj rozwiązanie zadania trzeciego z lekcji dotyczącej pętli for (obliczanie wydatków domowych).
# Skorzystaj z instrukcji break aby wyeliminować powtórzone wywołania funkcji input.

#
# print("Kalkulator budżetu miesięcznego")
# expenditures = {}
#
# def gather_expenditures(cathegory_name):
#     while True:
#         category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
#         if category_name == "X":
#             break
#         expenditures[category_name] = []
#
# def gather_expenditures(cathegory_name):
#
#     expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
#     if expenditure == "X":
#         break
#
#     expenditure_value = float(expenditure)
#     expenditures[category_name].append(expenditure_value)
#     return expenditures
#
#
# total_expenditures = 0
# for category_expenditures in expenditures.values():
#     total_expenditures += sum(category_expenditures)
#
#
# expenditures_percentage = {}
# for category_name, category_expenditures in expenditures.items():
#     total_category_expenditures = sum(category_expenditures)
#     expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
#
# most_important_category = None
# most_important_category_percentage = 0
# for category, percentage in expenditures_percentage.items():
#     if percentage > most_important_category_percentage:
#         most_important_category_percentage = percentage
#         most_important_category = category
#
# if most_important_category is not None:
#     print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")
#
# for category, percentage in expenditures_percentage.items():
#     print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")

#Kalkulator

# def load_values(category_name):
#     values_for_category = []
#     while True:
#         value_for_cat = input(f"Podaj wartoś wydatków dla kategori {category_name}: lub X jesli chcesz zakonczyc: ")
#         if value_for_cat == "X":
#             return values_for_category
#         values_for_category.append(float(value_for_cat))
#
# def load_val_to_cat_dict():
#     cat_with_values = {}
#     while True:
#         category_name = input("Podaj nazwe kategorii wydatków lub zakończ z X: ")
#         if category_name == "X":
#             return cat_with_values
#         cat_with_values[category_name] = load_values(category_name)
#
# def total_exp_per_cat(cat_with_values):
#     total_exp = 0
#     for cath in cat_with_values.values():
#         total_exp += sum(cath)
#     return total_exp
#
# def exp_percentage(cat_with_values, total_expend):
#     expenditures_percentage_by_cat = {}
#     for category_name, category_expenditures in cat_with_values.items():
#         total_category_expenditures = sum(category_expenditures)
#         expenditures_percentage_by_cat[category_name] = total_category_expenditures * 100 / total_expend
#     return expenditures_percentage_by_cat
#
# def find_most_imp_cat(expenditures_percentage_by_cat):
#     most_important_category = None
#     most_important_category_percentage = 0
#     for category, percentage in expenditures_percentage_by_cat.items():
#         if percentage > most_important_category_percentage:
#             most_important_category_percentage = percentage
#             most_important_category = category
#     return most_important_category, most_important_category_percentage
# def print_the_most_imp_cat(category_name, percentage):
#     print(f"Najwiecej wydajesz na kaktegorie {category_name} - o wyskosci: {percentage:.2f}%")
#
# def print_cat_info(category_name, percentage):
#     print(f"Na kaktegorie {category_name} wydajesz {percentage:.2f}% wszystkich wydatków")
#
# expe_by_cat = load_val_to_cat_dict()
# total_expenditures = total_exp_per_cat(expe_by_cat)
# expenditures_percentage = exp_percentage(expe_by_cat, total_expenditures)
# most_important_category, most_important_category_percentage = find_most_imp_cat(expenditures_percentage)
#
# if most_important_category is not None:
#     print_the_most_imp_cat(most_important_category, most_important_category_percentage)
#
# for category, percentage in expenditures_percentage.items():
#     print_cat_info(category, percentage)

# def speed_calc(dist,time):
#     speed = dist/time
#     print(f"Speed was {speed:.2f}")
#     return speed
#
# speed_calc(dist=30, time=2)


# number_to_convert = float(input("Podaj liczbe do konwersji: "))
#
# def convert_to_scope(number_to_convert, scope=0.1):
#     converted_value = number_to_convert * float(scope)
#     number_with_scope = [number_to_convert - converted_value, number_to_convert + converted_value]
#     return number_with_scope

# print(f"Dla liczby {number_to_convert} zakresem jest {convert_to_scope(number_to_convert)}")

new_persons = []
for i in range(1,10):
    person = input("Podaj imie uczestnika lub zakoncz wpisując X: ")
    if person == "X":
        break
    new_persons.append(person)
def participants(new_persons, previous_participants=None):
    print(f"{new_persons}")
    if previous_participants == None:
        previous_participants = []
    previous_participants.append(new_persons)
    return previous_participants

print(f"Po dołączeniu nowych osób mamy listę {participants(new_persons)}")


