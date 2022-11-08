problem Link:

https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re

a = re.findall('[aeiouAEIOU]{2,}[^aeiouAEIOU]{1}', input())
if a:
        print(*[i[:-1] for i in a], sep = "\n")
else:
        print("-1")