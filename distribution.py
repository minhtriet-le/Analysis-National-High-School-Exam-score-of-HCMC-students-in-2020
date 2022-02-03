import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("clean_data.csv")
data = data[~(data['toán'] == -1)]
math_score_list = data['toán'].tolist()

math_score_list_array = np.array(math_score_list)
math_median = np.percentile(math_score_list_array, 50)
math_percentile20 = np.percentile(math_score_list_array, 20)

print("Median = " + str(math_median))
print("20th Percentile = " + str(math_percentile20))

# Draw the histogram chart
plt.hist(math_score_list, bins=50, color = "#2d73f5")
plt.xticks(np.arange(0, 10.2, 0.2), rotation="vertical")

plt.axvline(math_median, color = "#ff6358", linewidth=2)
plt.axvline(math_percentile20, color = "#ffd246", linewidth=2)

plt.text(math_median + 0.1, 200, "Median = " + str(math_median), rotation=90, verticalalignment="bottom")
plt.text(math_percentile20 + 0.1, 200, "20th Percentile = " + str(math_percentile20), rotation=90, verticalalignment="bottom")

plt.title("The distribution of Math score")
plt.xlabel('Score')
plt.ylabel('Frequency')

plt.show()
