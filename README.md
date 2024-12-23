# asteroids-game
Game project to practise Python with OOP


If you're not sure if you have python3 installed, follow first steps of this [README.md](https://github.com/albertoroldanq/bookbot) 

Once you've confirmed python is installed, you can clone this repository and follow the instructions below.  

## Installation
Create a virtual environment at the top level of your project directory:

```
python3 -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```
You should see (venv) at the beginning of your terminal prompt, for example, mine is:

(venv) alberto@MacBook-Pro asteroids-game %

Note: make sure that your virtual environment is activated when running the game

Install the required packages:
- This will install the pygame module into the virtual environment you created.

```
pip install -r requirements.txt
```

Make sure pygame is installed:
```commandline
python3 -m pygame
```

## Running the game
Once you have installed the required packages, you can run the game by running the following command:
```commandline
python3 main.py
```

And you should see the game window pop up - **The game window will quit automatically as soon as an asteroid collides with the ship.**
