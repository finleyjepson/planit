string1="iHateuLOL".lower()
list1=[]
list2=[]
for i in string1:
  if i not in list1:
    list1.append(i)
    list2.append(string1.count(i))
occ=max(list2)
ele=list1[list2.index(occ)]
print("in", string1, "the character", ele, "is the most occurring character")