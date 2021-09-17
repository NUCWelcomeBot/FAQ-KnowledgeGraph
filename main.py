import jiagu

from ExtractionKeywords import get_extraction_keywords
from flask import request

from flask import Flask

app = Flask(__name__)


@app.route('/getExtractionKeyword', methods=("GET", "POST"))
def getExtractionKey():
    info = request.form.to_dict()
    sentence = info['sentence']
    return {
        'code': 200,
        'msg': 'success',
        'data': get_extraction_keywords(sentence)
    }


if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
