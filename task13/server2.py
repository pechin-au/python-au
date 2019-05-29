#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets

n = 0    
msg = ""
t = 5

async def producer_handler(websocket):
    while True:
        message = await producer()
        if (message != ""):
            await websocket.send(message)
        await asyncio.sleep(0.1)

async def consumer_handler(websocket):
    async for message in websocket:
        await consumer(message + '\n')

async def handler(websocket, path):
    consumer_task = asyncio.ensure_future(consumer_handler(websocket))
    producer_task = asyncio.ensure_future(producer_handler(websocket))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        task.cancel()

async def producer():
    global msg, t
    data = msg
    if t:
        t -= 1
    else:
        msg = ""
        t = 2
    return data


async def consumer(message):
    global msg
    print(message)
    msg = message


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_server = websockets.serve(handler, '0.0.0.0', 8083)

    server_task = asyncio.ensure_future(start_server)

    loop.run_until_complete(asyncio.wait([server_task]))


    loop.run_forever()
