content = input("오늘의 일기를 작성하세요: ")

# 'w'는 쓰기 모드, 'a'는 추가 모드
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("diary.txt 파일에 저장되었습니다.")