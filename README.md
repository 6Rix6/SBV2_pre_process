# SBV2用動画前処理pythonスクリプト
style-bert-vits2で学習するために動画を発話単位の音声ファイルに分割するためのスクリプトです

> [!CAUTION]
> **必ずLinux(Wsl)上のvenv仮想環境で実行してください**

## 初期設定
1. pythonとpython-venvのインストール
```
sudo apt update
sudo apt install python3 python3-venv
```

2. venv環境を構築
```
python3 -m venv .venv
```
3. venv環境に入る
```
source .venv/bin/activate
```
4. 必要なディレクトリを作成
```
mkdir inputs outputs
```
5. 必要なパッケージをインストール
```
sudo apt install ffmpeg
pip install pydub numpy moviepy yt_dlp
```

## 使い方
1. yt-dl.pyでyoutube動画をダウンロード
2. VideoToAudio.pyで動画をwavファイルに変換
3. SplitAudio.pyで無音区間で動画を分割
