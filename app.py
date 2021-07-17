from flask import Flask, jsonify
from flask_cors import CORS
import random
import itertools


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
    num1 = random.randint(2, 12)
    num2 = random.randint(1, 12)
    question = str(num1) + " x " + str(num2)
    correctAnswer = num1 * num2
    incorrectAnswer1 = (num1 - 1) * num2
    incorrectAnswer2 = num1 * (num2 + 1)
    incorrectAnswer3 = (num1 + 1) * (num2 + 1)
    newDict = {
        "question": question, 
        "correctAnswer": correctAnswer,
        "incorrectAnswer": [incorrectAnswer1, incorrectAnswer2, incorrectAnswer3],
    }
    return newDict

def division():
    num1 = random.randint(2, 12)
    correctAnswer = random.randint(1, 12)
    num2 = num1 * correctAnswer
    question = str(num2) + " / " + str(num1)
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


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/battle', methods=['GET', 'POST'])
def battle():
    #for loop of 10 questions
    #randomised between addition, subtraction, multiplication, division
    #subtract
    num1 = [x for x in range(1, 100)]
    return jsonify(num1)



if __name__ == '__main__':
    app.run()
