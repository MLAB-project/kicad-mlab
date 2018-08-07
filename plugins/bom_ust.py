
#    python "path/bom_ust.py" "%I" "%O"

from __future__ import print_function

import kicad_netlist_reader
import json, csv
import sys
net = kicad_netlist_reader.netlist(sys.argv[1])

print("...................")
print(sys.argv)

try:
    f = open(sys.argv[2]+'.ust_bom', 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print( __file__, ":", e, sys.stderr )
    f = sys.stdout

component_list = []
components = net.getInterestingComponents()

for c in components:
    fields = c.getFieldNames()
    c_dict = {}

    # bohuzel kicad tyto parametry v prikazu getFieldNames vynechava....
    c_dict['Ref'] = c.getRef()
    c_dict['Value'] = c.getValue()
    c_dict['Footprint'] = c.getFootprint()
    c_dict['Datasheet'] = c.getDatasheet()
    c_dict['Tstamp'] = c.getTimestamp()

    for field in fields:
        c_dict[field] = c.getField(field)
        print('field', field)
    component_list += [c_dict]

print(component_list)
print("Done...")

with f as outfile:
    json.dump(component_list, outfile,  sort_keys = True, indent = 4)
