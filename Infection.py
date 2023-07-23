import random, time, os

Generation = 0

try:
    f = open("Infection_Settings.txt","r")
    f.close()
except:
    f = open("Infection_Settings.txt","a")
    f.write("X=20\n\
Y=20\n\
InfectChance=5\n\
Healing=1\n\
MinGensToUninfect=20\n\
ChanceOfHealing=5\n\
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
    def __init__(self, ID, Gen_Infected = -1) -> None:
        self.ID = ID
        self.Gen_Infected = Gen_Infected

    def set_Gen_Infected(self, Generation):
        self.Gen_Infected = Generation

    def get_cell_type(self) -> str:
        if self.Gen_Infected == -2:
            return ImmuneRepresentation
        elif self.Gen_Infected == -1:
            return UnInfectedRepresentation
        else:
            return InfectedRepresentation

Cells = []

for x in range(AmountOfCells):
    Cells.append(Cell(x, -1))

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


def getInfectedCellCount():
    count = 0
    for i in Cells:
        if i.Gen_Infected >= 0:
            count += 1
    return count


def Print_As_Grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    GriddedString = ''
    for n in range(AmountOfCells):
        if n % X == 0:
            GriddedString += f'\n'

        GriddedString += f"{Cells[n].get_cell_type()}"

    print(f"{GriddedString}\n\n\n\nGeneration: {Generation}\nCells infected: {getInfectedCellCount}\n")

Print_As_Grid()

Seed = input("\nEnter in a seed (or leave blank for random): ")
if Seed != '':
    random.seed(Seed)

# Infecting 'patient zero' (for lack of better term.)
Cells[random.randint(0, AmountOfCells)].Gen_Infected = Generation


Print_As_Grid()

## Infecting logic
## DOES NOT WORK CURRENTLY, DO NOT USE

while len(InCells) != AmountOfCells:
    for infectiousCell in InCells:

        ## Infect to the right

        if infectiousCell != X * Y - 1 and infectiousCell % X != X - 1 and random.randint(1, InfectChance) == 1 and Gen_Infected[infectiousCell + 1] == -1: # Stops it infecting after the last cell and stops it wrapping around then it chooses randomly if it wants to infect and then if the cell it trys to infect is not already infected or immune.
            # It's probably better to do this in multiple if statements for readability or in a different order to be quicker but I'm not really sure how to test but I also don't care, its python, no one cares of its slow.
            Gen_Infected[infectiousCell + 1] = Generation
            InCells.append(infectiousCell + 1)

        ## Infects downwards

        if infectiousCell <= (X * Y - X) - 1 and random.randint(1, InfectChance) == 1 and Gen_Infected[infectiousCell + X] == -1:
            Gen_Infected[infectiousCell + X] = Generation
            InCells.append(infectiousCell + X)

        ## Infects to the left

        if infectiousCell >= 1 and infectiousCell % X != 0 and random.randint(1, InfectChance) == 1 and Gen_Infected[infectiousCell - 1] == -1:
            Gen_Infected[infectiousCell - 1] = Generation
            InCells.append(infectiousCell - 1)

        ## Infects upwards

        if infectiousCell >= X + 1 and random.randint(1, InfectChance) == 1 and Gen_Infected[infectiousCell - X] == -1:
            Gen_Infected[infectiousCell - X] = Generation
            InCells.append(infectiousCell - X)


    if Healing == 1:
        for h in InCells:
            if Generation - Gen_Infected[h] >= MinGensToUninfect and len(InCells) >= 10 and random.randint(1,ChanceOfHealing) == 1:
                Gen_Infected[h] = -1
                InCells.remove(h)


    Generation += 1

    Print_As_Grid(X,Y)
    time.sleep(Delay)

input()
