import csv

first_r = True
Head = []
d = []
with open('Student_marks_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:

        # This if statement is used for separate the title row in separate list

        if first_r:
            Head = row
            first_r = False


# And this part is the calculation of total marks happened ,and append the marks and total in same list
        else:
            temp = [row[0]]
            total = 0
            for i in range(1, len(row)):
                temp.append(int(row[i]))
                total += int(row[i])
            temp.append(total)
            d.append(temp)


# This part contains the step of finding topper in each subject
maxMath = [0, 0]
maxBio = [0, 0]
maxEng = [0, 0]
maxPhy = [0, 0]
maxChem = [0, 0]
maxHindi = [0, 0]
for i in range(len(d)):
        if d[i][1] > maxMath[0]:
            maxMath[0] = d[i][1]
            maxMath[1] = d[i][0]
        if d[i][2] > maxBio[0]:
            maxBio[0] = d[i][2]
            maxBio[1] = d[i][0]
        if d[i][3] > maxEng[0]:
            maxEng[0] = d[i][3]
            maxEng[1] = d[i][0]
        if d[i][4] > maxPhy[0]:
            maxPhy[0] = d[i][4]
            maxPhy[1] = d[i][0]
        if d[i][5] > maxChem[0]:
            maxChem[0] = d[i][5]
            maxChem[1] = d[i][0]
        if d[i][6] > maxHindi[0]:
            maxHindi[0] = d[i][6]
            maxHindi[1] = d[i][0]
print("Topper in Maths is {}".format(maxMath[1]))
print("Topper in Biology is {}".format(maxBio[1]))
print("Topper in English is {}".format(maxEng[1]))
print("Topper in Physics is {}".format(maxPhy[1]))
print("Topper in Chemistry is {}".format(maxChem[1]))
print("Topper in Hindi is {}".format(maxHindi[1]))


# This part contains top 3 students in a csv file

f = [0, 0]
s = [0, 0]
t = [0, 0]

for i in range(len(d)):
    if d[i][7] > t[0]:
        if d[i][7] > s[0]:
            if d[i][7] > f[0]:
                s[0] = f[0]
                s[1] = f[1]
                f[0] = d[i][7]
                f[1] = d[i][0]
            else:
                t[0] = s[0]
                t[1] = s[1]
                s[0] = d[i][7]
                s[1] = d[i][0]
        else:
            t[0] = d[i][7]
            t[1] = d[i][0]

print("\nBest students in the class are {}, {}, {} ".format(f[1], s[1], t[1]))
