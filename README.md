conda activate livecoding



## GPT3-FoxDot

work in progress!


Requires a [key from OpenAI](https://beta.openai.com/).

1) Clone this repo 
'''
$ git clone git@github.com:genekogan/GPT3-FoxDot.git
$ cd GPT3-FoxDot
'''
2) Create an env/choose a package manager
*requires python=3.8
'''
$ conda create -n LiveFox python=3.8
$ conda activate LiveFox
$ pip install -r requirements.txt
'''

3) Install [FoxDot](https://github.com/Qirky/FoxDot) from source.

$ conda install setuptools
$ conda install wheel
$ pip install foxdot
$ git clone https://github.com/Qirky/FoxDot.git
$ cd FoxDot
$ python setup.py install
$ cd .. # goes back to ./GPT3-FoxDot
'''

    

4) Download [SuperCollider](https://supercollider.github.io/) or install it from source and then [add the FoxDot quark](https://foxdot.org/installation/) to it by running `Quarks.install("FoxDot")` and recompiling the class library.

5) In the root folder, create a file called `.env` which contains the following line:

    `OPENAI_KEY=xxxxxx`

where `xxxxxx` is replaced with your API key from OpenAI.

6) Boot SuperCollider server and start FoxDot by running:

    `FoxDot.start`

7) In a terminal, run 

    `python runfoxdot.py`

This will launch the FoxDot editor.

8) In a second terminal, run 

    `python main.py`

And then click your mouse cursor onto the FoxDot editor, and wait for the main script to begin generating keystrokes to run FoxDot commands.

