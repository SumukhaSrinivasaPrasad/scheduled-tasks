# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas as pd
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


LETTER_TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 1. Update the birthdays.csv
birth_data_df = pd.read_csv("birthdays.csv")

now = dt.datetime.now()

for index,row in birth_data_df.iterrows():
    letter_template = random.choice(LETTER_TEMPLATES)

    # 2. Check if today matches a birthday in the birthdays.csv

    if row.day == now.day and row.month == now.month:

        # 3. If step 2 is true, pick a random letter from letter templates and
        # replace the [NAME] with the person's actual name from birthdays.csv

        with open(f"./letter_templates/{letter_template}") as file:
            new_data = file.readlines()
            new_data[0] = new_data[0].replace("[NAME]", f"{row["name"]}")
            with open("sending_content.txt", mode="w") as to_send:
                to_send.writelines(new_data)

        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PWD)
            file = open("sending_content.txt")
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=row.email,
                msg=f"Subject: Happy Birthday\n\n{file.read()}")
            file.close()












