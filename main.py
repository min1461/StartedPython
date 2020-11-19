#variable(변수)
a_string = '파이썬은 쉽다'
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None

print(a_number)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print("Mon" in days)  #"Mon"이 days에 있는가 T/F
print(days[3])  #days의 3번째 값
print(len(days))  #days의 길이
days.append("Sun")
print(days)
days.reverse()
print(days)
