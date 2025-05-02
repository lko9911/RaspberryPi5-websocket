import asyncio
import websockets
import json

async def send_data():
    uri = "ws://192.168.150.77:8765"
    async with websockets.connect(uri) as websocket:
        data = {"X": 150.0, "Y": 45.0, "Z": 67.0}
        await websocket.send(json.dumps(data))
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(send_data())
