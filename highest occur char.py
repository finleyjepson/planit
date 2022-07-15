# finds the most occurring character in the string
string1="iHateuLOL".lower()
list1=[]
list2=[]
for i in string1:
  if i not in list1:
    list1.append(i)
    list2.append(string1.count(i))
# finds max in the list
occ=max(list2)
ele=list1[list2.index(occ)]
# prints the string plus highest occuring character
print("in", string1, "the character", ele, "is the most occurring character")

# contributed by Finley Jepson
