text=input('Введіть текс: ')
num_sentences = text.count('.')+text.count('!')+text.count('?')
print(f'Кількість пропозицій у тексті: {num_sentences}')