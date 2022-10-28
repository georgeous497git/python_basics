text = 'I know the programming language Python'
print(text)
print('Is Python in the previous text? = ' + str('Python' in text))
print('Is Java in the previous text? = ' + str('Java' in text))

if 'JavaScript' in text:
    print('JS is not in the text')


## lenght of string
word = " Platzi "
length = len(word)
print(f'The word "{word}" has a length of {length} characters including blank spaces')

wordUpper = word.upper()
print(f'Word {word} to upper case: {wordUpper}')
wordLower = word.lower()
print(f'Word {word} to lower case: {wordLower}')

print(f'Counting "z" at the word {wordLower}: ' + str(wordLower.count("z")))
print(f'Swaping word {word}: ' + word.swapcase())

print(f'Is the word {word} starting with "pl": ' + str(word.startswith("pl")))
print(f'Is the word {word} ending with "va": ' + str(word.startswith("zi")))
sentence = "Courses in Platzi!"
print(f'Replacing the word "Platzi" by "Udemy" at the sentence {sentence}: ' + sentence.replace("Platzi", "Udemy"))
sentenceLower = sentence.lower()
print(f'Capitalizing the sentence {sentenceLower}: ' + sentenceLower.capitalize())
print(f'As a Title the sentence {sentenceLower}: ' + sentenceLower.title())
textNumber = "35"
print(f'The text {textNumber} can be a digit?: ' + str(textNumber.isdigit()))