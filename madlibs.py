"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Display madlib form."""

    user_choice = request.args.get("game")

    if user_choice == 'no':
        return render_template('goodbye.html')
    else:
        return render_template('game.html')


@app.route('/madlib')
def show_madlib():
    """Display madlib generated from user input."""

    user_color = request.args.get("color")
    user_noun = request.args.get("noun")
    user_person = request.args.get("person")
    user_adjective = request.args.get("adjective")
    user_animals = request.args.getlist("fav_animals")

    # user_animals = []

    # if 'cat' == 'on':
    #     user_animals.append('cat')
    # elif 'dog' == 'on':
    #     user_animals.append('dog')
    # elif 'dinosaur' == 'on':
    #     user_animals.append('dinosaur')
    # elif 'otter' == 'on':
    #     user_animals.append('otter')

    return render_template('madlib.html', color=user_color,
        noun=user_noun, person=user_person, adjective=user_adjective,
        animals=user_animals)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
