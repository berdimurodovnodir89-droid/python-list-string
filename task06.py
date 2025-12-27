
text = 'olol radar makka non kiyik'
result = text.split()
palindromlar = []
total = ",".join(result)
for son in text:
    if son == son[::-1]:
     palindromlar.append(son)
     

print(palindromlar)