# Router & Template_Render
from flask import  Blueprint, render_template
# 「.env」で設定した環境変数を使用する
import settings
# ログ出力のために、loggerをimportする
from logoutput import logger
import traceback
# Post受信をするためにFlask_requestをimportする
from flask import request, jsonify

# import requests
import csv
import json
import pprint

# PythonからPythonScriptを呼び出すためのモジュール！ => プログラム内でコマンド実行！
# import subprocess

# Generate Router Instance => Base_URLの設定はここ！
router = Blueprint('router', __name__ )


# ルート, Method: GET
@router.route('/', methods=['GET'])
def index():
    try :
        logger.debug('Flask-API-ルート起動！')
        return render_template('index.html')
    except Exception as error :
        error_msg:str = traceback.format_exc()
        logger.error(f"APIルート: Error:  {error_msg}")

# Robotama_エンドポイント, Method: GET
@router.route('/robotama', methods=['GET'])
def robotama():
  return 'Robotamaなのだ！！'

# FrontAppの情報を確認するためのエンドポイント, Method: GET
@router.route('/front_info', methods=['GET'])
def front_info():
    logger.debug('FrontApp-Info-アクセス！')
    front_end_url = settings.FRONT_APP_URL
    msg = f"FrontAppのURLは: {front_end_url}"
    return msg

# CSVの中身の情報、ColumnやRow_Dataを表示するためのエンドポイント, Method: POST
@router.route('/create_csv_info', methods=['POST'])
def create_csv_info():

    logger.debug('create_csv_info-アクセス！')
    pprint.pprint(request)
    # <Request 'http://localhost:5001/api/create_csv_info' [POST]>
    print('-------------------------------------')

    pprint.pprint(request.files)
    # ImmutableMultiDict([('file', <FileStorage: 'robotama.csv' ('text/csv')>)])
    print('-------------------------------------')

    pprint.pprint(request.files['file'])
    # <FileStorage: 'robotama.csv' ('text/csv')>
    print('-------------------------------------')

    file = request.files['file']
    pprint.pprint(csv.reader(file))
    # <_csv.reader object at 0xffff952222e0>
    print('-------------------------------------')

    # if file:
    #     # ファイルを読み込んで処理する
    #     reader = csv.reader(file)
    #     print('-------------------------------------')
    #     for row in reader:
    #         # データ処理
    #         pass

    responseData = {
        "robotama": 'ロボ玉',
        "hakutou": '白桃さん',
        "momo": 'ももちゃん',
    }
    return jsonify(responseData)


# FrontAppの情報を確認するためのエンドポイント, Method: GET
@router.route('/create_word_cloud', methods=['GET'])
def create_word_cloud():
    return 'create_word_cloud'


# @router.before_request
# def before_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response


# Requestの後処理
@router.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
