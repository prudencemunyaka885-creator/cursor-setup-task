from supadata import Supadata

client = Supadata(api_key="sd_151908e5b7329a2da23d23a0d85e4a69")

videos = [
      {"channel": "neil-patel", "url": "https://www.youtube.com/watch?v=3q3WBkSoANA"},
    {"channel": "matt-diggity", "url": "https://www.youtube.com/watch?v=4GBlHObjOrY"},
    {"channel": "surfer-seo", "url": "https://www.youtube.com/watch?v=NkOcLZpCMxI"},
    {"channel": "webhive-digital", "url": "https://www.youtube.com/watch?v=NkOcLZpCMxI"},
]

import os
os.makedirs("research/youtube-transcripts", exist_ok=True)

for video in videos:
    print(f"Getting transcript for {video['channel']}...")
    transcript = client.youtube.transcript(video["url"])
    
    filename = f"research/youtube-transcripts/{video['channel']}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {video['channel']} — YouTube Transcript\n\n")
        for item in transcript.content:
            f.write(item.text + " ")
    
    print(f"Saved: {filename}")

print("All done!")