name = "filA.txt"
text =''
file = open(name, "r", encoding='utf-8' )
text = file.read()
file.close
print(text.split())