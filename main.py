import csv
import smtplib
import schedule
import time
dic = {}
with open('D:/dataBase.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for i in csvreader:
        if int(i[4]) > 0:
            dic[i[0]] = i[1],i[4]
myMail = '' # add your mail here
myPassWord = ''  # add your password here

def sendMail():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=myMail, password=myPassWord)
        for students in dic:
            connection.sendmail(from_addr = myMail, to_addrs = dic[students][0], msg =(
                f'Subject : Fee remainder\n\nDear {students},\n'
                f'This is to remind you, the remaining fee of rupees {dic[students][1]} is due immediately.\n'
                f' \n'
                f'Make sure it is paid as soon as possible. \n'
                f'\n'
                f'If already paid, just disregard this email.\n'
                f'\n'
                f'Thank You!\n'
                f'\n'
                f'--\n'
                f'With Regards,\n'
                f'Dr.J.Max,\n'
                f'B.E., M.Tech.\n'
                f'Dean - E & T,\n'
                f'XYZ Institute,\n'
                f'abc - 12345 '))

schedule.every().day.at("18:55").do(sendMail)
while True:
    schedule.run_pending()
    time.sleep(1)

