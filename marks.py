# 1. Create a list of at least five marks
marks = [65, 42, 78, 33, 90, 55, 48]

passed_count = 0

print("Student Results:")
print("----------------")

# 2. Loop through the marks and print Pass or Fail
# 3. Count how many students passed
for mark in marks:
    if mark >= 50:
        print(f"{mark} - Pass")
        passed_count += 1
    else:
        print(f"{mark} - Fail")

print("\nSummary:")
print(f"Total students: {len(marks)}")
print(f"Number of students passed: {passed_count}")
print(f"Number of students failed: {len(marks) - passed_count}")

# 4. Print the highest, lowest and average mark
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print(f"\nHighest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Average mark: {average:.2f}")