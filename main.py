import smtplib
import datetime as dt
import pandas as pd
import random

# Fill in your email and password
my_email = "mail@gmail.com"
passwords ="mail"

# Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Load birthday data
data = pd.read_csv("birthdays.csv")

# Create a dictionary from the DataFrame
birthdays_dict = {(row["month"], row["day"]): row for index, row in data.iterrows()}

# Check if today is someone's birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    
    # Choose a random letter template
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        
    # Replace placeholder with the actual name
    contents = contents.replace("[NAME]", birthday_person["name"])
    
    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, passwords)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )



#with smtplib.SMTP("smpt.gmail.com") as connection:
  #  connection = smtplib.SMTP("smtp.gmail.com")
   # connection.starttls() #securelıyor
    #connection.login(user=my_email , password=passwords)

    #connection.sendmail(from_addr=my_email , to_addrs="halilibrahimkocak000@gmail.com",msg="Subject:Hello\n\nThis is the body of my email.")
    #connection.close()
