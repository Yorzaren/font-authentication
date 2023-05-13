# flake8: noqa

import font_generator.cjk as cjk
import font_generator.zh as zh

unq = []
for x in cjk.CJK_ALL:
    if x not in unq:
        unq.append(x)
    else:
        print(x)

# print(unq)
print("Done")
