# Virtual Machine Metrics
This program creates a docker service that creates a output that can be scraped by prometheus. The output is a list of active virtual machines

## Instructions for running on docker
1. Copy the repo
```bash
git clone https://github.com/AndreasBrygmann/metrics_api
```
2. navigate to repo
```bash
cd metrics_api
```

3. Build image
```bash
docker build -t metrics:v1 .
```

4. Run image
```bash
docker run -d --name=metricsapi -p 9080:80 metrics:v1
```
Note: This will make the image run on port 9080 

## Testing
Check that the image is running
```bash
docker ps
```

If there were any problems it will show up on:
```bash
docker logs <ID or name>
```

Check that the service is creating the correct output:
```bash
curl http://localhost:9080/metrics
```