"""Test the microservice's response time, scalability, and stability under load."""
from locust import HttpUser, task, between

class PdfSummarizerUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def summarize_pdf(self):
        files = {'file': open('large_test.pdf', 'rb')}
        self.client.post("/summarize", files=files)
