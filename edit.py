fname = "mail.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

print(content)

file = open("new.txt","w")

for name in content:
    name+="@bennett.edu.in\n"
    file.write(name)

