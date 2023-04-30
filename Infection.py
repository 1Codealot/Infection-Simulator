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

Cells=[] #Main List
InCells=[] #Place where cells were infected
Gen_Infected=[] #Generation the cell was infected

for n in range(0,Y): #Makes cell grid
    for i in range(0,X):
        Cells.append("○") #○ = uninfected, ● = infected
        Gen_Infected.append(-1)

if Immunity == 1:
    for u in range(ImmuneCellCount):
        Cells[u] = "X"
        Gen_Infected[u] = 9999
        
    temp = list(zip(Cells, Gen_Infected))
    random.shuffle(temp)
    random.shuffle(temp)
    random.shuffle(temp) #So it gets more shufflesd.
    Cells, Gen_Infected = zip(*temp)

    Cells=(list(Cells))
    Gen_Infected=(list(Gen_Infected))

def Print_As_Grid(X,Y):
    os.system('cls' if os.name == 'nt' else 'clear')
    GriddedString = ''
    for n in range(len(Cells)):
        if n % X == 0:
            #print()
            #print(Cells[n],end='')
            if n != 0:
                GriddedString += "\n"
            GriddedString += Cells[n] + '' 
        else:
            #print(Cells[n],end='')
            GriddedString += Cells[n] + ''

    print(f"{GriddedString}\n{len(InCells)} Cells infected\nGeneration: {Generation}", end="\r") #Ew

    # GriddedString += "\r"
    # print(f"{GriddedString}",end = "\r")

Print_As_Grid(X,Y)

Seed = input("\nEnter in a seed (or leave blank for random): ")
if Seed != '':
    random.seed(Seed)

Infected=random.randint(0,len(Cells))
Cells[Infected]='●'
Gen_Infected[Infected]=Generation
InCells.append(Infected)

#print("\n\n\n\n\n")
Print_As_Grid(X,Y)

while len(InCells) != X*Y:
    for t in range(0,len(InCells)):
        CellInfecting=InCells[t]
        
        if CellInfecting != X*Y-1 and CellInfecting % X != X-1:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Cells[CellInfecting+1] != "X":
                Cells[CellInfecting+1]="●"
                if CellInfecting+1 in InCells:
                    InCells.remove(CellInfecting+1)
                InCells.append(CellInfecting+1)
                
        if CellInfecting <= (X*Y-X)-1:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Cells[CellInfecting+X] != "X":
                Cells[CellInfecting+X]="●"
                if CellInfecting+X in InCells:
                    InCells.remove(CellInfecting+X)
                InCells.append(CellInfecting+X)
                
        if CellInfecting >= 1 and CellInfecting % X != 0:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Cells[CellInfecting-1] != "X":
                Cells[CellInfecting-1]="●"
                if CellInfecting-1 in InCells:
                    InCells.remove(CellInfecting-1)
                InCells.append(CellInfecting-1)
                
        if CellInfecting >= X+1:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Cells[CellInfecting-X] != "X":
                Cells[CellInfecting-X]="●"
                if CellInfecting-X in InCells:
                    InCells.remove(CellInfecting-X)
                InCells.append(CellInfecting-X)

    if Healing == 1:
        for h in InCells:
            if Generation - Gen_Infected[h] >= MinGensToUninfect and len(InCells) >= 10:
                if random.randint(1,ChanceOfHealing) == 1:
                    Cells[h] = "○"
                    Gen_Infected[h] = -1
                    InCells.remove(h)
    
    Generation += 1    

    Print_As_Grid(X,Y)
    time.sleep(Delay)

input()
