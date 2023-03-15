import random
import time

size = 500
window = Tk()
canvas = Canvas(window, width=size, height=size)
canvas.pack()

Cells=[]
InCells=[] 

for n in range(0,24): #Makes cell grid
    for i in range(0,24):
        Cells.append("○") #○ = uninfected, ● = infected

print(Cells)
input()

Infected=random.randint(0,575)
Cells[Infected]='●'
InCells.append(Infected)

print("\n\n\n\n\n")
print(Cells)

while len(InCells) != 576:
    for t in range(0,len(InCells)):
        time.sleep(0.2)
        CellInfecting=InCells[t]
        
        if CellInfecting != 575:
            Infected = random.randint(1,4)
            if Infected == 1:
                Cells[CellInfecting+1]="●"
                if CellInfecting+1 in InCells:
                    InCells.remove(CellInfecting+1)
                InCells.append(CellInfecting+1)
                
        if CellInfecting <= 551:
            Infected = random.randint(1,4)
            if Infected == 2:
                Cells[CellInfecting+24]="●"
                if CellInfecting+24 in InCells:
                    InCells.remove(CellInfecting+24)
                InCells.append(CellInfecting+24)
                
        if CellInfecting >= 1:
            Infected = random.randint(1,4)
            if Infected == 3:
                Cells[CellInfecting-1]="●"
                if CellInfecting-1 in InCells:
                    InCells.remove(CellInfecting-1)
                InCells.append(CellInfecting-1)
                
        if CellInfecting >= 25:
            Infected = random.randint(1,4)
            if Infected == 4:
                Cells[CellInfecting-24]="●"
                if CellInfecting-24 in InCells:
                    InCells.remove(CellInfecting-24)
                InCells.append(CellInfecting-24)
                
        
    print("\n\n\n\n\n")
    print(Cells)
    print(len(InCells), "Cells infected.")

##    for p in range(len(Cells)):
##        PixeL=canvas.create_rectangle(PrimeList[p],PrimeList[int(p/500)],PrimeList[p],PrimeList[int(p/500)])
##  
    
input()
