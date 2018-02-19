import random

print "Let's play Mad Libs!"
print "Enter in a word for each sentence. We will create your story"

random_city = raw_input('Random city:')
your_name = raw_input('Your name:')
pet_name = raw_input('Pet name:')
friend_name = raw_input('Friend Name:')
adjective = raw_input('Adjective:')

print "In the sunny city of " + random_city + "there on the bench sat" + " " + your_name + "alongside her dog called" +" "+ pet_name +" " + " and she was on the phone talking to her best friend" + " "+ friend_name + " " + "it was" + " " + adjective
