Problem Link:

https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true

def person_lister(f):
    
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return [f(person) for person in people]
            
    return inner