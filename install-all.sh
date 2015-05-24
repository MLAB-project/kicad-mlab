#! /bin/bash

sudo cp src/repo.py /usr/lib/python3/dist-packages/repo.py
sudo chmod +x src/kicad-footprint-manager
sudo cp src/kicad-footprint-manager /usr/bin/kicad-footprint-manager

mkdir -p ~/kicad_sources

cp -r footprints ~/kicad_sources

kicad-footprint-manager  -f ~/kicad_sources/footprints

sudo cp -r symbols/* /usr/local/share/kicad/library
sudo cp -r modules   /usr/local/share/kicad

if [ ! -e ~/kicad_sources/kicad-library ]; then
    git clone https://github.com/KiCad/kicad-library ~/kicad_sources/kicad-library
else
    wd=$(pwd)
    cd ~/kicad_sources/kicad-library
    git pull
    cd $wd
fi

sudo cp -r ~/kicad_sources/kicad-library/library /usr/share/kicad/

beg=$(grep -B 10000 eeschema/libraries template/mlab-default/mlab-default.pro | tr -d " ")
end=$(grep -A 10000 pcbnew template/mlab-default/mlab-default.pro | tr -d " ")

rm template/mlab-default/mlab-default.pro

for line in $beg; do
    echo $line >> template/mlab-default/mlab-default.pro
done

i=1
for lib in $(ls /usr/local/share/kicad/library | grep .lib | cut -d "." -f 1); do
    echo "LibName$i=$lib" >> template/mlab-default/mlab-default.pro
    ((i++))
done

for line in $end; do
    echo $line >> template/mlab-default/mlab-default.pro
done

sudo cp -r template /usr/local/share/kicad
