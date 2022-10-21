# 日報管理ツール
## 主な機能
- ユーザー登録、認証機能（サインアップ、ログイン、ログアウト機能付き）
- 日報の新規作成、編集、削除
- ユーザー毎に日報を管理する（他ユーザの日報は参照できない）
- ユーザー名、メールアドレス、パスワードの変更
- 日報検索機能
- ページネーション機能（10件ごと）

## テストユーザー（確認用）
- user : test
- mail : 空白
- password : testuser2000 

## デプロイ
- Heroku : https://work-daily-report.herokuapp.com/

## フロント

### signup画面
![signup](https://user-images.githubusercontent.com/65697369/194267062-6cb36f2a-33c5-4b16-8b4a-a2a920247d06.png)


### login画面
![login](https://user-images.githubusercontent.com/65697369/194266840-e520516d-84b6-4a8a-ae1e-099ea2d19bc9.png)

### top画面
![image](https://user-images.githubusercontent.com/65697369/194268660-2d0075b9-4a24-4098-8fb8-0766b1fe1822.png)

### ユーザー専用画面
![image](https://user-images.githubusercontent.com/65697369/194269027-67ce7aec-10fc-4ec9-b0cb-6f966c0010d8.png)

## コード利用時の注意点
- セキュリティの観点からsettings.py内のSECRET_KEY環境変数の値をリポジトリ外（ローカルファイル）で管理しています。
- そのため、git cloneでコードを利用する際は、Djangoのshell上でget_random_secret_key()関数を実行し、セキュリティキーを取得して、その値をSECRET_KEYに設定してからアプリを利用してください。

## 今後の予定
- メールを用いた認証機能
- カレンダーを用いた日報作成日の入力機能（Heroku環境ではカレンダーが表示されない問題）
- 年月別に日報を管理する機能
- カレンダーを用いた年月の検索機能

# Lisence
This project is licensed under the MIT License, see the LICENSE file for details
