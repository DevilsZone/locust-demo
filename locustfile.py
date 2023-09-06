from random import random

from locust import HttpUser, task, between


class BusinessProfileUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests

    # Replace these with appropriate values
    TEST_LEGAL_NAME = "TestCorp"
    TEST_EMAIL = "test@example.com"
    params = {'legalName': TEST_LEGAL_NAME}
    headers = {'Accept': 'application/json'}

    # POST request to create a business profile
    @task(1)
    def create_business_profile(self):
        self.client.post("/business-profile", json={
            "companyName": "Test Company",
            "legalName": self.TEST_LEGAL_NAME+str(random()),
            "email": self.TEST_EMAIL,
            "website": "https://www.test.com",
            "businessAddress": {
                "line1": "123 Test Street",
                "city": "Test City",
                "state": "TS",
                "zipCode": "12345",
                "country": "Testland"
            },
            "legalAddress": {
                "line1": "456 Legal Street",
                "city": "Legal City",
                "state": "LS",
                "zipCode": "67890",
                "country": "Legalland"
            },
            "taxIdentifiers": {"pan": "ID1234", "ein": "ID5678"},
            "createdBy": "test-creation"
        }, headers=self.headers)

    # GET request to fetch a business profile by legal name
    @task(2)
    def get_business_profile_by_legal_name(self):
        self.client.get(f"/business-profile?legalName={self.TEST_LEGAL_NAME}", headers=self.headers)

    # PUT request to update a business profile
    @task(1)
    def update_business_profile(self):
        self.client.put("/business-profile", json={
            "legalName": self.TEST_LEGAL_NAME,
            "email": "updated@example.com"
        }, headers=self.headers)

    # DELETE request to delete a business profile
    # @task(1)
    # def delete_business_profile(self):
    #     self.client.delete("/business-profile", json={
    #         "legalName": self.TEST_LEGAL_NAME
    #     })

# Ensure you have locust installed (`pip install locust`)
# To run: `locust -f locustfile.py`
