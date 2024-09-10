print("Are you able to sit the exam?")
working_days = int(input("Enter your number of working days: "))
absent_days = int(input("Enter your number of absent days: "))

Exam_check =  ((working_days-absent_days)/working_days) * 100
print("Your Exam check percentage is", Exam_check,"%")

if Exam_check < 75:
    print("You CANNOT sit exams")

elif Exam_check >= 75:
    print("You CAN sit exams")

else:
    print("Invalid")
