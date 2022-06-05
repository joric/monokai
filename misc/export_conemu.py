import os, re

for s in open(os.environ['FARHOME'] + '\\ConEmu.xml').read().splitlines(True):
    if "joric's monokai" in s:
        out = open('conemu-colors.xml','w')
    if 'out' not in locals():
        continue
    if m:=re.match(r'.*ColorTable(\d\d).*00(\w\w)(\w\w)(\w\w)',s):
        out.write(s)
