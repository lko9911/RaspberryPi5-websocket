import asyncio
import websockets
import json

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        print("Received IK solution:", data)

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
