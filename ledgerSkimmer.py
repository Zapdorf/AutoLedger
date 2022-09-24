import pandas as pd

df = pd.read_excel (r'C:\Users\SHODAN\Downloads\bill finder\The Legendary Ledger of The Apartment™.xlsx')
#print (df)

charges = pd.DataFrame(df, columns= ['Charge Name'])
#df.at[0, 'Charge Name']

# ===================================

class Shmuck:
    def __init__(self, name):
        self.name = name
        self.owesAndrew = 0
        self.owesWalker = 0
        self.owesWill = 0
        self.gains = 0

    def displayDamage(self):
        print("\n"+self.name)
        if self.name != "Andrew": print("-> Owes Andrew: $"+str(format(self.owesAndrew, '.2f')))
        if self.name != "Walker": print("-> Owes Walker: $"+str(format(self.owesWalker, '.2f')))
        if self.name != "Will": print("-> Owes Will: $"+str(format(self.owesWill, '.2f')))

    def takeDamage(self, payee, state, amount):
        if state != "x":
            match payee:
                case "Andrew":
                    self.owesAndrew += amount
                case "Walker":
                    self.owesWalker += amount
                case "Will":
                    self.owesWill += amount

    def getTotalOwed(self):
        return self.owesAndrew + self.owesWalker + self.owesWill

# ===================================

Andrew = Shmuck("Andrew")
Walker = Shmuck("Walker")
Will = Shmuck("Will")

for c in range(len(df)):
    amount = df.at[c, 'Amount']

    divideXWays = 0
    payStates = [df.at[c, 'Andrew'], df.at[c, 'Walker'], df.at[c, 'William']]
    for s in payStates:
        if s != "x": divideXWays += 1 
    amountPerPerson = amount / divideXWays
    
    #settle the finances
    if payStates[0] == "p": # me
        Walker.takeDamage("Andrew", payStates[1], amountPerPerson)
        Will.takeDamage("Andrew", payStates[2], amountPerPerson)
        
    elif payStates[1] == "p": # Walker
        Andrew.takeDamage("Walker", payStates[0], amountPerPerson)
        Will.takeDamage("Walker", payStates[2], amountPerPerson)
        
    elif payStates[2] == "p": # Will
        Andrew.takeDamage("Will", payStates[0], amountPerPerson)
        Walker.takeDamage("Will", payStates[1], amountPerPerson)
    

# cancel stuff out


Andrew.owesWalker -= Walker.owesAndrew
Walker.owesAndrew = 0
if Andrew.owesWalker < 0:
    Walker.owesAndrew = -1 * Andrew.owesWalker
    Andrew.owesWalker = 0
    
Andrew.owesWill -= Will.owesAndrew
Will.owesAndrew = 0
if Andrew.owesWill < 0:
    Will.owesAndrew = -1 * Andrew.owesWill
    Andrew.owesWill = 0

Walker.owesWill -= Will.owesWalker
Will.owesWalker = 0
if Walker.owesWill < 0:
    Will.owesWalker = -1 * Walker.owesWill
    Walker.owesWill = 0


# Display who owes what
Andrew.displayDamage()
Walker.displayDamage()
Will.displayDamage()

# Calculate Stonkey Kong
shmucks = [Andrew, Walker, Will]
shmucks[0].gains = shmucks[1].owesAndrew + shmucks[2].owesAndrew
shmucks[1].gains = shmucks[0].owesWalker + shmucks[2].owesWalker
shmucks[2].gains = shmucks[0].owesWill + shmucks[1].owesWill

mostGains = 0
nameOfWinner = ""
for s in shmucks:
    if s.gains > mostGains:
        mostGains = s.gains
        nameOfWinner = s.name
print("\n" + nameOfWinner + " will obtain $" + format(mostGains, '.2f') + ", earning him the title of Stonkey Kong")

# Calculate tonight's biggest loser
biggest = 0
nameOfLoser = ""
for s in shmucks:
    if s.getTotalOwed() > biggest:
        biggest = s.getTotalOwed()
        nameOfLoser = s.name
    
print("\n" + nameOfLoser + " owes a total of $" + format(biggest, '.2f') + ", making him tonight's biggest loser")




