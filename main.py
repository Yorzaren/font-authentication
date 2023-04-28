from zh import ZH_ALL as chinese_simplified
from zh import HSK as HSK

print(chinese_simplified)
print(len(HSK))
print(len(chinese_simplified))
print("----------------")
print(ord("诗"))
print(ord("Z"))

str1 = "诗"

import codecs
print(codecs.raw_unicode_escape_encode(str1))

print(str1.encode("raw_unicode_escape"))
print(str1.encode("unicode_escape"))
