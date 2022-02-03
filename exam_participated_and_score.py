import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("clean_data.csv")

data = data.replace(-1,None)
data["Average"] = data[['toán', 'ngữ văn', 'khxh', 'khtn', 'lịch sử', 'địa lí', 'gdcd', 'sinh học', 'vật lí', 'hóa học', 'tiếng anh']].mean(axis = 1)
data["Count"] = data[['toán', 'ngữ văn', 'khxh', 'khtn', 'lịch sử', 'địa lí', 'gdcd', 'sinh học', 'vật lí', 'hóa học', 'tiếng anh']].count(axis = 1)

average_score = data["Average"].tolist()
count_exam = data["Count"].tolist()

# plot the linear regression chart
def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "#2d73f5",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "#ff6358")

	# putting labels
	plt.xlabel('Number of exams participated')
	plt.ylabel('Average score')

	# function to show plot
	plt.show()

def main():
	# observations / data
	x = np.array(count_exam)
	y = np.array(average_score)

	# estimating coefficients
	b = estimate_coef(x, y)
	print("Estimated coefficients:\nb_0 = {:.2f} \
		\nb_1 = {:.2f}".format(b[0], b[1]))

	correlation_matrix = np.corrcoef(count_exam, average_score)
	correlation_xy = correlation_matrix[0,1]
	r_squared = correlation_xy**2

	print("R^2: " + str(round(r_squared, 2)))

	# plotting regression line
	plot_regression_line(x, y, b)

if __name__ == "__main__":
	main()