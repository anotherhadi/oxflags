####################################################################
#           ______________________________________
#  ________|                0xFlags               |_______
#  \       |                                      |      /
#   \      |              @0x68616469             |     /
#   /      |______________________________________|     \
#  /__________)                                (_________\
#
# A Handy Package to Parse Command-Line Arguments
#
# Github repo : https://github.com/0x68616469/oxflags
#
####################################################################

import sys
from oxtables import Table
from oxansi import Short as a

class Flag:

    def __init__(self, **kwargs): 
        self.description = kwargs.get('description', '')
        self.flags = kwargs.get('flags', [])
    
    class flag:
        def __init__(self, **kwargs):
            self.name = kwargs.get('name', '').replace('-','')
            self.short = kwargs.get('short', '')
            self.full = kwargs.get('full', '')
            self.default = kwargs.get('default', '')
            self.type = kwargs.get('type', 'string')
            self.required = kwargs.get('required', False)
            self.help = kwargs.get('help', '')
            
    def new(self, **kwargs):
        short = kwargs.get('short', '')
        full = kwargs.get('full', '')
        default = kwargs.get('default', '')
        type = kwargs.get('type', 'string')
        required = kwargs.get('required', False)
        help = kwargs.get('help', '')

        if 'full' not in kwargs:
            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Long option required: (.., full='..') ")
            sys.exit(1)
        
        if (default == "" and type != "bool") and (default == "" and required != True):
            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Default value required for {full}.")
            sys.exit(1)
    
        self.flags.append(self.flag(short=short, full=full, default=default, type=type, required=required, help=help))
                
    def parse(self):
        for flag in self.flags:
            setattr(self, flag.full.replace('-',''), flag.default)
        
        argc = len(sys.argv)
        i = 1
        while i < argc:
            for flag in self.flags:
                if sys.argv[i] == flag.short or sys.argv[i] == flag.full:
                    if flag.type == "bool":
                        if flag.default == True:
                            setattr(self, flag.full.replace('-',''), False)
                        else:
                            setattr(self, flag.full.replace('-',''), True)
                    
                    elif flag.type == "int":
                        i += 1
                        if i >= argc:
                            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Missing \"int\" argument for \"{flag.full}\".")
                            sys.exit(1)
                        setattr(self, flag.full.replace('-',''), int(sys.argv[i]))

                    else: # Consider as string
                        i += 1
                        if i >= argc:
                            print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Missing \"string\" argument for \"{flag.full}\".")
                            sys.exit(1)
                        setattr(self, flag.full.replace('-',''), sys.argv[i])
                    
                    flag.required = False
                    break
                
                elif sys.argv[i] == "-h" or sys.argv[i] == "--help":
                    print(f"{a.bl}[{a.g}?{a.bl}] {a.bl}Help: {a.rst}{self.description}.")
                    th = Table(spacer=True, style="=", border_color="black")
                    th.add(["", "Option", "Description", "Default"])
                    for flag in self.flags:
                        th.add([flag.short, flag.full, flag.help, flag.default])
                    th.draw()
                    sys.exit(0)
                    
            else:
                print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}\"{sys.argv[i]}\" unknown.")
                sys.exit(1)
                
            i += 1
            
        for flag in self.flags:
            if flag.required == True:
                print(f"{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}\"{flag.full}\" is required.")
                sys.exit(1)
