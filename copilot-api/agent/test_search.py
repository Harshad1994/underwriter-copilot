
import asyncio

from dotenv import load_dotenv

_ = load_dotenv()

from tavily import AsyncTavilyClient

client = AsyncTavilyClient("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")


async def main():
    return await client.search(query="capital of India")


if __name__=="__main__":
    print(asyncio.run(main()))

