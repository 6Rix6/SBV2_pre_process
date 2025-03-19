import os
import yt_dlp
from moviepy import AudioFileClip
from pydub import AudioSegment
from pydub.silence import split_on_silence

def download_video():
    url = input("YouTubeのURLを入力: ")
    input_folder = 'inputs'
    os.makedirs(input_folder, exist_ok=True)
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{input_folder}/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # ダウンロードされたファイルを取得
    for filename in os.listdir(input_folder):
        if filename.endswith('.mp4'):
            return os.path.join(input_folder, filename)
    return None

def extract_audio(video_path):
    input_folder = 'inputs'
    output_folder = 'outputs'
    os.makedirs(output_folder, exist_ok=True)
    
    custom_filename = input("モデル名を入力: ")
    output_path = os.path.join(output_folder, f"{custom_filename}.wav")
    
    print(f"{video_path} から音声を抽出中...")
    audio_clip = AudioFileClip(video_path)
    audio_clip.write_audiofile(output_path, codec='pcm_s16le', logger='bar')
    print(f"{output_path} に保存されました。\n")
    
    os.remove(video_path)
    print(f"{video_path} を削除しました。\n")
    
    return output_path

def split_audio(audio_path):
    output_folder = 'outputs'
    base_filename = os.path.splitext(os.path.basename(audio_path))[0]
    
    try:
        audio = AudioSegment.from_wav(audio_path)
        decibels = audio.dBFS
        
        chunks = split_on_silence(
            audio,
            min_silence_len=1000, # 無音と判定する最小の時間（ミリ秒）
            silence_thresh=decibels-29,  # 無音と判定するデシベル（オーディオのdBFSに基づく）
            keep_silence=250 # 分割後も無音を残す時間（ミリ秒）
        )
        
        print(f"{audio_path} の分割結果: {len(chunks)} チャンクが作成されました。")
        
        voice_folder = os.path.join(output_folder, base_filename, "raw")
        os.makedirs(voice_folder, exist_ok=True)
        
        for i, chunk in enumerate(chunks):
            chunk_path = os.path.join(voice_folder, f"{base_filename}_chunk_{i+1}.wav")
            chunk.export(chunk_path, format="wav")
            print(f"{chunk_path} に保存しました。")
        
        os.remove(audio_path)
        print(f"{audio_path} を削除しました。\n")
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def main():
    video_path = download_video()
    if video_path:
        audio_path = extract_audio(video_path)
        split_audio(audio_path)
    print("すべての処理が完了しました。")

if __name__ == "__main__":
    main()
