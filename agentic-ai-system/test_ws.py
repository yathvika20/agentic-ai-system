import asyncio
import websockets


async def main():

    uri = "ws://127.0.0.1:8000/api/v1/ws/user1"


    async with websockets.connect(uri) as ws:


        await ws.send(

            "What is RAG?"

        )


        while True:


            msg = await ws.recv()


            print(msg)


            if msg == "[DONE]":


                break


asyncio.run(main())