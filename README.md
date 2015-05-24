KiCad Mlab
==========

Scripts, setting, symbols and footprints for KiCad used by the [MLAB-project](http://mlab.cz)

Every new symbol and footprint should be added the official kicad repository.

Installation
------------

To install everthing just type:
```sh
$ ./install-all.sh
```

This script also updates libraries with schematic symbols, so it migth be a good idea to run it every week or so, to keep everything up to date.

KiCad Footprint Manager
-----------------------

Downloads/updates .pretty repositories for offline use.
To download/update repositories from [KiCad](https://github.com/KiCad) use this:

```sh
$ kicad-footprint-manager  -f ~/kicad_sources/footprints
```

Note: you need to run this command every time you update kicad
