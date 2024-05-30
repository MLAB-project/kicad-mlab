# MLAB layout generator

The MLAB layout generator is a plugin for the [KiCAD CAM tool](https://www.kicad.org/). The plugin allows for easy and precise placement of MLAB module mounting holes to the grid and the creation of the module outline.

#### 1. Insert components from the schematic into the PCB layout, primarily the mounting holes.

![PCB of MLAB design just opened in KiCAD](https://user-images.githubusercontent.com/5196729/217681811-f4ec1e3d-4cc8-44ed-899a-7b663f6295ef.png)

#### 2. Open the interface to set the dimensions of the MLAB board

  Tools -> External plugins -> MLAB PCB layout generator

#### 3. Fill in the board dimensions in the window
Board dimensions are specified in multiples of the MLAB pattern (10.16mm) between the screws.

The 'Hole names' field needs to have the correct references to the mounting holes. The default values are holes labeled M1-M4.

![setup of MLAB module size](https://user-images.githubusercontent.com/5196729/217682198-2e11ca6d-734a-4d6f-92ee-f511236133c2.png)

#### 4. Click 'prepare module layout'

After pressing the 'prepare module layout' button, the holes will be moved to the correct dimensions, the origin of the coordinate grid will be shifted to the corner of the module, and the module outline will be created in the Edge-Cuts layer.

![aligned holes with mlab layout in the grid](https://user-images.githubusercontent.com/5196729/217682318-598da928-3f21-46cc-b00f-9ae56d853c36.png)
