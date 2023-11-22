import rstr
from tdda import rexpy

# create accept strings
acceptStrings = []
for r in range(10): 
    acceptStrings.append(rstr.xeger('[A-Z0-9]{3} [A-Z0-9]{4}'))

#print(acceptStrings)

#create reject strings
rejectStrings = []
for r in range(10): 
    rejectStrings.append(rstr.xeger('reject'))

#print(rejectStrings)

results = rexpy.extract(acceptStrings)
print('Number of regular expressions found: %d' % len(results))
for r in results:
    print('   ' + r)

newReg = rexpy.Extractor(acceptStrings)
print(newReg)
