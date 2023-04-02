import os, re
import xml.etree.ElementTree as ET

# 1. Exports conemu colors ('Joric Monokai' scheme) from %FARHOME%/conemu.xml to conemu-colors.xml
# 2. Exports colors from conemu-colors.xml and monokai.hrd to hrd/monokai-rgb.hrd

colors_filename = "./conemu-colors.xml"

try:
    tree = ET.parse(os.environ['FARHOME'] + '\\ConEmu.xml')
    elem = tree.getroot().find("./key/key/key/key/value/[@data='Joric Monokai']/..")
    if elem:
        open(colors_filename,'wb').write(ET.tostring(elem))
except:
    print('Scheme not found, converting', colors_filename, '...')

c={}
for s in open(colors_filename).read().splitlines():
    if m:=re.match(r'.*ColorTable(\d\d).*00(\w\w)(\w\w)(\w\w)',s):
        c['#%X' % int(m[1])] = '#'+m[4]+m[3]+m[2]

out = open('../monokai/monokai-rgb.hrd','w')
for s in open('../monokai/monokai.hrd').read().splitlines(True):
    out.write(re.sub(r'(#\w)', lambda x:c.get(x.group(0).upper(),'#0'), s))
