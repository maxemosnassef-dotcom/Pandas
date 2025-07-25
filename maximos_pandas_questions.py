
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Sample data
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']
departments = ['Sales', 'Marketing', 'HR', 'Tech']

# Create a DataFrame
df = pd.DataFrame({
    'Name': np.random.choice(names, size=20),
    'Age': np.random.randint(22, 60, size=20),
    'Department': np.random.choice(departments, size=20),
    'Salary': np.random.randint(40000, 120000, size=20),
    'YearsExperience': np.random.randint(0, 20, size=20)
})
df.head()

"""# 🧪 PRACTICE QUESTIONS BELOW


# 1️⃣ Use .loc to select all rows where the Department is 'Tech'.
#    - Describe what .loc does and why it's useful for label-based filtering.

"""

print(df.loc[df['Department']=="Tech"])

#used to access rows and columns by label

"""
# 2️⃣ Use .iloc to select the first 5 rows and the last two columns.
#    - What is the difference between .loc and .iloc?
"""

print(df.iloc[:5, -2:])

#used to access rows and columns by index

"""
# 3️⃣ Map a new column called 'DeptCode' where:
#     'Sales' -> 1, 'Marketing' -> 2, 'HR' -> 3, 'Tech' -> 4.
#    - Use .map and explain what happens if a value is not mapped.
"""

dept_map = {"Sales":1, "Marketing" : 2, "HR" : 3, "Tech":4}
df["DeptCode"] = df["Department"].map(dept_map)
print(df)

"""
# 4️⃣ Use .apply to calculate a new column 'Seniority' where:
#     - If YearsExperience > 10 → 'Senior'
#     - If between 5-10 → 'Mid-Level'
#     - Else → 'Junior'
#    - Use a lambda function with apply.
"""

df["Seniority"] = df["YearsExperience"].apply(lambda x : "Senior"if x > 10 else ("Mid-Level" if x >= 5 else "Junior"))
print(df)

"""
# 5️⃣ Overwrite all salaries for employees with < 3 years of experience to 35000.
#    - Use boolean indexing with .loc to do this.
"""

df.loc[df["YearsExperience"] < 3, "Salary"] = 35000
print(df)

"""
# 6️⃣ Compare using .loc and .iloc to select the same row:
#    - Select the 3rd row using .iloc
#    - Find its index value and use .loc to select the same row by label
"""

print(df.iloc[2])
print(df.loc[2])

"""
# 7️⃣ Check if there are any duplicate names in the dataset.
#    - If there are, show only those duplicated rows.
"""

print(df[df.duplicated(subset=["Name"])])

"""
# 8️⃣ Sort the DataFrame by Salary in descending order.
#    - Then sort it by Department and within Department by Age.
"""

print(df.sort_values(by=["Salary"], ascending=False))
print(df.sort_values(by=["Department", "Age"]))

"""
# 9️⃣ Slice the DataFrame to return rows 5 through 12 and columns 'Name', 'Salary'
#    - Try slicing using both label-based and position-based methods.
"""

print(df.loc[5:12, ["Name", "Salary"]])
print(df.iloc[5:12, [0, 3]])

"""
# 🔟 Find all rows where the name starts with 'A' or 'D'.
#    - Use string methods with .str accessor.
"""

print(df[df["Name"].str.startswith("A") | df["Name"].str.startswith("D")])

"""
# 1️⃣1️⃣ Drop all rows where Age is below 25.
#     - Explain whether this modifies the DataFrame in place or returns a copy.
"""

print(df.drop(df[df['Age'] < 25].index))

"""
# 1️⃣2️⃣ Use groupby to calculate the average salary per Department.
#     - Bonus: Show the average age and average experience too.
"""

print(df.groupby('Department')['Salary'].mean())

"""
# 1️⃣3️⃣ Use groupby to count how many employees are in each Department.
"""

print(df.groupby('Department')['Name'].count())

"""
# 1️⃣4️⃣ Use .apply to normalize the Salary column (min-max scaling between 0 and 1).
#     - Bonus: Write your own normalization function and pass it to apply.
"""

print(df["Salary"].apply(lambda x : (x - df["Salary"].min()) / (df["Salary"].max() - df["Salary"].min())))

"""
# 1️⃣5️⃣ Use boolean indexing to find all employees who:
#     - Are in 'HR' OR 'Tech', AND have > 5 years of experience.

# 🔁 For many of these tasks, try both .loc and .iloc to build intuition on their differences.

"""

print(df[(df['Department'].isin(['HR', 'Tech'])) & (df['YearsExperience'] > 5)])