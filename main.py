import asyncio
import aiohttp


async def check_website_status(session, url):
    try:
        async with session.get(url) as response:
            print(f"Status of {url}: {response.status}")
    except aiohttp.ClientError as e:
        print(f"Error checking {url}: {e}")


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [check_website_status(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    # รายการเว็บไซต์ที่ต้องการตรวจสอบ
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.example.com",
        "https://www.narutodeagonball559.com",  # เว็บไซต์ที่ไม่ถูกต้องเพื่อทดสอบ error
    ]

    # รันโปรแกรม
    asyncio.run(main(urls))
