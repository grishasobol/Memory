import re
import argparse

m = argparse.ArgumentParser(description="Memory")
m.add_argument("strs", type=str, action='store', nargs='*')
m.add_argument("--mem_file", "-m", type=str, action='store')
m.add_argument("--new_mem", "-n", action='store_true')
args = m.parse_args()

MEM_FILE = None

from os import path
home = path.expanduser('~')
config_file = path.join(home, '.config', 'mymem.config')
if path.isfile( config_file):
    CONFIGS = open(config_file).read()
    MEM_FILE = path.expanduser(re.search('memfile=(.*)', CONFIGS).group(1))

if args.mem_file:
    MEM_FILE = args.mem_file

if not MEM_FILE:
    print("No mem file, please specify in {}".format( config_file))
    exit(1)

if args.new_mem:
    s = '\n## ' + input('Tags: ') + '\n'
    while True:
        next_line = input()
        if next_line == '':
            break
        s += next_line + '\n'
    with open( MEM_FILE, 'a') as f:
        f.write(s)
    exit(0)

mems = re.split( "##", open(MEM_FILE).read(), flags=re.MULTILINE)
for mem in mems:
    is_suit = True
    for s in args.strs:
        if not re.search(s, mem, flags=re.MULTILINE | re.IGNORECASE):
            is_suit = False
            break
    if is_suit:
        print('----------- ' + mem.strip())
