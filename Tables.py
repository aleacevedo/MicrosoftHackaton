class Table:
    def __init__(self):
        self.apoinments = {}
        self.times = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    
    def checkDateAviable(self, date, time):
        try:
            self.apoinments.get(date)
            if(self.apoinments[date].index(time[0]) and self.apoinments[date].index(time[1])):
                for i in range(date[0], date[1]):
                    self.apoinments[date].remove(i)
                return True
            else:
                return False

        except:
            self.apoinments[date] = self.times
            for i in range (date[0],date[1]):
                self.apoinments[date].remove(i)

            return True

    def reserveTable(self, date,time):

        self.apoinments[date] = self.times
        for i in range(date[0], date[1]):
            self.apoinments[date].remove(i)
        return True

