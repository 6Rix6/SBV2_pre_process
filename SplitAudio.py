from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

input_folder = 'outputs'
output_folder = 'outputs'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.wav'):
        input_path = os.path.join(input_folder, filename)
        base_filename = os.path.splitext(filename)[0]

        try:
            audio = AudioSegment.from_wav(input_path)
            decibels = audio.dBFS

            # 無音区間での分割
            chunks = split_on_silence(
                audio,
                min_silence_len=1200,  # 無音と判定する最小の時間（ミリ秒）
                silence_thresh=decibels-30,  # 無音と判定するデシベル（オーディオのdBFSに基づく）
                keep_silence=250  # 分割後も無音を残す時間（ミリ秒）
            )

            # チャンクの数と内容を表示
            print(f"{filename} の分割結果: {len(chunks)} チャンクが作成されました。")

            voice_folder = os.path.join(output_folder, base_filename, "raw")
            os.makedirs(voice_folder, exist_ok=True)
            
            for i, chunk in enumerate(chunks):
                chunk_path = os.path.join(voice_folder, f"{base_filename}_chunk_{i+1}.wav")
                chunk.export(chunk_path, format="wav")
                print(f"{chunk_path} に保存しました。")

            # 変換後に元のファイルを削除
            os.remove(input_path)
            print(f"{input_path} を削除しました。\n")

        except Exception as e:
            print(f"エラーが発生しました: {e}")

print("無音区間での分割が完了しました。")
