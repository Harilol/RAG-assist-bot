import re

text = """
P y t h o n , A P I
F a s t A P I
L a n g C h a i n
"""

cleaned = re.sub(r'(?<=\b\w) (?=\w\b)', '', text)

print(cleaned)