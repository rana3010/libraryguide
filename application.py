import os

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("postgres://sqrnjpvrexcfat:35430cad4ba40571270335938b1737575f6b1469a1fb8bca3c9aa2736de39114@ec2-23-21-148-223.compute-1.amazonaws.com:5432/d6qcdnha05od0a"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://sqrnjpvrexcfat:35430cad4ba40571270335938b1737575f6b1469a1fb8bca3c9aa2736de39114@ec2-23-21-148-223.compute-1.amazonaws.com:5432/d6qcdnha05od0a")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")
hhhhhiiiii
