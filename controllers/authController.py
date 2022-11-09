# !/usr/bin/python
# coding=utf-8

import re
from flask import render_template, redirect, request,Blueprint, make_response,current_app


auth=Blueprint('auth',__name__)


@auth.route('/thukhoaly')
def zxc():
    return render_template('/index1.html')

@auth.route('/thukhoaly/heart')
def zxc1():
    return render_template('/index2.html')
