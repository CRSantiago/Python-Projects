#MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

#Comments are first attempt

def master_yoda(phrase):
  #spl_phrase = phrase.split()
  #spl_phrase.reverse()
  #yoda_talk = ' '.join(spl_phrase)
  #return yoda_talk
  return ' '.join(phrase.split()[::-1])
  
print(master_yoda('I am home'))
print(master_yoda('We are ready'))