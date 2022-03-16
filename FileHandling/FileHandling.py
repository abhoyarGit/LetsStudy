with ('Test.txt','r') as myText:
    #data1 = myText.read()
    #data2 = myText.readline()
    data3 = myText.readlines()

print(data3)

memory = {}
for i in range(1,len(data3)):
    pidList = data3[i].split(' ')
    memory[pidList[0]] = float(pidList[-3])



maxValue = max(list(memory.values()))
index = list(memory.values()).index(maxValue)
print(index)
print(list(memory.keys())[10])


