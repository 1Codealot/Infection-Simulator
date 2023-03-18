import random
import time

Generation = 0

f = open("Infection_Settings.txt","r")

X=f.readline()
Y=f.readline()

X=int(X[2:])
Y=int(Y[2:])


Cells=[]
InCells=[] 

for n in range(0,Y): #Makes cell grid
    for i in range(0,X):
        Cells.append("○") #○ = uninfected, ● = infected

def Print_As_Grid(X,Y):
    for n in range(len(Cells)):
        if n % X == 0:
            print()
            print(Cells[n],end='')
        else:
            print(Cells[n],end='')

Print_As_Grid(X,Y)
input()

Infected=random.randint(0,len(Cells))
Cells[Infected]='●'
InCells.append(Infected)

print("\n\n\n\n\n")
Print_As_Grid(X,Y)

while len(InCells) != X*Y:
    for t in range(0,len(InCells)):
        time.sleep(0.2)
        CellInfecting=InCells[t]
        
        if CellInfecting != X*Y-1 and CellInfecting % X != X:
            Infected = random.randint(1,4)
            if Infected == 1:
                Cells[CellInfecting+1]="●"
                if CellInfecting+1 in InCells:
                    InCells.remove(CellInfecting+1)
                InCells.append(CellInfecting+1)
                
        if CellInfecting <= X*Y-X:
            Infected = random.randint(1,4)
            if Infected == 2:
                Cells[CellInfecting+X]="●"
                if CellInfecting+X in InCells:
                    InCells.remove(CellInfecting+X)
                InCells.append(CellInfecting+X)
                
        if CellInfecting >= 1 and CellInfecting % X != 0:
            Infected = random.randint(1,4)
            if Infected == 3:
                Cells[CellInfecting-1]="●"
                if CellInfecting-1 in InCells:
                    InCells.remove(CellInfecting-1)
                InCells.append(CellInfecting-1)
                
        if CellInfecting >= X+1:
            Infected = random.randint(1,4)
            if Infected == 4:
                Cells[CellInfecting-X]="●"
                if CellInfecting-X in InCells:
                    InCells.remove(CellInfecting-X)
                InCells.append(CellInfecting-X)

    Generation += 1    
    print("\n\n\n\n\n")
    Print_As_Grid(X,Y)
    
    print("\n",len(InCells), "Cells infected.")
    print("Generation:", Generation)
 
input()
