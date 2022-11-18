import asyncio
import aiohttp
import time 

API_KEY = "your api key"

async def get_weather(cityname):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}"
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        if(resp.status == 200):
            data = await resp.json()
            print(cityname,":", round(data['main']['temp'] - 273.15, 2))
        else:
            print("error")    


async def main():
    start = time.time()
    await asyncio.gather(get_weather("damascus"), get_weather("chicago"), get_weather("london"), get_weather("berlin"), get_weather("amsterdam"), get_weather("brussels"), get_weather("caracas"), get_weather("paris"))
    end = time.time() - start
    print("Time elapsed", round(end, 2))

if __name__ == "__main__":
    # RUN MAIN LOOP OR EVENT LOOP
    asyncio.run(main())
