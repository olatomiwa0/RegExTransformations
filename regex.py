import rstr
from tdda import rexpy

# create accept strings
acceptRE = []
for x in range(10): 
    acceptRE.append(rstr.xeger('[A-Z0-9]{3} [A-Z0-9]{4}'))

#create reject strings
rejectRE = []
for x in range(10): 
    rejectRE.append(rstr.xeger('[A-Z0-9]{3} [A-Z0-9]{4}'))


results = rexpy.extract(acceptRE)
print('Number of regular expressions found: %d' % len(results))
for r in results:
    print('   ' + r)