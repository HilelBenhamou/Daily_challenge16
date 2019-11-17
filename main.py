//DAILY CHALLENGE


first_name=input("What's your first nam ?")
last_name= input("What's your last name ?")
birth_year=int(input("what is the year you were born ?"))
actual_date=int(input("In what year are we ?"))
age= actual_date-birth_year
email=input("What's your email ?");
tel= input("What's your phone number ?")
job=input("What was your last job ? What did you learnd ?")

html_MyCv =f'''
<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
	<title>MY PYTHON CV</title>
</head>
<body>
	<h1>CV</h1>
	<ul>
		<li>Name: {first_name} {last_name}</li>
		<li>Age : {age}</li>
		<li>Email: {email}</li>
		<li>Tel: {tel}</li>
		<li>Last job: {job}</li>
	</ul>
</body>
</html>
'''
print(html_Mycv)