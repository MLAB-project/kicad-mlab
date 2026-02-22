KiCad MLAB libraries
==========
Libraries are compatible with KiCAD 8.0 and KiCAD 7.0

MLAB-specific KiCAD parts library.


Scripts, settings, symbols, and footprints for KiCad used by the [MLAB-project](http://mlab.cz)

Installation
------------
To install everything, just type:
```sh
$ ./install-all.sh
```
This script makes symlinks from the cloned kicad-mlab repository to `~/.local/share/kicad/8.0/` (or the corresponding KiCAD version folder) for templates, footprints, symbols, and plugins.
Then, the symbol and footprint **libraries need to be manually added and opened in KiCAD as a folder**.
