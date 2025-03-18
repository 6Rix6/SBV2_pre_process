# SBV2 用動画前処理スクリプト

このスクリプトは、Style-Bert-VITS2（SBV2）で学習するために、動画を発話単位の音声ファイルに分割するためのものです。YouTube の動画をダウンロードし、音声を抽出し、無音部分で分割するプロセスを自動化します。

## 機能
- `yt-dlp` を使用して YouTube の動画をダウンロード
- 音声を WAV ファイルとして抽出
- 無音区間で音声を分割
- 一時ファイルを自動的に削除

## 必要な環境

> **推奨:** venv 仮想環境での実行

このスクリプトは `python`、`python-venv` を使用します。また、`ffmpeg` のインストールが必要です。

### FFmpeg のインストール方法
- **Windows**: [公式サイト](https://ffmpeg.org/download.html) からダウンロードし、システム PATH に追加
- **Mac (Homebrew)**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`（Debian系）または `sudo yum install ffmpeg`（RHEL系）

## 使い方 (Linux)
### 1. リポジトリをクローン
```sh
git clone https://github.com/6Rix6/SBV2_pre_process.git
cd SBV2_pre_process
```

### 2. 仮想環境を作成
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 依存関係のインストール
```sh
pip install pydub numpy moviepy yt_dlp
```

### 4. ディレクトリの作成
```sh
mkdir inputs outputs
```

### 5. スクリプトを実行
```sh
python3 SBV2_Pre_Process.py
```

## スクリプトの動作
1. プロンプトで YouTube の動画 URL を入力
2. 音声の出力名（モデル名）を入力
3. スクリプトが以下の処理を実行:
   - 動画をダウンロード
   - 音声を WAV ファイルとして抽出
   - 無音部分で音声を分割
   - `outputs/{model_name}/raw/` に保存
4. 処理完了後、一時ファイルを自動削除

### 既存のファイルを使用する場合
- `VideoToAudio.py`：動画から音声を抽出
- `SplitAudio.py`：抽出した音声を分割

## 出力フォルダ構成
スクリプトを実行すると、以下のフォルダに処理済みファイルが保存されます。

```
outputs/
  ├── {model_name}/raw/
      ├── {model_name}_chunk_1.wav
      ├── {model_name}_chunk_2.wav
      ├── ...
```

処理済みファイルは `sbv2/Style-Bert-VITS2/Data/` に移動してください。

## 参考
このスクリプトは以下のサイトを参考に作成しました。  
[推しに話してもらおうの会【SBV2を利用した音声生成について】](https://tonevoadventcalendar.hatenablog.com/entry/2024/12/24/154640)

---

# SBV2 Video Preprocessing Script

This script is designed to split videos into speech unit audio files for training Style-Bert-VITS2 (SBV2). It automates the process of downloading YouTube videos, extracting audio, and splitting it based on silent sections.

## Features
- Uses `yt-dlp` to download YouTube videos
- Extracts audio as WAV files
- Splits audio based on silent sections
- Automatically deletes temporary files

## Required Environment

> **Recommendation:** Run in a venv virtual environment

This script uses `python` and `python-venv`. Additionally, `ffmpeg` is required.

### Installing FFmpeg
- **Windows**: Download from the [official site](https://ffmpeg.org/download.html) and add it to the system PATH
- **Mac (Homebrew)**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg` (Debian-based) or `sudo yum install ffmpeg` (RHEL-based)

## Usage (Linux)
### 1. Clone the repository
```sh
git clone https://github.com/6Rix6/SBV2_pre_process.git
cd SBV2_pre_process
```

### 2. Create a virtual environment
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```sh
pip install pydub numpy moviepy yt_dlp
```

### 4. Create directories
```sh
mkdir inputs outputs
```

### 5. Run the script
```sh
python3 SBV2_Pre_Process.py
```

## Script Workflow
1. Enter the YouTube video URL when prompted
2. Enter the output name (model name)
3. The script performs the following steps:
   - Downloads the video
   - Extracts audio as a WAV file
   - Splits the audio based on silent sections
   - Saves the output in `outputs/{model_name}/raw/`
4. Temporary files are automatically deleted after processing

### Using Existing Files
- `VideoToAudio.py`: Extracts audio from videos
- `SplitAudio.py`: Splits extracted audio

## Output Folder Structure
After running the script, processed files will be stored in the following structure:

```
outputs/
  ├── {model_name}/raw/
      ├── {model_name}_chunk_1.wav
      ├── {model_name}_chunk_2.wav
      ├── ...
```

Move the processed files to `sbv2/Style-Bert-VITS2/Data/`.

## References
This script was created based on the following resource:  
[推しに話してもらおうの会【SBV2を利用した音声生成について】](https://tonevoadventcalendar.hatenablog.com/entry/2024/12/24/154640)

