text = "Jorge is a Java programmer"
print("String indexes")
print(f'Getting the position 3 of the text {text}: ' + text[3])
print(f'Getting the last position of the text {text}: ' + text[-1])

print("String Slicing")
print(f'Slicing sentence {text} from 0 to 10 index: ' + text[0:10])
print(f'Slicing sentence {text} from 0 to 10 index: ' + text[:10])

print(f'Slicing sentence {text} from 5 to the end of the index: ' + text[4:])
print(f'Slicing sentence {text} from 5 to the end of the index: ' + text[4:-1])

print(f'Slicing sentence {text} from 5 to 15 skipping 2 characters in between: ' + text[5:15:2])
print(f'Slicing sentence {text} from 0 to the end skipping 2 characters in between: ' + text[::2])