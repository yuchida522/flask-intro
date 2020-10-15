"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS = ['annoying', 'mean', 'stupid']


@app.route('/')
def start_here():
    """Home page."""
    
    return f"""
    <!doctype html>
    <html>
    <body>
      Hi! This is the home page.
      <a href='/hello'>Go to Hello Page.</a>
    </body>
    </html>
    """

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <p>What's your name? <input type="text" name="person"></p>
          
          <div>
            <label for="compliment">How are you feeling today?</label>
            <select name="compliment">
              <option value={AWESOMENESS[0]}>{AWESOMENESS[0]}</option>
              <option value="terrific">Terrific</option>
              <option value="fantastic">Fantastic</option>
              <option value="neato">Neato</option>
              <option value="fantabulous">Fantabulous</option>
              <option value="wowza">Wowza</option>
              <option value="oh-so-not-meh">Oh-so-not-meh</option>
              <option value="brilliant">Brilliant</option>
              <option value="ducky">Ducky</option>
              <option value="coolio">Coolio</option>
              <option value="incredible">Incredible</option>
              <option value="wonderful">Wonderful</option>
              <option value="smashing">Smashing</option>
              <option value="lovely">Lovely</option>
          </div>

          <input type="submit" value="Submit">
        </form>

        <form action="/diss">
          <p>What's your name? <input type="text" name="person"></p>
          <div>
              <label for="diss">Do you want to be dissed?</label>
              <select name="diss">
                <option value="annoying">{DISS[0]}</option>
                <option value="mean">{DISS[1]}</option>
                <option value="stupid">{DISS[2]}</option>
          </div>

          <input type="submit" value="Submit">
        </form>      
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
  """"""
  player = request.args.get("person")

  diss = request.args.get("diss")

  return f"""
  <!doctype html>
  <html>
    <head>
      <title>A Diss</title>
    </head>
    <body>
      Hi, {player}! I think you're {diss}!
    </body>
  </html>
  """
  

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
