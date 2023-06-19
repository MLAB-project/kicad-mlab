#! /bin/sh

#sudo cp src/repo.py /usr/lib/python3/dist-packages/repo.py
#sudo chmod +x src/kicad-footprint-manager
#sudo cp src/kicad-footprint-manager /usr/bin/kicad-footprint-manager


if [ -d "${HOME}/.local/share/kicad/7.0/" ]
then
    echo "Installing for KICAD 7, user folder"
    BASEFOLDER="${HOME}/.local/share/kicad/7.0/"
    VERSION=7

elif [ -d "${HOME}/.local/share/kicad/6.0/" ]
then
    echo "Installing for KICAD 6, user folder"
    BASEFOLDER="${HOME}/.local/share/kicad/6.0/"
    VERSION=6

else
    echo "Error: Directory does not exists.. Try to check this source code"
    exit
fi

echo "Pouzivam slozku:"
echo ${BASEFOLDER}
echo "Verze: ${VERSION}"

#mkdir -p ~/kicad_sources
#cp -r footprints ~/kicad_sources/
#sudo cp -r symbols /usr/share/kicad/library/

ln -s "$(realpath template/mlab-default/)" ${BASEFOLDER}template/
echo $(realpath plugins/*.py) | tr " " "\n" | xargs -I % cp -s % ${BASEFOLDER}scripting/plugins/
echo $(realpath footprints/*.pretty) | tr " " "\n" | xargs -I % ln -s % ${BASEFOLDER}footprints/
echo $(realpath symbols/*.kicad_sym) | tr " " "\n" | xargs -I % cp -s % ${BASEFOLDER}symbols/

#sudo cp -r modules /usr/share/kicad/

#kicad-footprint-manager  -f ~/kicad_sources/footprints
