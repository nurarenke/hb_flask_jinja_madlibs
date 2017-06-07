"""A madlib game that compliments its users."""

from random import choice, sample

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

    return render_template("homepage.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


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

    if len(user_animals) > 1:
        last_two_animals = (user_animals[-2] + " and " + user_animals[-1])
        user_animals = ', '.join(user_animals[:-2]) + ", " + last_two_animals
    elif len(user_animals == 1):
        user_animals = user_animals[0]


    madlib_choices = ['madlib.html', 'madlib_two.html']


    return render_template(choice(madlib_choices), color=user_color,
        noun=user_noun, person=user_person, adjective=user_adjective,
        animals=user_animals)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
