from flask import Flask, request

app = Flask(__name__)

BRAIN = 'brain'
PINKY = 'pinky'
OTHER = 'other'
QUESTION = 'question'
RESPONSE = 'response'


MICE_DICT = {QUESTION: {BRAIN: 'Pinky, are you pondering what I\'m pondering?',
                        PINKY: 'Gee Brain, what are we gonna do tonight?',
                        OTHER: '...I don\'t what other mice say...'},
             RESPONSE: {BRAIN: 'The same thing we do every night, Pinky. Try to take over the world',
                        PINKY: 'Uh, I think so, Brain, but where will we find a duck and a hose at this hour?',
                        OTHER: '...cheese please?...'}}


@app.route('/mice_question')
def mice_question():
    mice = request.args.get('mice')
    return MICE_DICT[QUESTION][mice]


@app.route('/mice_answer')
def mice_answer():
    mice = request.args.get('mice')
    return MICE_DICT[RESPONSE][mice]


def main():
    app.run()


if __name__ == '__main__':
    main()
