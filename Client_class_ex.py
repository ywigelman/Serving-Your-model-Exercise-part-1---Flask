import requests

LOCAL = 'http://127.0.0.1:5000/'
QUESTIONING = LOCAL + 'mice_question?mice='
ANSWERING = LOCAL + 'mice_answer?mice='


def mice_talk():
    print(requests.get(QUESTIONING + 'pinky').text)
    print(requests.get(ANSWERING + 'brain').text)


def main():
    mice_talk()


if __name__ == '__main__':
    main()