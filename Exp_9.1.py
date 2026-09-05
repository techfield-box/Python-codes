import matplotlib.pyplot as plt

roll_numbers = list(range(1, 11))
marks = [45, 78, 62, 89, 34, 90, 76, 85, 92, 58]

max_mark = max(marks)

# Line Graph
plt.figure(figsize=(8, 4))
plt.plot(roll_numbers, marks, marker='o', color='blue', label='Marks')
plt.title('Mathematics Marks Analysis (Line Graph)')
plt.xlabel('Roll Number')
plt.ylabel('Marks')
plt.grid(True)
plt.show()

# Bar Graph
plt.figure(figsize=(8, 4))
colors = ['red' if m == max_mark else 'blue' for m in marks]

plt.bar(roll_numbers, marks, color=colors)
plt.title('Mathematics Marks Analysis (Bar Graph)')
plt.xlabel('Roll Number')
plt.ylabel('Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()