class Tribute():
    __id          = 0
    __district    = 0
    __name        = ''
    __health      = 100
    __location    = 0
    __turn_played = 0

    def __init__(self, id, district, name):
        self.__id       = id
        self.__district = district
        self.__name     = name

    def get_name(self):
        return self.__name

def InitTributes(number_of_players, tributes_per_district, tribute_list):
    number_of_districts = int(number_of_players / tributes_per_district)
    print("Welcome to the Hunger Games!")
    print(number_of_districts, "districts, ", tributes_per_district, "tributes per district")

    id = 1
    for district in range(1, number_of_districts + 1):
        for player in range(1, tributes_per_district + 1):
            name = input(f"Disctric {district}, tribute {id}: ")
            tribute = Tribute(id, district, name)
            tribute_list.append(tribute)
            id += 1

    id = 0
    print("Our tributes are:")
    for district in range(1, number_of_districts + 1):
        print("\nDISTRICT ", district)
        for player in range(1, tributes_per_district + 1):
            print(tribute_list[id].get_name())
            id += 1

    print("\nLet the Hunger Games begin!")

    return tribute_list