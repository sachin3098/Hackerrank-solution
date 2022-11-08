Problem Link:

https://www.hackerrank.com/challenges/re-group-groups/problem

import re
reg = re.match(r".*?([a-zA-Z0-9]+)\1", input())
if reg:
    print(reg.group(1))
else:
    print(-1)