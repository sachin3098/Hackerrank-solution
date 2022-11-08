Problem Link:

https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
for i in range(int(input())):
    if re.match("^[789]\d{9}$",input()):
        print("YES")
    else:
        print("NO")
        