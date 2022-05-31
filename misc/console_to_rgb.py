import re

c={}

for s in open('conemu-colors.xml').read().splitlines():
    if m:=re.match(r'.*ColorTable(\d\d).*00(\w\w)(\w\w)(\w\w)',s):
        c['#%X' % int(m[1])] = '#'+m[4]+m[3]+m[2]

out = open('../hrd/monokai-rgb.hrd','w')

for s in open('../hrd/monokai.hrd').read().splitlines(True):
    out.write(re.sub(r'(#\w)', lambda x:c.get(x.group(0).upper(),'#0'), s))
