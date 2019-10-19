from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
ages_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[22222,33333,44444,55555,66666,77777,88888,99999,22222,33333,44444]
plt.bar(ages_x,dev_y,color="#444444",label="All Devs")

plt.legend()

plt.title("Median Salary (USD) by Ages")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()
