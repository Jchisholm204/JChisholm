#personal question bot
#Author: jChisholm204
#Date: 2021-05-13
import random
print('Welcome to personal question bot\n')
questions = ['whats your favorite color?', 'what do you do in your free time?', 'whats your current mood?']
responces = ['awesome', 'cool cool cool...', 'epic', '¯\_(ツ)_/¯ its wensday my dudes ¯\_(ツ)_/¯']
for question in questions:
  print(question+'\n')
  input().lower().split()
  print(random.choice(responces)+'\n')