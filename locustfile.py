from locust import HttpUser, task, between

class CricketFan(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_highlights(self):
        self.client.get("/highlights")