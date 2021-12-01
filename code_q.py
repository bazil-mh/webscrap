# pylint: disable=C0103
# pylint: disable=C0114
# multi-line statement

# Pylint and regex demonstration.

import re

def regex_test(pat, string):
    x = re.search(pat, string)
    return x

txt = "dskh23312.32:hd8dfd8"

res = re.findall('[0-9.:]',txt)

res2 = ''
for x in res:
    res2+=x


print(res2)

