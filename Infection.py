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

InCells=[] #Place where cells were infected
Gen_Infected=[] #Generation the cell was infected
        
Gen_Infected = [-1] * (X*Y)

if Immunity == 1:
    for u in range(ImmuneCellCount):
        Gen_Infected[u] = -2
        
    random.shuffle(Gen_Infected)
    random.shuffle(Gen_Infected)
    random.shuffle(Gen_Infected)
    
    Gen_Infected=(list(Gen_Infected))

def Print_As_Grid(X,Y):
    os.system('cls' if os.name == 'nt' else 'clear')
    GriddedString = ''
    for n in range(len(Gen_Infected)):
        if n % X == 0:
            if n != 0:
                GriddedString += "\n"
                
            if Gen_Infected[n] == -1:
                GriddedString += "○" + ''
            elif Gen_Infected[n] == -2:
                GriddedString += "X" + ''
            else:
                GriddedString += "●" + ''
                
        else:
            if Gen_Infected[n] == -1:
                GriddedString += "○" + ''
            elif Gen_Infected[n] == -2:
                GriddedString += "X" + ''
            else:
                GriddedString += "●" + ''

    print(f"{GriddedString}\n{len(InCells)} Cells infected\nGeneration: {Generation}") #Ew

    # GriddedString += "\r"
    # print(f"{GriddedString}",end = "\r")

Print_As_Grid(X,Y)

Seed = input("\nEnter in a seed (or leave blank for random): ")
if Seed != '':
    random.seed(Seed)

Infected=random.randint(0,len(Gen_Infected))
Gen_Infected[Infected]=Generation
InCells.append(Infected)

#print("\n\n\n\n\n")
Print_As_Grid(X,Y)

while len(InCells) != X*Y:
    for t in range(0,len(InCells)):
        CellInfecting=InCells[t]
        
        if CellInfecting != X*Y-1 and CellInfecting % X != X-1:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Gen_Infected[CellInfecting+1] == -1:
                Gen_Infected[CellInfecting+1] = Generation
                if CellInfecting+1 in InCells:
                    InCells.remove(CellInfecting+1)
                InCells.append(CellInfecting+1)
                
        if CellInfecting <= (X*Y-X)-1:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Gen_Infected[CellInfecting+X] == -1:
                Gen_Infected[CellInfecting+X] = Generation
                if CellInfecting+X in InCells:
                    InCells.remove(CellInfecting+X)
                InCells.append(CellInfecting+X)
                
        if CellInfecting >= 1 and CellInfecting % X != 0:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Gen_Infected[CellInfecting-1] == -1:
                Gen_Infected[CellInfecting-1] = Generation
                if CellInfecting-1 in InCells:
                    InCells.remove(CellInfecting-1)
                InCells.append(CellInfecting-1)
                
        if CellInfecting >= X+1:
            Infected = random.randint(1,InfectChance)
            if Infected == 1 and Gen_Infected[CellInfecting-X] == -1:
                Gen_Infected[CellInfecting-X] = Generation
                if CellInfecting-X in InCells:
                    InCells.remove(CellInfecting-X)
                InCells.append(CellInfecting-X)        
    
    if Healing == 1:
        # print("Hello from line 150")
        for h in range(len(Gen_Infected)):
            # print(f"We loopin {Gen_Infected[h]}")
            if (Gen_Infected[h] >= 0) and ((Generation - Gen_Infected[h]) >= MinGensToUninfect) and (len(InCells) >= 10) and (random.randint(1, ChanceOfHealing) == 1):
                Gen_Infected[h] = -1
                InCells.remove(h)
                #del InCells[currentIndex] # Delete currentIndex
                # print("Heloo from the healing alg!!")
            # time.sleep(0.03)
    
    Generation += 1    

    Print_As_Grid(X,Y)
    time.sleep(Delay)

input()
