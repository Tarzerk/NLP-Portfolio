EldenBot

EldenBot is a knowledge bot to help users in the game of Elden Ring. Here are some of the things EldenBot can help you with. 

If you haven't played the game you can find information here 
{https://docs.eldenring.fanapis.com/docs#!} and 
{https://eldenring.wiki.fextralife.com/Elden+Ring+Wiki}

Remember to run:
Also remember to give the path to your API JSON Key in the eldenbot.py (Ex: "./key.json")
You must run both: controller.py & eldenbot.py


Before the game starts the game will ask your for your name
If it is in the database it will log you in. Otherwise, it will ask you for your
game level and class. 
I recommend selecting a level under [1-120] to be able to use all features. 
We are also using NLTK to parse the user's name but it doesn't do good with parsing all names therefore we recommend picking a common American name if it doesn't work. 

You don't have to ask the questions word for word for EldenBot to recognize the question type but you can experiment. 

Make sure to ask enough questions as if there is enough input
EldenBot will display the TF-IDF from the user's conversation


Ask about an boss
- Who is Malenia?
- Tell me about Mohg?

Build Help (Based on user's build)
- How should improve my build?
- How can I do more damage?


Ask about classes
- What is the Astrologer class?
- Hero

Compare classes
- What is the difference between the Astrologer class and the Hero class?
- What is better the Samurai or Vagabond class?

Recommendations (Based on user's level)
- What should I do next?
- What should I do at this moment?

Stat help
- What stats should I upgrade?
- What stats should I focus on?

Change level (Changes user's level)
- I want to change my level to 99

Weapon recommendation (Based on user's build)
- What is the best weapon for me?

Item help
- What is Blue Cipher Ring?
- What is Bloody Finger?

Small Talk
- How are you?
- What is your name?
- You are annoying


