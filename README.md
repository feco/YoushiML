# YoushiML
Goal of the project
I made a game way back in high school about a boy, a mountain and some trees. The boy glide on his sledge and the player must avoid the trees by going to the left or the right.
About a year ago I caught an interest in machine learning and more specifically in Reinforcement Learning. So, I got the idea to make an AI for this game.

![Image of Yaktocat](https://raw.githubusercontent.com/feco/YoushiML/master/Youshi.png)

I settled on DQN, which seemed more than enough for the project. With some book and online tutorials, I made an agent to play the game with Keras and Tensorflow and so far, no results.
Then I discovered Google’s tf-agents. To my surprise, it worked. The QNetwork agent worked right away without even fiddling with parameters.

I tried to implement the tf-agents myself and nothing works. The agent always goes all the way to one side and wait to die.

For each implementation you can find the notebook with the implementation, a trained Keras network saved and a script to play with this saved network.

There is also a playable version for you to try: PlayableVersion.py
‘Q’ to go left and ‘D’ to go right

Tf-agents:
Notebook: YoushiTFAgent.ipynb
Saved network: myPolicyHard
Script to play: PlaySavedQnetHard.py

First try inspired from a book.
DQN with the same replay buffer and loss function as Tf-agents
Notebook: DQLBook.ipynb
Saved network: kerasDQL.h5
Script to play: PlayKerasModelHard.py
There is others version of this: 
- With a prioritized experience replay: DQLBookPER.ipynb
- With stacked frame: DQLBookStacked.ipynb / PlayKerasModelHardStacked.py

I found another tutorial on PyLessons website, so I tried with that: 
Notebook: PyLessons.ipynb
Saved network: models
Script to play: PlayPyLessons.py


With this, the TF-agents work perfectly well and play better than any human can do (at least those who tried the game^^)
And none of my own implementation works. 

Is there some kind of magic in TF-agents or am I missing something?

If I could get some insight it would be amazing as I have been working on this for months (a year maybe) without results.

