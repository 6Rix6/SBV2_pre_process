import os
from moviepy import AudioFileClip


# フォルダのパス
input_folder = 'inputs'
output_folder = 'outputs'


# フォルダが存在しない場合、作成
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)


# inputsフォルダ内のすべての.mp4ファイルを処理
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace('.mp4', '.wav'))

        # 音声を抽出してWAV形式で保存
        print(f"{filename} を変換中...")
        audio_clip = AudioFileClip(input_path)
        audio_clip.write_audiofile(output_path, codec='pcm_s16le', logger='bar')
        print(f"{output_path} に保存されました。\n")

print("すべてのファイルの変換が完了しました。")