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

def verify_capital(answers: dict) -> dict:
    """
    Takes in a dictionary with states as keys and user's answers as values.
    
    Attributes:
        mark_scheme: dicitonary containing the correct answers of the quiz.
        score: user's total score after quiz.
        result: a dictionary containing the correct or wrong answers of the user on each question.
    """
    score = 0
    mark_scheme = {'CA': 'Sacramento', 'TX': 'Austin', 'WA': 'Olympia', 'AK': 'Juneau', 'OR': 'Salem'}
    result = {}

    for state in answers:
        if answers[state].lower().title() != mark_scheme[state]:
            result[state] = False
        else:
            result[state] = True
            score += 1
    final_score = (score / 5) * 100
    return result, final_score

