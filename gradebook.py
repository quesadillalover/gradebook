lloyd = {'name': 'lloyd', 'homework':[90.0, 97.0, 75.0, 92.0] , 'quizzes': [88.0, 40.0, 94.0], 'test': [75.0, 90.0] }
alice = {'name': 'alice', 'homework':[80.0, 92.0, 65.0, 69.0] , 'quizzes': [89.0, 77.0, 98.0], 'test': [86.0, 80.0]}
tyler = {'name':'tyler', 'homework':[89.0, 46.0, 32.0, 91.0] , 'quizzes':[78.0, 88.0, 69.0], 'test':[78.0, 75.0]}

students= [lloyd, alice, tyler]

# for in students:
   # print(x)
    
def average(num):
    total = float(sum(num))
    avg= total/len(num)
    return avg

def get_average (students):
    homework = students['homework']
    quizzes = students['quizzes']
    tests = students ['test']
    avg= average(homework)*0.1 + average(quizzes)*0.3 + average(tests)*0.6
    return avg

def letter_grade(score):
    if score >= 90:
        return('A')
    elif score >=80:
        return('B')
    elif score >=70:
        return('C')
    elif score >=60:
        return('D')
    elif score <60:
        return('F')

def class_average(students):
    results= []
    for tea in students:
        results.append(get_average(tea))
    return average(results)

print('Student average is: ' + str(get_average(lloyd)))
print("Student letter grade is: " + str(letter_grade(get_average(lloyd))))
print('The class average is: ' + str(class_average(students)))
print('Class letter grade is: ' + str(letter_grade(class_average(students))))
    
    


    