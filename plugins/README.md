# MLAB layout generator

MLAB layout generator je plugin do CAM nástroje KiCAD. Plugin umožňuje snadno a přesně umístit montážní otvory MLAB modulů a vytvořit jeho obrys.

#### 1. do PCB layoutu vložte součástky ze schématu, především montážní otvory. 
![obrazek](https://user-images.githubusercontent.com/5196729/217681811-f4ec1e3d-4cc8-44ed-899a-7b663f6295ef.png)


#### 2. Otevřte rozhraní pro nastavení rozměru MLAB desky

  Nástroje -> Externí pluginy -> MLAB PCB layout generator

#### 3. V okně vyplňte rozměry desky
Rozměry desky se zadávají v násobcích MLAB patternu (10.16mm) mezi šrouby. 

V poli 'Hole names' je potřeba mít správně vyplněné reference na montážní otvory. Výchozí hodnotou jsou otvory označené M1-M4. 

![obrazek](https://user-images.githubusercontent.com/5196729/217682198-2e11ca6d-734a-4d6f-92ee-f511236133c2.png)


#### 4. Klikněte prepare module layout

Po stisknutí na tlačítko 'prepare module layout'. Dojde k přemístění otvorů do správného rozměru, počátek souřadnicové mřížky se přesune do rohu modulu a vytvoří se obrys modulu ve vrstvě Edge-Cuts. 
![obrazek](https://user-images.githubusercontent.com/5196729/217682318-598da928-3f21-46cc-b00f-9ae56d853c36.png)
