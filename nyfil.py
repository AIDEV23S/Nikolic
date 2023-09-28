name = "filA.txt"
text =''
file = open(name, "r", encoding='utf-8' )

text = file.read()
list=[]
print (text)
print(text[0])
ord = text.split()
ord.append(list)
print (ord)