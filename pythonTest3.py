name = input('User enter your introduction')
print(name)
characterCount,wordCount = 0,1
print(characterCount,wordCount)
for character in name:
    characterCount += 1 
    if(character == ' '):
        wordCount+=1
print(str(wordCount) + ' number of words in the string')
print(str(characterCount) + 'number of character in name')