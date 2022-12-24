import serial
import asyncio
import websockets
import sys

ser = None  # serial connection
ws = None   # websocket connection


async def bridge(url, tty, speed):
    "Initializes connection to websocket and local serial port"
    global ser, ws

    ser = serial.Serial(tty, speed, parity=serial.PARITY_EVEN,
                        bytesize=7, timeout=1)
    ws = await websockets.connect(url, ping_interval=None)
    ser.write(b'\x07\x0c\x1f\x40\x41connexion\x0a')
    # cancel local echo (keyboard > modem > screen)
    ser.write(b'\x1b\x3b\x60\x58\x52')


async def w2m():
    "websocket > minitel"
    while (True):
        data = await ws.recv()
        ser.write(data.encode())


async def m2w():
    "websocket < minitel"
    while (True):
        if ser.inWaiting() > 0:
            tosend = ser.read(ser.inWaiting()).decode()
            await ws.send(tosend)
        else:
            await asyncio.sleep(0.1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bridge(sys.argv[1], sys.argv[2], sys.argv[3]))
    loop.run_until_complete(asyncio.gather(w2m(), m2w()))
