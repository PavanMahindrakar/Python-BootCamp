marks = [10, 20, 30, 40, 50]
extra_marks = [60, 70, 80]

marks.append(5)
print(marks)  # Output: [10, 20, 30, 40, 50, 5]

marks.extend(extra_marks)
print(marks)  # Output: [10, 20, 30, 40, 50, 5, 60, 70, 80]

marks.insert(2, 25)
print(marks)  # Output: [10, 20, 25, 30, 40, 50, 5, 60, 70, 80]

marks.remove(5)
print(marks)  # Output: [10, 20, 25, 30, 40, 50, 60, 70, 80]

marks.pop(3)
print(marks)  # Output: [10, 20, 25, 40, 50, 60, 70, 80]

marks.sort()
print(marks)  # Output: [10, 20, 25, 40, 50, 60, 70, 80]

marks.reverse()
print(marks)  # Output: [80, 70, 60, 50, 40, 25, 20, 10]