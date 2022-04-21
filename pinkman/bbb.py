class Score:
    last_n = ''
    name = ''
    kl = 0
    point = 0


data = []
mysum = 0
score = Score()
inFile = open('input.txt', 'r', encoding='utf8')
for line in inFile:
    myline = line.strip('\n')
    # data = myline.split(sep=' ')
    last_n, name, kl, point = myline.split(sep=' ')
    score.last_n = last_n
    score.name = name
    score.kl = int(kl)
    score.point = int(point)
    data.append((score.kl, score.point))
    # print(myline)
inFile.close()
# print(*data)
data.sort()
# print(*data)
# Создаем Список из кортежей [класс][сумма][число учеников]
mysum = []
start = 0
index = 0
# print("length of data list is", len(data))
for i in range(9, 12):
    temp = 0
    count = 0
    mysum.append((i, temp, count))
    # print(i)
    for j in range(start, len(data)):
        # print("start =", start)
        if data[j][0] == i:
            temp += data[j][1]
            count += 1
            mysum[index] = (i, temp, count)
        else:
            # mysum.append((i, temp, count))
            start = j
            index += 1
            break

# surn, name, kl, grade = inFile.readline().split(' ')
# print(kl, grade)
# print(mysum)

for value in mysum:
    print(value[1] / value[2], end=" ")