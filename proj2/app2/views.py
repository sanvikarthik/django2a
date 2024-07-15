from django.shortcuts import render

def fruit_student(request):
    fruitList = ['Mango', 'Kiwi', 'Banana', 'Apple', 'Grapes']
    studentList = ['Rama', 'Chetan', 'Kumar', 'Harish', 'Geetha']
    return render(request, 'fruit_student.html', {'fruitList': fruitList, 'studentList': sorted(studentList)})
