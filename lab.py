import calendar

class Person:
    def __init__(self, s):
        fullName = s[:25].strip().split()
        self.firstName = "";
        self.lastName = "";
        for name in fullName:
            if fullName.index(name) == (len(fullName)-1):
                self.lastName = name
            else:
                self.firstName = self.firstName+name+" "
        self.firstName.strip()
        self.lastName.strip()

        burialDate = s[25:37].strip().split()
        self.day = burialDate[0]
        self.month = burialDate[1]
        self.year = int(burialDate[2])
        if self.day == "xx":
            self.day = int(0)
        else:
            self.day = int(self.day)
        self.month = int(list(calendar.month_abbr).index(self.month))

        self.age = 0.0

        self.ages = s[37:42].strip().split()

        if("d" in self.ages[0]):
            self.age = float(self.ages[0])/365
        elif("w" in self.ages[0]):
            self.age = float(self.ages[0])/52.1429
        else:
            self.age = float(self.ages[0])

        self.address = s[42].strip().split()

        ##continue w/ address stuff
        







g = Person("Mary SARTINE             xx Dec 1815 64   Taylor's Court, Lambeth Hill")
print(g.firstName+" "+g.lastName)
print(" ")
print(g.day)
print(g.month)
print(g.year)
