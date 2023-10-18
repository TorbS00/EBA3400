# Task A
# Import the data from credit_risk and assign the data type as described above
import os.path
import pandas as pd
import matplotlib.pyplot as plt

absolute_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
relative_path = "resources/credit_risk.csv"
full_path = os.path.join(absolute_path, relative_path)

df = pd.read_csv(full_path, dtype = {"default":object})
df.info()
print()


# Task B
# What is  the  average  age  of  customers?
# What  is  the  minimum  income  and  maximum income of these customers?

average_age = df["age"].mean()
min_income = df["income"].min()
max_income = df["income"].max()

print(f"The average age of customers are {average_age} years old.")
print(f"And the minimum income is ${min_income}K, maximum income is ${max_income}K.")
print()

# Task C
# Among  the  customers whose  income  is less  than 30k,
# how  many  customers have previously defaulted on debts?

df1 = df[(df.income < 30) & (df.default == "1")].shape[0]
print(f"Customers with less than $30K and previous defaulted is {df1}")

# Task D
# Use a scatter plot to show the relationship between income and
# credit card debt, and use the age value to color the points

df.plot(kind="scatter", x="income", y="creddebt", c="age", colormap="RdBu", sharex=False)
plt.show()

# Task E
# Calculate the debt-to-income ratio(DTI) and add it to the dataframe as a new column.
# Round the number to two decimal places. (Hint: DTI is total debt divided by income.)
df["DTI"] = round((df.creddebt + df.othdebt)/df.income, 2)
print(df["DTI"])

# Task F
# Use 15bins to draw a histogram of DTI.
df["DTI"].plot.hist(bins=15)
plt.show()

# Task G
# Convert age to age group according to the table below
df["age_group"] = pd.cut(df.age, bins=[20, 30, 40, 50, 60],
                         labels=["Group-A (20-30)", "Group-B (31-40)", "Group-C (41-50)",
                                 "Group-D (51-60)"], include_lowest=True)
print(df.head(10))

# Task H
# Draw a horizontal multiple bar chart to show the average
# credit card debt and average other debt of each age group.
df.groupby("age_group").mean().plot(kind="barh", y=["creddebt", "othdebt"])
plt.show()
