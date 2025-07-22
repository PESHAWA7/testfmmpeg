import subprocess
from pytube import YouTube

# Example short video URL (replace with your own if needed)
yt_url = "https://youtu.be/JORaOqnh2KM?si=-X_YeDHuqwcPcvWU"  # Sample short video from yt-dlp project
# Output file name
output_filename = "input.mp4"

try:
    yt = YouTube(yt_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(f"🎬 Downloading: {yt.title}")
    stream.download(filename=output_filename)
    print(f"✅ Saved as {output_filename}")
except Exception as e:
    print("❌ Error downloading video:", e)


input_file = "input.mp4"
output_file = "output_trimmed.mp4"

# Trim first 10 seconds of video
command = [
    "ffmpeg",
    "-i", input_file,
    "-t", "10",         # Duration: 10 seconds
    "-c", "copy",       # Copy codec (no re-encoding, fast)
    output_file
]

try:
    subprocess.run(command, check=True)
    print("✅ Video trimmed and saved as", output_file)
except subprocess.CalledProcessError as e:
    print("❌ FFmpeg error:", e)
