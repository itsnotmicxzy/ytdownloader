from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os
import moviepy.editor as mp
import schedule
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        choice = request.form['choice']
        output_folder = './downloads'

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        if choice == 'mp4':
            download_video(url, output_folder)
            filename = os.path.join(output_folder, os.listdir(output_folder)[-1])
            return send_file(filename, as_attachment=True)
        elif choice == 'mp3':
            download_audio(url, output_folder)
            audio_filename = os.path.join(output_folder, os.listdir(output_folder)[-1])
            mp3_output_filename = os.path.splitext(audio_filename)[0] + ".mp3"
            convert_to_mp3(audio_filename, mp3_output_filename)
            return send_file(mp3_output_filename, as_attachment=True)
    
    return render_template('index.html')

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print("Downloading video...")
        stream.download(output_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", e)

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        print("Downloading audio...")
        stream.download(output_path)
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", e)

def convert_to_mp3(input_path, output_path):
    try:
        clip = mp.AudioFileClip(input_path)
        clip.write_audiofile(output_path)
        print("Conversion to MP3 successful!")
    except Exception as e:
        print("Error:", e)

def delete_downloaded_files():
    output_folder = './downloads'
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted {file_path}")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    # Schedule the deletion of downloaded files every 10 minutes
    schedule.every(10).minutes.do(delete_downloaded_files)

    # Run the Flask app
    app.run(port=2323, debug=True)
    
    # Run the scheduler in a loop
    while True:
        schedule.run_pending()
        time.sleep(1)
