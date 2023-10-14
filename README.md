# python-celery-ms
Python Microservice with shared celery instance

# To run it set below .env
```
PYTHONPATH=/home/user/path/to/ms-celery
```
# do the basic packages installation
```
cd user && pip install -r requirements.txt

cd project && pip install -r requirements.txt
```
# vulcan holds shared celery instance
```
cd vulcan && pip install -r requirements.txt
```
# Run the project
```
cd user
python -m run
```
# Run the worker
```
cd celery
celery -A vulcan.celery_instance worker -l INFO
```
# To test hit the <add> API from USER
```curl http://localhost:8081/add/2/1```

### You can see the process is being hit in the worker
