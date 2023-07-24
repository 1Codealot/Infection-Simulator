import random, time, os

Generation = 0

try:
    f = open("Infection_Settings.txt","r")
    f.close()
except:
    f = open("Infection_Settings.txt","a")
    f.write("X=20\n\
Y=20\n\
InfectChance=20\n\
Healing=1\n\
MinGensToUninfect=20\n\
ChanceOfHealing=40\n\
Immunity=1\n\
ImmuneCellCount=12\n\
Delay=0.2")
    #I guess these are default settings now ¯\_(ツ)_/¯
    f.close()
finally:
    f = open("Infection_Settings.txt","r")
    X = f.readline()
    Y = f.readline()
    InfectChance = f.readline()
    Healing = f.readline()
    MinGensToUninfect = f.readline()
    ChanceOfHealing = f.readline()
    Immunity = f.readline()
    ImmuneCellCount = f.readline()
    Delay = f.readline()

    f.close()

X=int(X[2:])
Y=int(Y[2:])
InfectChance=int(InfectChance[13:])
Healing=int(Healing[8:]) #1 = True because I couldn't get srings to work and idc
MinGensToUninfect=int(MinGensToUninfect[18:])
ChanceOfHealing=int(ChanceOfHealing[16:])
Immunity=int(Immunity[9:])
ImmuneCellCount=int(ImmuneCellCount[16:])
Delay=float(Delay[6:])

InfectedRepresentation = "●"
UnInfectedRepresentation = "○"
ImmuneRepresentation = "X"

AmountOfCells = X*Y # Less computing time needed for making variables

class Cell:
    def __init__(self,Gen_Infected = -1) -> None:
        self.Gen_Infected = Gen_Infected

    def get_cell_type(self) -> str:
        if self.Gen_Infected == -2:
            return ImmuneRepresentation
        elif self.Gen_Infected == -1:
            return UnInfectedRepresentation
        else:
            return InfectedRepresentation

    def infect(self):
        # Part of Infection logic included: random, not already infected
        if  self.Gen_Infected!= Generation and random.randint(1, 100) <= int(InfectChance): # I don't know why I have to cast InfectChance here but for some reason I do
            self.Gen_Infected = Generation

    def heal(self): #                     THe issue was an `==` and not `>=` rhjkwehsnithvgkjklvjikfryhuvgbeiyo
        if Generation - self.Gen_Infected >= int(MinGensToUninfect) and random.randint(1, 100) <= int(ChanceOfHealing): # Also more nonsensical type casting
            self.Gen_Infected = -1


Cells = []

for x in range(AmountOfCells):
    Cells.append(Cell())


if Immunity == 1:
    # Set the generation of {ImmuneCellCount} Cells to -2 so that they are immune.
    # They are randomised

    # Not a fan of this solution but idc
    immuneCell = random.randint(0, AmountOfCells)
    Cells[immuneCell].Gen_Infected = -2

    for n in range(ImmuneCellCount - 1):
        while Cells[immuneCell].Gen_Infected == -2:
            immuneCell = random.randint(0, AmountOfCells)

        Cells[immuneCell].Gen_Infected = -2


def getInfectedCellCount() -> int:
    count = 0
    for i in Cells:
        if i.Gen_Infected >= 0:
            count += 1
    return count


def Print_As_Grid():

    InfectedCellCount: int = 0
    if Generation > 0:
        InfectedCellCount = getInfectedCellCount()

    os.system('cls' if os.name == 'nt' else 'clear')
    GriddedString = ''
    for n in range(AmountOfCells):
        if n % X == 0:
            GriddedString += f'\n'

        GriddedString += f"{Cells[n].get_cell_type()}"

    print(f"{GriddedString}\n\n\nGeneration: {Generation}\nCells infected: {InfectedCellCount}\n")

Print_As_Grid()

Seed = input("\nEnter in a seed (or leave blank for random): ")
if Seed != '':
    random.seed(Seed)

# Infecting 'patient zero' (for lack of better term.)
Cells[random.randint(0, AmountOfCells - 1)].Gen_Infected = Generation


Print_As_Grid()
time.sleep(Delay)

while getInfectedCellCount() != AmountOfCells:
    for C in range(AmountOfCells):
        if (currentCell := Cells[C]).Gen_Infected >= 0: # currentCell stores the Cell object.

            # Right

            if C != AmountOfCells - 1 and C % X != X-1 and Cells[C+1].Gen_Infected == -1 :
                Cells[C+1].infect()

            # Down

            if C <= AmountOfCells - X - 1 and Cells[C+X].Gen_Infected == -1:
                Cells[C+X].infect()

            # Left

            if C >= 1 and C % X != 0 and Cells[C-1].Gen_Infected == -1:
                Cells[C-1].infect()

            # Up

            if C >= X + 1 and Cells[C-X].Gen_Infected == -1:
                Cells[C-X].infect()

            # Healing

            if Healing == 1:
                Cells[C].heal()

    Generation += 1

    Print_As_Grid()
    time.sleep(Delay)

input()
