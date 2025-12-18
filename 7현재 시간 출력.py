import datetime

now = datetime.datetime.now()

# 수정 전 (에러 발생):
# print(f"현재 시간: {now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')}")

# 수정 후 (해결 방법):
# 날짜/시간 숫자만 strftime으로 가져오고, 한글은 f-string으로 따로 붙입니다.
print(f"현재 시간: {now.strftime('%Y')}년 {now.strftime('%m')}월 {now.strftime('%d')}일 {now.strftime('%H')}시 {now.strftime('%M')}분 {now.strftime('%S')}초")