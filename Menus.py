class Menu:
    def __init__(self):
        self.menu = ["Milanesas","Pizza","Choripan","Ensalada"]

    def getMenu(self):
        return ','.join(self.menu)