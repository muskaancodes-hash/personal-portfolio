from flask import Flask, render_template, request

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Contact Form
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("\n--- New Contact Message ---")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)
    print("--------------------------\n")

    return render_template(
        "index.html",
        success="Thank you! Your message has been received."
    )


if __name__ == "__main__":
    app.run(debug=True)