import os
import json
import asyncio
import aiohttp

base_url = "https://cdn.albiononline2d.com/game-images/"

async def download_avatar(session, avatar_name):
    url = f"{base_url}{avatar_name}.png"
    file_path = f"albion_images/{avatar_name}.png"

    if os.path.exists(file_path):
        print(f"Skipping download for {avatar_name} as file already exists.")
        return

    async with session.get(url) as response:
        if response.status == 200:
            with open(file_path, "wb") as file:
                file.write(await response.read())
            print(f"Image for {avatar_name} downloaded successfully.")
        else:
            print(f"Failed to download image for {avatar_name}, status code: {response.status}.")

async def main():
    os.makedirs("albion_images", exist_ok=True)

    with open('mobs.json') as json_file:
        mobs_data = json.load(json_file)
        
    async with aiohttp.ClientSession() as session:
        tasks = []

        for mob in mobs_data:
            task = asyncio.create_task(download_avatar(session, mob['avatar']))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
