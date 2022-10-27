from locust import HttpUser, task, between


class APIUser(HttpUser):

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO
    wait_time = between(3, 5)
    '''
    This load testing workflow consists of X steps:

    1. Enter the website: index_gate
    2. Charge an image using "datefile"
    
    '''

    @task
    def index_get(self):
        self.client.get("/")

    @task
    def index_post(self):
        datafile={'file':open('dog.jpeg','rb')}
        self.client.post("/predict", files=datafile)



    
