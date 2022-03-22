# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# ---- Members ----
# -- Samantha Roberts --
# -- Yoofi Williams --


# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import verify_capital


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():   
    return render_template('index.html')
    
@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == "GET":
        return "Please complete the quiz!!"
    else:
        form_ans = {"WA": request.form['Washington DC'],
                    "TX": request.form['Texas'],
                    "AK": request.form['Alaska'],
                    "CA": request.form['California'],
                    "OR": request.form['Oregon'],
                    }
        for state in form_ans:
            if form_ans[state] == '':
                return "Please complete the quiz!!"
        
        final_result, score = verify_capital(form_ans)
    return render_template('result.html', results=final_result, ans=form_ans, score=score)

if __name__=="__main__":
    app.run()


# TODO: create a results.html file to be rendered in app.py
# TODO: find out the states in the quiz
# TODO: create a dictionary with state as key and answers as values
# TODO: return a dictionary with the states as keys and correct / wrong as values
# TODO: so if correct, css in result.html background is green else red
# TODO: add a score display at bottom.