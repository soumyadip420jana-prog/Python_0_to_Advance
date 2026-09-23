a="Harry"#string is immutable

#string Slicing
nameshort=a[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)

#negative_Slicing
name="harry"
print(name[-4:-1]);#starting from the last index -1


print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

#skip value slicing

# → start from index 0
# 7 → stop before index 7
# 2 → skip 1 element and take the next one


name = "ABCDEFGHIJ"

print(name[0:10:2])#the skip value at the last 2

#output :- ACEGI

