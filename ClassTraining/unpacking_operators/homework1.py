import random
def concate_all(*args):
    string_result = ""
    for item in args:
        string_result += str(item)
        string_result += "_"
    return string_result[:-1]

def print_all():
    for_print = concate_all("ma", "ta", 7, "la", "wa")
    print(for_print)

def create_descr(**kwargs):
    call_str = "def create_descr("
    for item, descr in kwargs.items():
        call_str += f"{item} = {descr},"
    call_str += ")"
    print(call_str)

# def run_create_descr():
#
#     create_descr(**kwargs)

def run_create_own_descr():
    kwargs1 = {"first_name" : "Ania",
              "Age" : "15",
              "LastName" : "Kowalska",
              "Live in" : "Warsaw"
              }
    kwargs2 = {"first_name1" : "Jan",
              "Age1" : "17",
              "LastName1" : "Kowalskowy",
              "Live in1" : "Grójec"
              }

    all_data = {**kwargs1, **kwargs2}
    create_descr(**all_data)

def list_genration():
    list_name = []
    list_length = random.randint(4,9)
    for item in range (1, list_length):
        list_name.append(random.randint(1,100))
    return list_name

def run_concate_list():
    list1 = list_genration()
    print(list1)
    list2 = list_genration()
    print(list2)
    list3 = [*list1, *list2]
    print(list3)


if __name__ == '__main__':
    run_concate_list()
