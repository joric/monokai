import os, re
import xml.etree.ElementTree as ET

colors_filename = "./conemu-colors.xml"

tree = ET.parse(os.environ['FARHOME'] + '\\ConEmu.xml')
elem = tree.getroot().find("./key/key/key/key/value/[@data='Joric Monokai']/..")
open(colors_filename,'wb').write(ET.tostring(elem))

c={}
for s in open(colors_filename).read().splitlines():
    if m:=re.match(r'.*ColorTable(\d\d).*00(\w\w)(\w\w)(\w\w)',s):
        c['#%X' % int(m[1])] = '#'+m[4]+m[3]+m[2]

out = open('../hrd/monokai-rgb.hrd','w')
for s in open('../hrd/monokai.hrd').read().splitlines(True):
    out.write(re.sub(r'(#\w)', lambda x:c.get(x.group(0).upper(),'#0'), s))

