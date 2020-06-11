from flask import Flask, render_template, request, jsonify
import logging
import time
import os
import json

app = Flask(__name__)

handler = logging.FileHandler('error.log', encoding='UTF-8')
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

handler.setFormatter(logging_format)
app.logger.addHandler(handler)


# @app.errorhandler(404)
# def page_not_found(error):
#     app.logger.error(error)
#     return 'This page does not exist', 404


@app.errorhandler(500)
def special_exception_handler(error):
    app.logger.error(error)
    return '页面出错，请点击「系统总览」。依然出错，请联系管理员', 500


# def page_not_found(error):
#     return 'This page does not exist', 404
#
#
# app.error_handler_spec[None][404] = page_not_found


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/ad')
def ad():
    return render_template('ad.html')


@app.route('/setting')
def setting():
    return render_template('setting.html')


@app.route('/edit-vue')
def edit():
    return render_template('edit-vue.html')


@app.route('/test-vue')
def test():
    return render_template('test-vue.html')


@app.route('/addTest', methods=["POST"])
def add_test():
    content = request.json.get("content")
    run_date = request.json.get("run_date")
    run_time = request.json.get("run_time")
    account = request.json.get("account")
    recv_id = request.json.get("recv_id")

    print(content, run_date, run_time, account, recv_id)
    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(request.json, f, ensure_ascii=False)

    data = {
        "message": "发送成功",
        "message_type": "success"
    }

    return jsonify(data)


@app.route('/testData')
def test_data():
    data = {}
    try:
        with open('test.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        pass

    return jsonify(data)


@app.route('/testStatus', methods=["POST", "GET"])
def test_status():
    data = {}
    if request.method == 'GET':
        with open('testStatus.json', 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                pass
            return jsonify(data)
    elif request.method == 'POST':
        print(dict(request.form))
        with open('testStatus.json', 'w', encoding='utf-8') as f:
            json.dump(dict(request.form), f, ensure_ascii=False)
        return jsonify({})



if __name__ == '__main__':
    app.run()
