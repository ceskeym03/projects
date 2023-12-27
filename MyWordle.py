import nltk
import random
nltk.download('words')
word_list = nltk.corpus.words.words()
fivel_words = []

for i in range(len(word_list)):
    if len(word_list[i])==5:
        fivel_words.append(word_list[i])
        



def clue(word,answer):
     word_layout=['X','X','X','X','X']
     
     for j in range(len(word)):
          if word[j] == answer[j]:
               word_layout[j] =  word[j].upper()
          
          else:
               word_layout[j] = word[j]
     
     return word_layout


def game():
    wordle = []
    
    
    for i in range(len(fivel_words)):
        if fivel_words[i][0].islower():
            wordle.append(fivel_words[i]) 
            
    r = random.randint(0,len(wordle))
    correct=wordle[r]
    
    for x in range(1,7):
        prompt = input("Word?")
        common = list(set(prompt) & set(correct))
        print(clue(prompt,correct),common)
        if prompt == correct:
             print("Congratulations the word was:", correct)
             break
    
    if prompt != correct:
     print("Unlucky, the word was",correct)