import requests
import subprocess
from tqdm import tqdm
import os

def download_segment(url, output_path, filename, total_size):
    response = requests.get(url, stream=True)
    with open(output_path, 'wb') as file, tqdm(
            desc=filename,
            total=total_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            bar.update(len(chunk))

video_url = str(input("Video URL : "))
audio_url = str(input("Audio URL : "))
video_output_path = "video.mp4"
audio_output_path = "audio.mp4"

# Get the content length (total size) of the video and audio files for progress bar
video_response = requests.head(video_url)
audio_response = requests.head(audio_url)
video_total_size = int(video_response.headers.get('content-length', 0))
audio_total_size = int(audio_response.headers.get('content-length', 0))

# Download video and audio segments with progress bars
download_segment(video_url, video_output_path, "Downloading Video", video_total_size)
download_segment(audio_url, audio_output_path, "Downloading Audio", audio_total_size)


# Get the full path to the FFmpeg executable
# To merge both audio video, add ffmpeg path here"

ffmpeg_path = r'ffmpeg path'

# Merge video and audio using FFmpeg with a progress bar
output_file = r"name-of-file"

# Merge video and audio using FFmpeg with a progress bar
ffmpeg_command = [
    ffmpeg_path,
    "-i", video_output_path,
    "-i", audio_output_path,
    "-c:v", "copy",
    "-c:a", "aac",
    "-strict", "experimental",
    "-y",  # Overwrite output if it already exists
    output_file
]

subprocess.run(ffmpeg_command)


print("Merging complete. Output file:", output_file)

os.remove("video.mp4")
os.remove("audio.mp4")
