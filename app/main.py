from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

from novaclient import client as novaclient
from keystoneauth1 import session
from keystoneauth1.identity import v3

def NovaClient():

    auth = v3.ApplicationCredential(auth_url='https://pegasus.sky.oslomet.no:5000/v3',
                                    application_credential_id='bf1cb183404d4490ae0d04f3737c4c9a',
                                    application_credential_secret='6stPHUnryXuL9Yo_3TWqVnm7jWodPYBJzv5SyUpXfPzm4ZCK0W739bH4QXuqHwIwMkBK6nGopXVTRDnTlfCbqg')
    sess = session.Session(auth=auth)
    nova = novaclient.Client("2.0", session=sess)
    return nova

def checkServers():
    active = 0
    suspended = 0
    for i in range(9):
        server = NovaClient().servers.find(name = f"server{i}")
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