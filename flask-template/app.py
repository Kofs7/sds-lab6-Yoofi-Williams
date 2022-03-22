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
    
@app.route('/results', methods=["POST", "GET"])
def results():
    if request.method == "GET":
        return "Please complete the quiz!!"
    else:
        form_ans = {"WA": request.form['Washington'],
                    "TX": request.form['Texas'],
                    "DE": request.form['Delaware'],
                    "CA": request.form['California'],
                    "GA": request.form['Georgia'],
                    }
        for state in form_ans:
            if form_ans[state] == '':
                return "Please complete the quiz!!"
        
        final_result, score, answers = verify_capital(form_ans)
    return render_template('results.html', results=final_result, ans=form_ans, score=score, correct=answers)

if __name__=="__main__":
    app.run(debug=True)
