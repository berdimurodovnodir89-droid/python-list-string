text = "Ism:Ali, Familiya:Valiyev, Yil:2002" 
result = text.split(',')
for word in result:
    print(word.strip())