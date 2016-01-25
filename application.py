from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def shows_application_form():
    """Shows the application form"""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def acknowledges_application():
    """Prints a message acknowleding application"""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")

    print firstname, lastname, salary, position



    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            salary=salary,
                            position=position,
                           )

if __name__ == "__main__":
    app.run(debug=True)