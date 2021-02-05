##########################################################################

# 사용방법
# 1. mail.txt 파일의 첫 줄은 제목, 나머지는 내용으로 채워주세요.
# 2. mail_list.csv 파일의 첫 줄은 보내는 사람(from), 나머지는 받는 사람(to) 입니다.
# 3. 로그인 인증시 https://yeolco.tistory.com/93 블로그를 참고하여 사용해 주세요!

##########################################################################
import smtplib
from email.mime.text import MIMEText
import csv

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
s.starttls()

########## 로그인 인증##########

s.login('', '')

###############################

# 메일 작성
print("메일 내용 : \n")
f = open("./mail.txt", 'r',encoding='UTF8')
message = ''
count = 0
while True:
    line = f.readline()
    if not line: break
    print(line)
    if count == 0:
        title = str(line)
        count += 1
    else:
        message += str(line)
f.close()


msg = MIMEText(message)
msg['Subject'] = title


# 메일 보내기
# 보내는 이메일 , 받는 이메일
print("받는사람 : \n")
count = 0
mail_list = []
f = open('./mail_list.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    if count == 0:
        mail_from = str(line)
        count += 1
    else:
        mail_list.append(line)
        print(line)
f.close()  

for to in range(len(mail_list)):
    s.sendmail(mail_from, mail_list[to], msg.as_string())

# 세션 종료
s.quit()


