import re
import unicodedata

upass = "愛知県１００１"
pattern = re.compile("[０-９][\u3041-\u309f][\u30A1-\u30FF][\uFF66-\uFF9F]+")
print(pattern.fullmatch("１２３４５"))

letter_cnt = 0
for c in upass:
    bigLetter = unicodedata.east_asian_width(c)
    if "F" == bigLetter or "W" == bigLetter:
        letter_cnt += 1

print(letter_cnt)
