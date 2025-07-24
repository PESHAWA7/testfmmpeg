import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from telethon.tl.types import InputPeerChannel
import asyncio
import tqdm
import subprocess
# Load .env
load_dotenv()
# api_id = int(os.getenv("API_ID"))
# api_hash = os.getenv("API_HASH")
api_id = int(os.getenv("APITELEGRAM_ID")) 
api_hash = os.getenv("APITELEGRAM_HASH")
channel_to_send = -1002384585674

DOWNLOADS_DIR = "downloads100"
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

client = TelegramClient("name1", api_id, api_hash)
client.start()


# def show_progress(current, total):
#     percent = int(current * 100 / total) if total else 0
#     print(f"\r📥 Downloading... > {percent}%", end="")

def download_and_forward(chat, limit):
    # isdownload = True
    messages = client.get_messages(chat, limit=limit)

    reverse_data = messages[::-1]

    # all_listed_id = [message.id for message in messages if "چیرۆکی شەوێک" in message.text and message.media]

    # max_id = max(all_listed_id) if all_listed_id else print("No messages found with the specified text and media.")


    for msg in tqdm.tqdm(reverse_data):


        if msg.media:


            # for message2 in tqdm.tqdm(messages) if message2.media and "چیرۆکی شەوێک" in message2.text and message2.id == max_id:
            #     current_max_id = msg.id
            #     DOWNLOAD_VIDEO = message2

            

            try:
                
                print(f"\n📥 Downloading media from message ID {msg.id} {msg.text}...")
                filename = client.download_media(msg, DOWNLOADS_DIR)

                if filename:

                    # Input and output file paths
                    input_file = filename
                    output_file = "output_test.mp4"

                    # FFmpeg command: trim 10 seconds, overlay text
                    command = [
                        "ffmpeg",
                        "-i", input_file,
                        "-vf", "drawtext=text='Test Video':fontcolor=white:fontsize=30:x=(w-text_w)/2:y=h-60",
                        "-t", "10",
                        "-c:a", "copy",
                        output_file
                    ]

                    # Run the command
                    try:
                        subprocess.run(command, check=True)
                        print("✅ Video edited successfully.")
                    except subprocess.CalledProcessError as e:
                        print("❌ FFmpeg error:", e)


                    print(f"\n✅ Downloaded: {filename}")

                    # Send to another channel
                    client.send_file(channel_to_send, filename, caption=f"{msg.text}")
                    print(f"🚀 Sent to {channel_to_send}\n")

                    

                    # Delete file
                    os.remove(filename)
                    print(f"🗑️ Deleted {filename}")

            except Exception as e:
                print(f"❌ file Error : {e}")



if __name__ == "__main__":
    source = "@hadiagull"
    limit = 2
    download_and_forward(source, limit)
