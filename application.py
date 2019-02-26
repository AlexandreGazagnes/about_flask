#!/usr/bin/env python3
# coding: utf-8

# import
from datetime import datetime
from flask import Flask, render_template, request


# init
app = Flask(__name__)

# routes
@app.route("/")
def main():
    return "hello world, please go to the index page..."


@app.route("/alex")
def alex():
    return "hello alex"

@app.route("/alex/bonjour")
def alex_fr():
    return "bonjour alex"


@app.route("/alex/h1")
def alex_h1():
    return "<h1>bonjour alex</h1>"


@app.route("/<string:name>")
def hello(name):
    return f"hello {name.capitalize()}"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/var")
def var() :
    my_var = 3.1415
    return render_template("var.html", var=my_var)


@app.route('/bye')
def bye() :
    return render_template("var.html", var="bye!")


@app.route('/noel_python')
def noel_python() :
    d = datetime.now()
    noel = (d.month == 12) and (d.day == 25)
    if noel :   noel = "C'est NOEL"
    else :      noel = "C'est pas Noel :("
    return render_template("noel_python.html", var=noel)


@app.route('/noel_jinja')
def noel_jinja() :
    d = datetime.now()
    noel = (d.month == 12) and (d.day == 25)
    return render_template("noel_jinja.html", var=noel)


@app.route('/looper')
def looper() :
    people = ["Georges", "Heny", "Thomas", "Barack"]
    return render_template("looper.html", var=people)


@app.route('/link')
def link() :
    return render_template("link.html")


@app.route('/factor')
def factor() :
    return render_template("factor.html")


@app.route("/form")
def form() :
    return render_template("form.html")


# @app.route("/willkommen", methods=["POST"])
# def willkommen() :
#     name = request.form.get("name")
#     return render_template("willkommen.html", name=name)

@app.route("/form/willkommen", methods=["GET", "POST"])
def willkommen() :
    if request.method == "GET" :
        return "Error, please fill the form before"
    else :
        name = request.form.get("name")
    return render_template("willkommen.html", name=name)
