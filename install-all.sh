#! /bin/sh

sudo cp src/repo.py /usr/lib/python3/dist-packages/repo.py
sudo chmod +x src/kicad-footprint-manager
sudo cp src/kicad-footprint-manager /usr/bin/kicad-footprint-manager

cp -r footprints ~/kicad_sources
sudo cp -r symbols /usr/share/kicad/library
sudo cp -r template /usr/local/share/kicad
sudo cp -r template /usr/share/kicad
sudo cp -r modules /usr/share/kicad

kicad-footprint-manager  -f ~/kicad_sources/footprints
