# SBV2用動画前処理pythonスクリプト
style-bert-vits2で学習するために動画を発話単位の音声ファイルに分割するためのスクリプトです

> [!CAUTION]
> **必ずLinux(Wsl)上のvenv仮想環境で実行してください**

## 使い方
1. yt-dl.pyでyoutube動画をダウンロード
2. VideoToAudio.pyで動画をwavファイルに変換
3. SplitAudio.pyで無音区間で動画を分割
