

foo = open("ourfile.txt","w")
fruitbowl = ["apple", "pear", "grapes"]
for fruit in fruitbowl:
    print(fruit, file=foo)

foo.close()