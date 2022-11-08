Problem Link:

https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import re
for _ in range(int(input())):
    print(bool(re.match('^[-+]?[0-9]*\.[0-9]+$', input())))