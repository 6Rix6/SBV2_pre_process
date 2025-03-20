import os
import glob
from pydub import AudioSegment

def get_audio_length(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        return len(audio) / 1000  # ミリ秒を秒に変換
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return 0

def delete_specific_length_audio_files(directory, min_threshold_seconds=10, max_threshold_seconds=15):
    # 対象とする音声ファイルの拡張子
    audio_extensions = ('*.mp3', '*.wav')

    # 各拡張子ごとにファイルを検索して処理
    for ext in audio_extensions:
        for file_path in glob.glob(os.path.join(directory, ext)):
            length = get_audio_length(file_path)
            if length <= min_threshold_seconds or length >= max_threshold_seconds:
                try:
                    os.remove(file_path)
                    print(f"削除しました: {file_path} (長さ: {length:.2f}秒)")
                except Exception as e:
                    print(f"ファイルの削除中にエラーが発生しました: {e}")

if __name__ == "__main__":
    target_directory_model = input("モデル名:")
    target_directory = f"outputs/{target_directory_model}/raw"
    delete_specific_length_audio_files(target_directory)
