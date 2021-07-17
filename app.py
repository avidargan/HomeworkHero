from flask import Flask, jsonify
from flask_cors import CORS
import random
import itertools


# global
hp = 100
gold =0

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



#firstNum = [1,2,3,4,5,6,7,8,9,10,11,12]
#secondNum = [1,2,3,4,5,6,7,8,9,10,11,12]

#pairs = list(itertools.product(firstNum,secondNum))
#random.shuffle(pairs)

#for x,y in pairs:
    #print(f'{x} x {y} = ')

#QUESTION: 3 + 2
#CORRECT ANSWER: 5
#INCORRECT ANSWER: 4, 3, 6

def subtract():
    num1 = random.randint(2, 100)
    num2 = random.randint(1, num1 - 1)
    question = str(num1) + " - " + str(num2)
    correctAnswer = num1 - num2
    incorrectAnswer1 = correctAnswer - 1
    incorrectAnswer2 = correctAnswer + 1
    if incorrectAnswer1 != 0:
        incorrectAnswer3 = incorrectAnswer1 - 1
    else:
        incorrectAnswer3 = incorrectAnswer2 + 1
    newDict = {
        "question": question, 
        "correctAnswer": correctAnswer,
        "incorrectAnswer": [incorrectAnswer1, incorrectAnswer2, incorrectAnswer3],
    }
    return newDict

def addition():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = str(num1) + " + " + str(num2)
    correctAnswer = num1 + num2
    incorrectAnswer1 = correctAnswer - 1
    incorrectAnswer2 = correctAnswer + 1
    incorrectAnswer3 = correctAnswer + 3
    newDict = {
        "question": question, 
        "correctAnswer": correctAnswer,
        "incorrectAnswer": [incorrectAnswer1, incorrectAnswer2, incorrectAnswer3],
    }
    return newDict

def multiplication():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/battle/<is_correct>', methods=['GET', 'POST'])
def battle(is_correct):
    try:
        is_correct = int(is_correct)
        # What to do on first call???

        global hp, gold
        if not is_correct:
            hp -= 10
        else:
            gold += 1
    except:
        pass

    questiontype = random.randint(1, 4)
    if questiontype == 1:
        dictionary  = addition()
    elif questiontype == 2:
        dictionary = subtractation()
    elif questiontype == 3:
        dictionary = multiplication()
    else:
        dictionary = division()

    return {
        'hp': hp, 
        'gold': gold,
        'question': dictionary
        }



if __name__ == '__main__':
    app.run()
