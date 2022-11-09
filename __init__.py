# !/usr/bin/python
# coding=utf-8
from flask import Flask, config,jsonify,render_template

from controllers.authController import *


app=Flask(__name__)
app.register_blueprint(auth)


@app.route('/')
def index():
    return "Hello, I'm Hy đẹp trai"
    # return render_template('index2.html')

if __name__=='__main__':
    app.run(debug=True,port=8113)
