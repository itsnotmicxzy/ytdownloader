# YouTube Downloader

YouTube Downloader is a simple web application built with Flask that allows users to download videos and audio from YouTube in MP4 and MP3 formats respectively.

## Features

- Download YouTube videos in MP4 format.
- Extract audio from YouTube videos and download it in MP3 format.
- Simple user interface with Bootstrap styling.
- Responsive design, suitable for desktop and mobile devices.

## Setup

1. Clone the repository:

```
git clone https://github.com/itsnotmicxzy/youtube-downloader.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Flask application:

```
python app.py
```

4. Open a web browser and go to `http://localhost:5000` to access the application.

## Usage

1. Enter the URL of the YouTube video you want to download.
2. Choose the desired file format (MP4 or MP3).
3. Click the "Download" button.
4. The file will be downloaded to your device.

## Dependencies

- Flask
- pytube
- moviepy

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
