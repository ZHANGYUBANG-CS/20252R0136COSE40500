dictionary = {
    "apple": "사과",
    "banana": "바나나",
    "cat": "고양이",
    "dog": "개"
}

word = input("검색할 영어 단어를 입력하세요: ")
print(dictionary.get(word, "사전에 없는 단어입니다."))