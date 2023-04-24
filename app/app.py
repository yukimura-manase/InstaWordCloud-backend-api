# Flask-APIを構築するための基本機能
from flask import Flask, Blueprint, render_template
# 「.env」で設定した環境変数を使用する
import settings
# ログ出力のために、loggerをimportする
from logoutput import logger

import traceback

# PythonからPythonScriptを呼び出すためのモジュール！ => プログラム内でコマンド実行！
# import subprocess

# Flask-Appを立ち上げる & templateのDirを指定する
app = Flask(__name__, template_folder='./templates')

# Generate Router Instance => Base_URLの設定はここ！
router = Blueprint('router', __name__ )

# ルート
@router.route('/')
def index():
    try :
        logger.debug('Flask-API-ルート起動！')
        return render_template('index.html')
    except Exception as error :
        error_msg:str = traceback.format_exc()
        logger.error(f"APIルート: Error:  {error_msg}")


# FrontAppの情報を確認するためのエンドポイント
@router.route('/front_info')
def front_info():
    logger.debug('FrontApp-Info-アクセス！')
    front_end_url = settings.FRONT_APP_URL
    msg = f"FrontAppのURLは: {front_end_url}"
    return msg


# Router を Flask-App に登録する
app.register_blueprint(
    router, 
    # 末尾に /api を追加する
    url_prefix='/api'
)