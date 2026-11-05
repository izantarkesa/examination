def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    result = "PASS" if percentage >= 40 else "FAIL"

    print("Total:", total)
    print("Percentage:", percentage)
    print("Result:", result)

calculate_result([80, 70, 60, 90, 85])


