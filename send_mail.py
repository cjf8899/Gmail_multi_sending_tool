##########################################################################

# 사용방법
# 1. mail.txt 파일의 첫 줄은 제목, 나머지는 내용으로 채워주세요.
# 2. mail_list.csv 파일의 첫 줄은 보내는 사람(from)과 보내는 사람 이메일, 나머지는 받는 사람(to)과 받는 사람 이메일 입니다.
# 3. 로그인 인증시 https://yeolco.tistory.com/93 블로그를 참고하여 사용해 주세요!
# 4. csv한글은 오른쪽 하단부 Spaces: 옆에 있는 버튼 클릭 후, Reopen with encoding 에서 korean 검색 후 설정
# 5. 그 후, save with encoding 에서 UTF-8으로 설정

##########################################################################
import smtplib
from email.mime.text import MIMEText
import csv

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
s.starttls()


########## 로그인 인증##########

s.login('nhchul99@gmail.com', 'dlurcpzwpiafzibo')

###############################


# txt 파일 읽어오기
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


# csv 파일 읽어오기
# 보내는 이메일 , 받는 사람, 받는 사람 이메일
print("받는사람 : \n")
mail_list = []
mail_name_list = []
nameplus = ''
f = open('./mail_list.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for count, (name, email) in enumerate(rdr):
    if count == 0:
        mail_from = str(email)
    else:
        mail_name_list.append(name)
        mail_list.append(email)
        print(" name : ",name)
        print(" email : ",email)


# 메일 보내기
for idx in range(len(mail_name_list)):
    nameplus = str(mail_name_list[idx]) + " 님, "+ message
    msg = MIMEText(nameplus)
    msg['Subject'] = title
    s.sendmail(mail_from, mail_list[idx], msg.as_string())

# 세션 종료
s.quit()


