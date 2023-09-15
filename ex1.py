namn = "test.txt"
text= ""
file=open(namn,"r",encoding="utf-8")
text=file.read()
file.close

print(text)
print(text[0])
ord=text.split()
print(ord[0])