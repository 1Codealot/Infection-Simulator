import random, time, os, sys

Generation = 0

try:
    f = open("Infection_Settings.txt","r")
    f.close()
except FileNotFoundError:
    print("Warning: Infection_Settings.txt file not found. Creating new file with default settings; you can change these later.")
    f = open("Infection_Settings.txt","a")
    f.write("X=20\n\
Y=20\n\
InfectChance=20\n\
Healing=1\n\
MinGensToUninfect=20\n\
ChanceOfHealing=40\n\
Immunity=1\n\
ImmuneCellCount=12\n\
ImmunityAfterHealingLength=10\n\
Delay=0.2\n\
ShouldUseColours=1\
")
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
    ImmunityAfterHealingLength = f.readline()
    Delay = f.readline()
    ShouldUseColours = f.readline()

    f.close()

X=int(X[2:])
Y=int(Y[2:])
InfectChance=int(InfectChance[13:])
Healing=int(Healing[8:]) #1 = True because I couldn't get srings to work and idc
MinGensToUninfect=int(MinGensToUninfect[18:])
ChanceOfHealing=int(ChanceOfHealing[16:])
Immunity=int(Immunity[9:])
ImmuneCellCount=int(ImmuneCellCount[16:])
ImmunityAfterHealingLength=int(ImmunityAfterHealingLength[27:])
Delay=float(Delay[6:])
ShouldUseColours=int(ShouldUseColours[17:])

AmountOfCells = X*Y # Less computing time needed for making variables

class Cell:
    def __init__(self,Gen_Infected = -1) -> None:
        self.Gen_Infected = Gen_Infected
        self.last_time_infected = 0

        if ShouldUseColours == 1:
            self.InfectedRepresentation = '\x1b[0;31;40m' + "●" + '\x1b[0m'
            self.UnInfectedRepresentation = '\x1b[0;32;40m' + "○" + '\x1b[0m'
            self.ImmuneRepresentation = '\x1b[0;34;40m' + "X" + '\x1b[0m'
        else:
            self.InfectedRepresentation = "●"
            self.UnInfectedRepresentation = "○"
            self.ImmuneRepresentation = "X"


    def get_cell_type(self) -> str:
        if self.Gen_Infected == -2:
            return self.ImmuneRepresentation
        elif self.Gen_Infected == -1:
            return self.UnInfectedRepresentation
        else:
            return self.InfectedRepresentation

    def infect(self):
        # Part of Infection logic included: random, not already infected
        if  self.Gen_Infected!= Generation and random.randint(1, 100) <= int(InfectChance): # I don't know why I have to cast InfectChance here but for some reason I do
            if Generation - self.last_time_infected >= int(ImmunityAfterHealingLength):
                self.Gen_Infected = Generation

            elif Generation <= int(ImmunityAfterHealingLength):
                self.Gen_Infected = Generation

    def heal(self): #                     THe issue was an `==` and not `>=` rhjkwehsnithvgkjklvjikfryhuvgbeiyo
        if Generation - self.Gen_Infected >= int(MinGensToUninfect) and random.randint(1, 100) <= int(ChanceOfHealing): # Also more nonsensical type casting
            self.Gen_Infected = -1
            self.last_time_infected = Generation


Cells: list[Cell] = []

for x in range(AmountOfCells):
    Cells.append(Cell())


if Immunity == 1:
    # Set the generation of {ImmuneCellCount} Cells to -2 so that they are immune.
    # They are randomised

    # Not a fan of this solution but idc
    immuneCell = random.randint(0, AmountOfCells)
    Cells[immuneCell].Gen_Infected = -2

    for j in range(ImmuneCellCount - 1):
        while Cells[immuneCell].Gen_Infected == -2:
            immuneCell = random.randint(0, AmountOfCells)

        Cells[immuneCell].Gen_Infected = -2


def getInfectedCellCount() -> int:
    count = 0
    for i in Cells:
        if i.Gen_Infected >= 0:
            count += 1
    return count


def getAsGrid(shouldOutput = True):

    InfectedCellCount: int = 0
    if Generation >= 0:
        InfectedCellCount = getInfectedCellCount()

    GriddedString = ''
    for n in range(AmountOfCells):
        if n % X == 0:
            GriddedString += f'\n'

        GriddedString += f"{Cells[n].get_cell_type()}"

    if shouldOutput:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{GriddedString}\n\n\nGeneration: {Generation}\nCells infected: {InfectedCellCount}\n")

    else: return GriddedString

getAsGrid()

# Infecting 'patient zero' (for lack of better term.)
Cells[random.randint(0, AmountOfCells - 1)].Gen_Infected = Generation

def infecting():
    for currentCell in range(AmountOfCells):
        if Cells[currentCell].Gen_Infected >= 0 and Cells[currentCell].Gen_Infected != Generation: # currentCell stores the Cell object.

            # Right
            #  Stops outOfIndexError                  Stops wrapping around        Makes sure that Cell is uninfected
            if (currentCell != AmountOfCells - 1) and (currentCell % X != X-1) and (Cells[currentCell+1].Gen_Infected == -1):
                Cells[currentCell+1].infect()

            # Down
            #  Stops outOfIndexError                      Makes sure that Cell is uninfected
            if (currentCell <= AmountOfCells - X - 1) and (Cells[currentCell+X].Gen_Infected == -1):
                Cells[currentCell+X].infect()

            # Left
            #  Stops outOfIndexError  Stops wrapping around      Makes sure that Cell is uninfected
            if (currentCell >= 1) and (currentCell % X != 0) and (Cells[currentCell-1].Gen_Infected == -1):
                Cells[currentCell-1].infect()

            # Up
            #  Stops outOfIndexError      Makes sure that Cell is uninfected
            if (currentCell >= X + 1) and (Cells[currentCell-X].Gen_Infected == -1):
                Cells[currentCell-X].infect()

def healing():
    for currentCell in range(AmountOfCells):
        if Cells[currentCell].Gen_Infected >= 0: # currentCell stores the Cell object.
            Cells[currentCell].heal()

def main():
    global Generation # This was a solution to a problem I had.
    # I need to make a main function so that I can call it on a button press.
    # No args because reasons.
    while ((cellCount:=getInfectedCellCount()) != AmountOfCells and Healing == 0) or (cellCount != 0):
        startTime = time.time()

        infecting()
        Generation += 1
        if Healing == 1:
            healing()
        getAsGrid()

        if (finalDelay:= time.time()-startTime) <= Delay:
            time.sleep(Delay-finalDelay)
        elif Delay < 0:
            input()

if __name__ == '__main__':

    ## Seed stuff
    if len(sys.argv) >= 2:
        random.seed(sys.argv[1])
    else:
        Seed = input("\nEnter in a seed (or leave blank for random): ")
        if Seed != '':
            random.seed(Seed)
        else:
            Seed = time.time()
            random.seed(Seed)

    main()
