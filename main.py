text = input("Введіть текст: ")
reserved_words = input("Введіть список зарезервованих слів (через пробіл): ").split()

words = text.split()

for i in range(len(words)):
    if words[i].lower() in reserved_words:
        words[i] = words[i].upper()
result_text = ' '.join(words)

print(result_text)