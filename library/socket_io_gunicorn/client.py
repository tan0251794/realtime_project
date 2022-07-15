import asyncio
import random

import socketio

from library.constant.socket import BOT_MESSAGES

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print('connection established')


@sio.event
async def my_message():
    while True:
        await asyncio.sleep(random.randint(5, 10))
        print(sio.get_sid(), 'post a message to server')
        await sio.emit('my_message', f'{sio.get_sid()}: {BOT_MESSAGES[random.randint(0, len(BOT_MESSAGES)-1)]}')


@sio.event
async def disconnect():
    print('disconnected from server')


async def main():
    await sio.connect('http://localhost:6600')
    await my_message()
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(main())
