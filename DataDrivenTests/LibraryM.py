# DATA DRIVEN TEST USING MOKE DATA GENERATED BY MIMESIS MODULE
# in this file we will follow a document object model
# according to which we are creating separate file with common methods for using in test cases
# and covert generated data to json then post it
# then we separately create a testcase file

import requests
import random
from mimesis import Person, Datetime


class CommonM:

    def __init__(self, person=Person, datetime=Datetime):
        self.person = person('en')  # using mimesis mock Person lib for names
        self.datetime = datetime('en')
        self.date = self.datetime.formatted_date(fmt='')  # using mimesis Datetime lib for date of birth
        self.personal_data = {
            "first_name": self.person.first_name(),
            "middle_name": self.person.name(),
            "last_name": self.person.last_name(),
            "date_of_birth": self.date
        }

    def post_personal_data(self, api_url):
        """Generate an instance of the CommonM class, convert and post its self.personal data dict to api endpoint"""
        response = requests.post(api_url, json=self.personal_data)
        print(response.text)
        print(response.status_code)
        return response

    @staticmethod
    def assert_success(text='\nAssert successful'):
        print(text)
        return True