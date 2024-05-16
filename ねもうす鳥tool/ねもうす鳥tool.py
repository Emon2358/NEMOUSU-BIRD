import requests
import time

# 自分のアクセストークンを設定
DISCORD_TOKEN = ''
CHANNEL_ID = ''

# 定型の応答メッセージ
RESPONSE_MESSAGE = "ぴょぉぉぉぉぉぉぉぉぉぉぉぉぉぉぉぉぉぉぉ！！"

# Discord APIのエンドポイント
DISCORD_API_URL = 'https://discord.com/api/v9'

# メッセージを送信する関数
def send_message(channel_id, content):
    url = f"{DISCORD_API_URL}/channels/{channel_id}/messages"
    headers = {
        'Authorization': DISCORD_TOKEN,  # プレフィックスなし
        'Content-Type': 'application/json'
    }
    payload = {
        'content': content
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}")

# メインループ
while True:
    send_message(CHANNEL_ID, RESPONSE_MESSAGE)
    time.sleep(3600)  # 3600秒（1時間）ごとにメッセージを送信