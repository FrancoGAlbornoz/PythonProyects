miset = set((1,2,3,4,5))

#print(type(miset))

#print(len(miset))

#print(2 in miset)

s1 = {1,2,3}
"""
s2 = {3,4,5}

s3 = s1.union(s2)

print(s3)
"""
s1.add(4)
print(s1)
s1.remove(1)
print(s1)
s1.clear()
print(s1)