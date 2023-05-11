# Instagram Word Cloud App BackEnd API

## 環境構築方法(初期 setup)

<br>

### 1. プロジェクトを Clone

```
git clone git@github.com:yukimura-manase/InstaWordCloud-backend-api.git
```

### 2. docker-compose で Dockerfile から image をビルドする

プロジェクトルートに移動します。

```
cd InstaWordCloud-backend-api
```

続いて、Dockerfile から Docker Image を作成します。  
docker-compose build コマンドは、Dockerfile から image を作成してくれるコマンドです。

```
docker-compose build
```

このコマンドを実行すると、Dockerfile に従って各サービスの Docker イメージがビルドされ、
<br/>
イメージ名とタグ名が作成されます。

### 3. Docker Image の ビルドを確認する

docker image ls で、build された image を確認しておきます。

```
docker image ls
# [ 出力結果 ]
REPOSITORY                         TAG       IMAGE ID       CREATED          SIZE
flask-api-backend-app              latest    5f1597c166e0   50 seconds ago   135MB
```

### 4. docker-compose で Docker コンテナを実行する

次のコマンドで、Docker Compose ファイルに定義されたサービスをバックグラウンドで起動できます。

```
docker-compose up -d
```

### 5. docker-compose で コンテナの起動状況を確認する

Docker コンテナの起動状況は、`docker container ps` コマンドで確認できます。

```
docker container ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED         STATUS         PORTS                    NAMES
e2c5d0c63478   flask-api-backend-app              "flask run --host=0.…"   7 seconds ago   Up 6 seconds   0.0.0.0:5001->5000/tcp   flask_api
```

### 6. Web ブラウザからアクセスする

http://localhost:5001/api/ にアクセスして、BackEnd-API の起動を確認します。

### 7. Docker コンテナの停止 & 削除

docker-compose down コマンドを使用して、すべてのコンテナを停止し、削除することができます。

```
docker-compose down
```

---

## 【 関連記事・学習用の記事 】

<br>

### 1. Docker で Python・Flask 環境を構築する方法

[Docker で Python・Flask 環境を構築する方法(ハンズオン講座)](https://masanyon.com/docker-python-flask-env-dockerfile-dockercompose/)

### 2. Docker コンテナの中に入って標準出力を実行する方法: Log 確認\_Develop_Debug_Skill

[Docker コンテナの中に入って標準出力を実行する方法・確認する方法](https://masanyon.com/docker-container-exec-it-logs-inside/)
