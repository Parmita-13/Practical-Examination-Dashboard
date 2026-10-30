import pandas as pd
import matplotlib.pyplot as plt

# Read Excel
df = pd.read_excel("C:/Users/user/Desktop/Excel files/practical exam dashboard i base.xlsx")

# Basic calculations
average = df["Marks"].mean()
highest = df["Marks"].max()
lowest = df["Marks"].min()

# Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 1. Subject-wise marks
ax[0, 0].bar(df["Practical subject"], df["Marks"])
ax[0, 0].set_title("Subject-wise Marks")
ax[0, 0].set_xlabel("Practical subject")
ax[0, 0].set_ylabel("Marks")
ax[0, 0].tick_params(axis="x", rotation=30)

# 2. Line graph
ax[0, 1].plot(df["Practical subject"], df["Marks"], marker="o")
ax[0, 1].set_title("Marks Trend")
ax[0, 1].set_xlabel("Practical subject")
ax[0, 1].set_ylabel("Marks")
ax[0, 1].tick_params(axis="x", rotation=30)

# 3. Pie chart
subject_marks = df.groupby("Practical subject")["Marks"].sum()

ax[1, 0].pie(
    subject_marks,
    autopct="%1.1f%%",
    startangle=90
)

ax[1, 0].legend(
    subject_marks.index,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.2),
    ncol=3,
    fontsize=8
)

ax[1, 0].set_title("Marks Distribution", pad=15)
# 4. Summary
ax[1, 1].axis("off")

summary = f"""
STUDENT PERFORMANCE

Average Marks: {average:.2f}
Highest Marks: {highest}
Lowest Marks: {lowest}
Total Subjects: {len(df)}
"""

ax[1, 1].text(
    0.1, 0.5,
    summary,
    fontsize=14,
    verticalalignment="center"
)

# Dashboard title
plt.suptitle("Practical Examination Performance Dashboard", fontsize=18)

plt.tight_layout()
plt.show()
