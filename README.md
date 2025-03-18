# SBV2用動画前処理pythonスクリプト
style-bert-vits2で学習するために動画を発話単位の音声ファイルに分割するためのスクリプトです

> [!CAUTION]
> **必ずLinux(Wsl)上のvenv仮想環境で実行してください**

## 初期設定
1. venv環境を構築
```
python3 -m venv .venv
```
2. venv環境に入る
```
source .venv/bin/activate
```
3. 必要なディレクトリを作成
```
mkdir inputs outputs
```
3. 必要なパッケージをインストール
```
pip install pydub numpy moviepy yt_dlp
sudo apt install ffmpeg
```

## 使い方
1. yt-dl.pyでyoutube動画をダウンロード
2. VideoToAudio.pyで動画をwavファイルに変換
3. SplitAudio.pyで無音区間で動画を分割
