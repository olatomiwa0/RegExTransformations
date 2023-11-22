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

#regular expressions created from input data
acceptRE = rexpy.Extractor(acceptStrings) #acceptRE.results.rex
rejectRE = rexpy.Extractor(rejectStrings) #reject.results.rex

#evaluate no. strings that match RE
for acc1, n1 in zip(acceptRE.results.rex, acceptRE.coverage(dedup=True)):
    print('%d accept string examples are matched by the acceptRE: %s' % (n1, acc1))

for acc2, n2 in zip(acceptRE.results.rex, rejectRE.coverage(dedup=True)):
    print('%d reject string examples are matched by the acceptRE: %s' % (n2, acc2))

for re1, n3 in zip(rejectRE.results.rex, rejectRE.coverage(dedup=True)):
    print('%d reject string examples are matched by the rejectRE: %s' % (n3, re1))

for re2, n4 in zip(rejectRE.results.rex, acceptRE.coverage(dedup=True)):
    print('%d accept string examples are matched by the rejectRE: %s' % (n4, re2))

#######################