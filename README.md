# SBV2用動画前処理pythonスクリプト
style-bert-vits2で学習するために動画を発話単位の音声ファイルに分割するためのスクリプトです

> [!NOTE]
> **必ずLinux(Wsl)上での実行をお勧めします**　　
> Windows上での動作確認はしていません

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
### Youtubeから動画をダウンロードする場合
SBV2_Pre_Process.pyを実行
```
python3 SBV2_Pre_Process.py
```
youtubeのリンクと出力先のディレクトリ名が聞かれたら入力

### 既存のファイルを使用する場合
1. VideoToAudio.pyで動画をwavファイルに変換
```
python3 VideoToAudio.py
```
2. SplitAudio.pyで無音区間で動画を分割
```
python3 SplitAudio.py
```

## 参考
このスクリプトは以下のサイトを参考に作成しました。  
[推しに話してもらおうの会【SBV2を利用した音声生成について】](https://tonevoadventcalendar.hatenablog.com/entry/2024/12/24/154640)
