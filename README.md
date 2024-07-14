KiCad MLAB libraries
==========
Libraries are compatibile with KiCAD 8.0 and KiCAD 7.0

MLAB specific KiCAD parts library.


Scripts, setting, symbols and footprints for KiCad used by the [MLAB-project](http://mlab.cz)

Installation
------------
To install everthing just type:
```sh
$ ./install-all.sh
```
This script make symlinks from cloned kicad-mlab repository to `~/.local/share/kicad/8.0/` (or corresponding KiCAD 7.0 folder) for templates, footprints, symbols and plugins.
Then the symbol and footprint libraries should be added and opened in KiCAD manually.
