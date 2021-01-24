"""
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
"""

string = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

str_list = [word for word in string if word not in 'aeiou']

result = "".join(str_list)
print(result)