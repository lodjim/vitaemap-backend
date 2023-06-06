from fastapi import FastAPI
import uvicorn
from schemas_io import *
import argparse

class APIServer:

    def __init__(self,host:str,port:int) -> None:
        
        self.host = host
        self.port = port 
        
        self.api = FastAPI()
        # get request
        self.api.add_api_route('/heartbeat',self.heartbit,methods=['GET'],response_model=HeartbeatResponse)



    async def heartbit(self):
        return HeartbeatResponse(status='alive')

    async def registration(self):
        pass


    def start_server(self):
        server_config = uvicorn.Config(self.api,host=self.host,port=self.port)
        server = uvicorn.Server(server_config)
        server.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ceci est un server fastapi')
    parser.add_argument('--host',type=str,help="mettre le endpoint d'ecoute de votre server",default="0.0.0.0")
    parser.add_argument('--port',type=int,help="mettre le port d'ecouter de votre server",default=8080)
    args = parser.parse_args()
    api = APIServer(host=args.host,port=args.port)
    api.start_server()
