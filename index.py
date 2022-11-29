import csv

# Reading CSV file
first_r = True
Head = []
d = []
with open('Student_marks_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:

        if first_r:
            Head = row
            first_r = False
        else:
            temp = [row[0]]
            total = 0
            for i in range(1, len(row)):
                temp.append(int(row[i]))
                total += int(row[i])
            temp.append(total)
            d.append(temp)


# Function for finding topper in each subject
def findTopper(rankList, subject_name):
    subject_index = {
        'Maths': 1,
        'Biology': 2,
        'English': 3,
        'Physics': 4,
        'Chemistry': 5,
        'Hindi': 6
    }
    maxMark = [rankList[0]]
    for i in range(1, len(rankList)):
        index = subject_index[subject_name]
        if rankList[i][index] > maxMark[0][index]:
            maxMark = [rankList[i]]
        elif rankList[i][index] == maxMark[0][index]:
            maxMark.append(rankList[i])

    name = ""
    for i in range(0, len(maxMark)):
        name += maxMark[i][0] + ' '
    return "Topper in {} {} {}".format(subject_name, "are" if len(maxMark) > 1 else 'is', name)


# Function for finding top three students
def topThree(rank):
    first = [0, 0]
    second = [0, 0]
    third = [0, 0]

    for j in range(len(rank)):
        if rank[j][7] > third[0]:
            if rank[j][7] > second[0]:
                if rank[j][7] > first[0]:
                    second[0] = first[0]
                    second[1] = first[1]
                    first[0] = rank[j][7]
                    first[1] = rank[j][0]
                else:
                    third[0] = second[0]
                    third[1] = second[1]
                    second[0] = rank[j][7]
                    second[1] = rank[j][0]
            else:
                third[0] = rank[j][7]
                third[1] = rank[j][0]

    return "\nBest students in the class are {}, {}, {} ".format(first[1], second[1], third[1])


print(findTopper(d, 'Maths'))
print(findTopper(d, 'Biology'))
print(findTopper(d, 'English'))
print(findTopper(d, 'Physics'))
print(findTopper(d, 'Chemistry'))
print(findTopper(d, 'Hindi'))
print(topThree(d))
