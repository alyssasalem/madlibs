"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""


    return """Hi! This is the home page.
            <p> 
            <a href="http://localhost:5000/hello"> Play a game? </a> 
            </p>"""


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Get the user's response from form."""
    user_response = request.args.get("want-game")

    if user_response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route("/madlib")
def show_madlib():
    """Show user their madlib."""
    
    results = []
    results.append(request.args.get("person"))
    results.append(request.args.get("color"))
    results.append(request.args.get("noun"))
    results.append(request.args.get("adjective"))
    results.append(request.args.get("adverb"))
    results.append(request.args.get("past-tense-verb"))
    results.append(request.args.getlist("colors-list"))
    results.append(request.args.get("place"))
    result_6_len = len(results[6])

    return render_template("madlib.html", answers = results, colors_len = result_6_len)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
