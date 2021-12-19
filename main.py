from init_tributes import InitTributes

class Game():
    def __init__(self):
        number_of_players     = 4
        tributes_per_district = 2
        
        self.tribute_list = []

        self.tribute_list = InitTributes(number_of_players, tributes_per_district, self.tribute_list)

        Cornucopia()


Game()