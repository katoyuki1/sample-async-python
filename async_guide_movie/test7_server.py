import asyncio


class ChatServer:
    def __init__(self):
        self.clients = []

    async def handle_client(self, reader, writer):
        self.clients.append(writer)
        addr = writer.get_extra_info('peername')
        print(f"New connection from {addr}")
        while True:
            data = await reader.read(100)
            if not data:
                print(f"Connection closed by {addr}")
                self.clients.remove(writer)
                writer.close()
                break
            message = data.decode()
            print(f"Recived from {addr}: {message}")
            for client in self.clients:
                if client != writer:
                    client.write(data)
                    await client.drain()
        print(f"End connection from {addr}")

    async def run_Server(self, host, port):
        server = await asyncio.start_server(self.handle_client, host, port)
        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    chat = ChatServer()
    asyncio.run(chat.run_Server("localhost", 5003))