"""
#!/usr/bin/python
for letters in 'python':

    if letters == 'o':
        break

    print(letters)
var = 10
while var > 5:
    print(var)
    if var == 8:
        print(var)
        break
    var = var -1

for letters in 'devops':
    if letters == 'v':
        continue
    print(letters)

while var > 6:
    print("continue statement:",var)
    if var == 6:
        continue
    var = var -1
    print(var)
"""
########Break command
for letters in 'python':
    if letters == 'h':
        break
    print(letters)
var = int(input("enter number:"))
while var > 5:
    if var == 8:
        break

    print(var)
    var = var - 1
#continue command
for letters in 'python':
    if letters == 'o':
        continue
    print(letters)
var = 10
while var > 6:
    if var == 8:
        continue
    print(var)

    var = var -1