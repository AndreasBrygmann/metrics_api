from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

from novaclient import client as novaclient
from keystoneauth1 import session
from keystoneauth1.identity import v3

def NovaClient():

    auth = v3.ApplicationCredential(auth_url='',
                                    application_credential_id='',
                                    application_credential_secret='')
    sess = session.Session(auth=auth)
    nova = novaclient.Client("2.0", session=sess)
    return nova

def checkServers():
    active = 0
    for i in range(9):
        server = NovaClient().servers.find(name = f"server{i}")
        status = server.status
        if status == "ACTIVE":
            active += 1

    return active

@app.get("/")
def read_root():
    return {"Hello": "WorldFROMPYTHON"}

@app.get("/metrics", response_class=PlainTextResponse)
def displayActiveVMs():
    active = checkServers()
    activeVMString = '# TYPE server_count_active gauge\n# HELP server_count_active "Number of active servers or VMs"\nserver_count_active{title="Active Virtual Machines", totalvms="9"} ' + str(active) + '\n'
    #template = f"<html><head><title>Is this Showing?</title></head><body><p>{activeVMString}</p></body></html>"
    
    return PlainTextResponse(content=activeVMString, status_code=200)