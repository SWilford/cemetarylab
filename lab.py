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

        ages = s[37:42].strip()

        if("d" in ages):
            self.age = float(ages[:(len(ages)-1)])/365
        elif("w" in ages):
            self.age = float(ages[:(len(ages)-1)])/52.1429
        else:
            self.age = float(ages)

        stringMonth = ""
        stringDay = ""

        if self.month < 10:
            stringMonth = "0"+str(self.month)
        else:
            stringMonth = str(self.month)
        if self.day < 10:
            stringDay = "0"+str(self.day)
        else:
            stringDay = str(self.day)

        addedDate = str(self.year)+stringMonth+stringDay
        self.fullDate = float(addedDate)

        self.address = s[42:].strip()
        
        self.streetLetter = "";

        splitAddress = self.address.split(", | |,")
        
        for word in splitAddress:
            if not word[0:1].strip().isnumeric():
                self.streetLetter = word

    def __str__(self):
        return "Name: "+self.firstName+self.lastName+" Buried on: "+str(self.day)+"-"+str(self.month)+"-"+str(self.year)+" Age: "+str(self.age)+" year(s) old. Residence: "+self.address
    

#Main stuff begins here
    
def sortByLastName(peeps):
    for i in range (len(peeps)-1):
        min = i
        for j in range(i+1, len(peeps)):
            if peeps[min].lastName > peeps[j].lastName:
                min = j
        peeps[i], peeps[min] = peeps[min], peeps[i]

def sortByAddress(peeps):
    for i in range (len(peeps)-1):
        min = i
        for j in range(i+1, len(peeps)):
            if peeps[min].streetLetter > peeps[j].streetLetter:
                min = j
        peeps[i], peeps[min] = peeps[min], peeps[i]

def sortByBurialDate(peeps):
    for i in range (len(peeps)-1):
        min = i
        for j in range(i+1, len(peeps)):
            if peeps[min].fullDate > peeps[j].fullDate:
                min = j
        peeps[i], peeps[min] = peeps[min], peeps[i]

def sortByAge(peeps):
    for i in range (len(peeps)-1):
        min = i
        for j in range(i+1, len(peeps)):
            if peeps[min].age > peeps[j].age:
                min = j
        peeps[i], peeps[min] = peeps[min], peeps[i]

text = open("cemetery_orig.txt", "r")
people = []

for line in text:
    i = 0
    if line[0:1] == " " or line[0:1] == "-" or line[0:4] == "NAME":
        i+1
    else:
        person = Person(line)
        people.append(person)

imput = ""
while imput != "0": 
    imput = input("Enter '1' to seach by last name, enter '2' to search by street name, enter '3' to sort and display data, enter '4' to display interesting data, enter '0' to quit: ")
    loc = 0
    iterator = 0
    if imput == "1": #Search by last name
        sortByLastName(people)
        lastNameToSearch = input("Enter last name to seach for: ").lower()
        for i in range (len(people)-1):
            iterator = iterator + 1
            if(people[i].lastName.lower() == lastNameToSearch):
                loc = i
        if iterator == (len(people)-1):
            print("Last name not found.")
        while(people[loc].lastName.lower() == lastNameToSearch):
            print(people[loc])
            loc = loc - 1

    elif imput == "2": #Search by street name
        sortByAddress(people)
        addressToSearch = input("Enter a street name to search for: ").lower()
        for i in range (len(people)-1):
            iterator = iterator + 1
            if(people[i].address.lower() == addressToSearch):
                loc = i
        if iterator == (len(people)-1):
            print("Street not found.")
        while(people[loc].address.lower() == addressToSearch):
            print(people[loc])
            loc = loc - 1

    elif imput == "3": #Sort
        imputSort = input("Enter '1' to sort by name, enter '2' to sort by burial date, enter '3' to sort by age, enter '4' to sort by address: ")
        if imputSort == "1": #Sort by name
            sortByLastName(people)
        elif imputSort == "2": #Sort by burial date
            sortByBurialDate(people)
        elif imputSort == "3": #Sort by age
            sortByAge(people)
        elif imputSort == "4": #sort by address
            sortByAddress(people)
        for person in people:
            print(person)
    
    elif imput == "4": #Show interesting data
        avgAge = 0.0
        oldestAge = 0.0
        allYears = []
        allStreets = []
        for person in people:
            avgAge = avgAge + person.age
            if oldestAge < person.age:
                oldestAge = person.age
            allYears.append(person.year)
            allStreets.append(person.address)
        avgAge = avgAge / len(people)
        highestYear = max(set(allYears), key=allYears.count)
        highestStreet = max(set(allStreets), key=allStreets.count)
        print("Average age at death: "+str(avgAge))
        print("Oldest age at death: "+str(oldestAge))
        print("Year with most amount of deaths: "+str(highestYear)+" with "+str(allYears.count(highestYear))+" deaths")
        print("Street with most deaths: "+str(highestStreet+" with "+str(allStreets.count(highestStreet))+" deaths"))
        
    elif imput != "0": #Checking for invalid inputs
        print("Invalid Input")
print("Program exited.")





        


        
    