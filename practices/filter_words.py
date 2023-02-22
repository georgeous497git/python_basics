print('Filtering words with length equals or greater than four')

def filter_by_length(words):
    return list(filter(lambda w: len(w) >= 4, words))


words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)