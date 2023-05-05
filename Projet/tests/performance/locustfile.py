"""Locust test package"""
from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    """Test class for Locust"""

    @task
    def home(self):
        """Tests the home page"""
        self.client.get("/")

    #       Chaque test doit tester une route différente
    #       Chaque test doit être executé 2 fois plus de fois que le précédent.

    # Pas sur du truc
    @task(2)
    def about(self):
        """Tests the login page twice"""
        self.client.get("/display_password")

    @task(4)
    def contact(self):
        """Tests the contact page four times"""
        self.client.post("/generate_password")
