words = ['сессия', 'сердце', 'ссуслик', 'обезьяна', 'расстройство', 'сосиска']

res = sum(word.count('с') == 3 for word in words)

print(res)