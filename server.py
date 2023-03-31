import websockets
import asyncio
import random
import constant


def getRandomNumber():
    return random.uniform(constant.GEOMETRY_MINIMUM_SIZE, constant.GEOMETRY_MAXIMUM_SIZE)

async def main(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            if message == "size_request":
                randomInt = getRandomNumber()
                await websocket.send(str(randomInt))

    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")


start_server = websockets.serve(main, "localhost", constant.PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

print("Server listening on Port " + str(constant.PORT))
