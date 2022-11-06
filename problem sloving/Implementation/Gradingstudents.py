Problem Link:

https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

def gradingStudents(grades):
    # Write your code here
    result=[]
    for grade in grades:
        if grade>=38:
        #we take modulo to find remainder.
            mod5=grade%5    
             
            if mod5>=3:
                grade+=(5-mod5)
        result.append(grade)
    return result  