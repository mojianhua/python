import datetime
today = datetime.date.today()
mouth = int(input("请问你是在哪月出生："))
day = int(input("请问你是几号出生："))
birthday = datetime.date(today.year,mouth,day)
print(birthday)
if birthday < today:
	birthday = datetime.date(today.year+1,mouth,day)
diff = birthday - today
if diff.days == 0:
	print("今天生日！")
else:
	print("还差" + str(diff.days) + "生日")