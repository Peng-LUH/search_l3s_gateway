import os, requests
# import schedule
# import time
from flask import request, url_for
from l3s_gateway_api import create_app
from l3s_gateway_api import db
from apscheduler.schedulers.background import BackgroundScheduler
import schedule, time, threading
import socket
from pprint import pprint


from dotenv import load_dotenv

load_dotenv()


app = create_app(os.getenv("FLASK_ENV", "development"))

os.environ["HOST_NAME"] = socket.gethostname()

## import database tables
from l3s_gateway_api.models.test import Test
from l3s_gateway_api.models.task import Task
from l3s_gateway_api.models.document import Document

##Create db tables
with app.app_context():
    db.create_all()


# requests.head("http://127.0.0.1:9040/l3s-gateway/")


##----------------------- Schedule Synchronization --------------- ##
def scheduled_task():
    ## set the server name
    # host_name = socket.gethostname()
    # host_ip = socket.gethostbyname(host_name)
    # app.config['SERVER_NAME'] = f"{host_ip}:9040"
    app.config['SERVER_NAME'] = f"localhost:9040"
    print(app.config['SERVER_NAME'])
    
    with app.app_context():
        app.logger.info("App Context: ...")
        app.logger.info("Running scheduled task")
        # request_url = url_for('api.l3s_db_sync')
        request_url = url_for('api.search_srv_connection')
        app.logger.info(f"request_url: {request_url}\n")
        response = requests.get(request_url)
        print(response.json())
    #     # app.cli.invoke(run_database_updater)
    
    app.logger.info("Out of App Context")
    app.logger.info(f"Send HTTP request to {request_url}:")
    # response = requests.get(request_url)
    # pprint(response.json())
    app.logger.info("Schedule Done: Search Service Synchronization")
    # response = requests.get(request_url)
    # print(response.json())
    return
    
## Schedule the task to run every 10 minutes
schedule.every(30).seconds.do(scheduled_task)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

#----------------------------------------------------------
## Start the scheduler in a separate thread
# scheduler_thread = threading.Thread(target=run_scheduler)
# scheduler_thread.start()
#----------------------------------------------------------

####
# @app.before_first_request
# def before_first_request():
#     print(f"******* This is what I'm doing before the first request ********")
    # request_url = get_request_url('api.recsys_service_connection')
    # response = requests.get(request_url)
    # print(response.json())
    # response = requests.get('http://localhost:9040/example')
    # print("Response from the endpoint:", response.json())
    # call(["python", "test.py"])
    # response = requests.get("http://localhost:9040/l3s-gateway/l3s-search/connection")
    # print(response.json())


####
# @app.before_first_request
# def before_first_request():
#     # Make a request to your endpoint after the app is started
#     with app.app_context():
#         # response = app.test_client().get('/your_endpoint')
#         # print(f"Response from /your_endpoint: {response.get_data(as_text=True)}")
#         print("before_first_request")


if __name__ == "__main__":
    ## Create a scheduler
    # scheduler = BackgroundScheduler()

    ## Schedule the task to run every 10 minutes
    # scheduler.add_job(scheduled_task, 'interval', minutes=0.5)

    ## Start the scheduler
    # scheduler.start()

    app.run(debug=True, host="0.0.0.0", port="9040")
    # app.test_client().get('/')
    # call(["python", "test.py"])
    # response = request_url = get_request_url('api.recsys_service_connection')
    # print("Response from the endpoint:", response.json())
    
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    

@app.shell_context_processor
def shell():
    return {"db": db,
            "test": Test,
            "task": Task,
            "document": Document}