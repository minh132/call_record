# Call Record API
# Getting Started
Follơw these steps to set up and run the Call_record API:
## 1. Clone this repo
```bash
git clone https://github.com/minh132/call_record.git
```
## 2. Build dockercompose 
Run the following command to build docker compose:
```bash
docker compose build
```
## 3. Run dockercompose
Run docker compose, execute command below and wait a few minutes to run testcase and start server:
```bash
docker compose up
```
## 4. TestAPI
Go to ``` http://0.0.0.0:8888/docs ``` to test API

# Gunicorn with Uvicorn Workers
Gunicorn supports working as a process manager and allowing users to tell it which specific worker process class to use. Then Gunicorn would start one or more worker processes using that class.
I use [JMeter](https://jmeter.apache.org/) to test success rate when send many request with resource limit in docker-compose(2 core cpu and 2048m memory) . Result when use uvicorn and gunicorn with same config in JMeter, send 2500 request in 2 seconds and set timeout 2s:

Gunicorn

![Uvicorn](https://github.com/minh132/call_record/assets/89315105/b2e4eab0-a9b6-4467-be0f-798a436a9fb6)
Uvicorn

![Screenshot from 2024-01-04 20-58-52](https://github.com/minh132/call_record/assets/89315105/d1971586-4b35-4b11-b4ff-fee12062fd79)

The result shows that using Gunicorn help error rate reduce from 84% to 39%
