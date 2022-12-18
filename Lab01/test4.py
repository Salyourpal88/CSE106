class Havel:
    def __init__(self, title, num, name, credits, days, start, end, percentage):
        self.title = title
        self.num = num
        self.name = name
        self.credits = credits
        self.days = days 
        self.start = start
        self.end = end 
        self.percentage = percentage

file = open("classesInput.txt","r")
paragraphs = int(file.readline())
courses = []
for x in range(paragraphs):
    item1 = file.readline().strip()
    item2 = file.readline().strip()
    item3 = file.readline().strip()
    item4 = file.readline().strip()
    item5 = file.readline().strip()
    item6 = file.readline().strip()
    item7 = file.readline().strip()
    item8 = file.readline().strip()
    obj = Havel(item1, item2, item3, item4, item5, item6, item7, item8)
    courses.append(obj)

for i in range(paragraphs):
    print("COURSE " + str(i + 1) + ": " + (courses[i].title) + (courses[i].num) + ": " + (courses[i].name))
    print("Number of Credits: " + courses[i].credits)
    print("Days of Lecture: " + courses[i].days)
    print("Lecture Time: " + courses[i].start + " - " + courses[i].end)
    print("Stat: on average, students get " + courses[i].percentage + "% in this course \n")
file.close()