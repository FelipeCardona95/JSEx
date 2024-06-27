import os
import json
import asyncio
import aiohttp

async def download_spell_image(session, spell_data):
    spell_url = f"https://render.albiononline.com/v1/spell/{spell_data['@uniquename']}.png"
    file_path = f"spell_images/{spell_data['@uniquename']}.png"

    if os.path.exists(file_path):
        print(f"Skipping download for {spell_data['@uniquename']} as file already exists.")
        return

    async with session.get(spell_url) as response:
        if response.status == 200:
            with open(file_path, "wb") as file:
                file.write(await response.read())
            print(f"Image for {spell_data['@uniquename']} downloaded successfully.")
        else:
            print(f"Failed to download image for {spell_data['@uniquename']}.")

async def main():
    os.makedirs("spell_images", exist_ok=True)

    async with aiohttp.ClientSession() as session:
        with open('spells.json') as json_file:
            data = json.load(json_file)
            tasks = []

            for spell_type in ['passivespell', 'activespell', 'togglespell']:
                for spell in data['spells'][spell_type]:
                    task = asyncio.create_task(download_spell_image(session, spell))
                    tasks.append(task)

            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())