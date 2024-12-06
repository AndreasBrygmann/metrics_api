from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

from novaClient import NovaClient

nova = NovaClient()

def checkServers():
    active = 0
    suspended = 0
    for i in range(9):
        server = nova.servers.find(name = f"server{i}")
        status = server.status
        if status == "ACTIVE":
            active += 1
        elif status == "SUSPENDED":
            suspended += 1

    return active, suspended

@app.get("/")
def read_root():
    return {"Hello": "WorldFROMPYTHON"}

@app.get("/metrics", response_class=PlainTextResponse)
def displayActiveVMs():
    activeVMString = '# TYPE server_count gauge\n# HELP server_count "Number of active servers or VMs"\nserver_count_python{title="Active Virtual Machines", totalvms="9"} ' + str(active) + '\n'
    #template = f"<html><head><title>Is this Showing?</title></head><body><p>{activeVMString}</p></body></html>"
    
    return PlainTextResponse(content=activeVMString, status_code=200)