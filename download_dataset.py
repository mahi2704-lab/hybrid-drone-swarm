import time
from icrawler.builtin import BingImageCrawler
import os

base_dir = "dataset/train"

classes = {
    "flood": "flood disaster city submerged houses rescue boat people water damage 2024",
    "fire": "big building fire flames smoke firefighters emergency burning house 2024",
    "earthquake": "earthquake collapsed buildings rubble disaster rescue 2024 damage",
    "safe": "normal city park street people walking sunny day traffic clean environment 2024"
}

for cls, query in classes.items():
    save_dir = os.path.join(base_dir, cls)

    crawler = BingImageCrawler(
        storage={"root_dir": save_dir},
        downloader_threads=6
    )

    crawler.crawl(
        keyword=query + " real",
        max_num=200
    )

    time.sleep(10)  # IMPORTANT (avoids blocking)

print("Done")