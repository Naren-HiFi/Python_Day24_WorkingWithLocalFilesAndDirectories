with open("../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

'''
 ôpen() method opens the file.

file = open("my_file.txt")

read() method returns the content of the file as a string.
contents = file.read()
print(contents)

 Why do we need to close the file using close() method?
When python opens up the file, it basically takes up some of the resources of your computer.
At some point later on, it might decide to close it and free up those resources.
We dunno when that's gonna happen

file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode='w') as file:
    file.write("New text")
    
with open("Details.txt", mode='w') as file:
    file.write('\n'.join(['All is well'] * 10))

'''
