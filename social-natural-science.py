import pandas as pd
import matplotlib.pyplot as plt
import numpy

data = pd.read_csv("clean_data.csv")
subjects = ["social science", "natural science"]

# number of students registering social science
ss_count = data[data["khxh"]>=0]["khxh"].count()

# number of students registering natural science
ns_count = data[data["khtn"]>=0]["khtn"].count()

total_student = len(data)
take_exam = [ss_count, ns_count]
take_exam_percentage = [0,0]

take_exam_str = [0, 0]
take_exam_percentage_str = [0,0]

# convert to percentage
for i in range(0,2):
	take_exam_percentage[i] = round(take_exam[i]*100/total_student, 2)

# convert to string
for i in range(0,2):
	take_exam_percentage_str[i] = str(take_exam_percentage[i]) + "%"
for i in range(0,2):
	take_exam_str[i] = "{:,}".format(take_exam[i])

print(take_exam_str)
# plot barchart
figure, axis = plt.subplots()

# list from 0-1
y_pos = numpy.arange(len(subjects))

# plot the barchart using 2 list
plt.bar(y_pos, take_exam_percentage, color=["#ff6358","#2d73f5"])

# change horizontal category name
plt.xticks(y_pos, subjects)

# set limit to vertical axis
axis.set_ylim(0,100)

# label and title
plt.ylabel('Percentage')
plt.title('Number of students participating in the exam')

# Draw number of student on top of each bar
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
rects = axis.patches
for rect, label1, label2 in zip(rects, take_exam_str, take_exam_percentage_str):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label1, ha='center', va='bottom')
    axis.text(rect.get_x() + rect.get_width() / 2, height/2, label2, ha='center', va='center')

# show the plot
plt.show()