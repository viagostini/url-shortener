from locust import HttpUser, between, task

API_ROOT = "http://localhost:8000"


class Getter(HttpUser):
    """This user creates one shortlink and proceeds to perform several GET requests"""

    host = API_ROOT
    shortlink = ""
    wait_time = between(0.005, 0.01)

    def on_start(self):
        response = self.client.post(url="/", json={"url": "google.com"})
        self.shortlink = response.json()["shortlink"].split("/")[-1]

    @task
    def get_url(self):
        self.client.get(f"/{self.shortlink}")
