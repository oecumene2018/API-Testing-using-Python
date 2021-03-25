# DATA DRIVEN TEST USING EXCEL TABLE
# in this file we will follow a document object model
# according to which we are creating separate file with common methods for using in test cases
# from excel and convert to json then post it
# then we separately create


import requests
import openpyxl


class CommonXl:

    def __init__(self, path_string: str, sheet_name: str): # class excepts path to excel file and sheet name
        self.book = openpyxl.load_workbook(path_string) # loading openpyxl book object
        self.sheet = self.book[sheet_name]  # getting the sheet object
        self.column_names = tuple(self.sheet.values)[0]     # this will create the tuple of column names
                                                            # which is the 1st row
        self.students_data = list(self.sheet.values)[1:]    # this will create the list of data tuples
                                                            # except the column names

    def send_post_request(self, api_url: str, student_data=None):
        """The method to post particular user data/one table row as json"""
        data_dict = {}
        for i in range(0, len(self.column_names)):      # setting key: value pairs
            data_dict[self.column_names[i]] = student_data[i] # column_name[index] - key, sudent data[indexx] - value
        response = requests.post(api_url, json=data_dict)
        print(response.text)
        return response

    @staticmethod
    def assert_success(text='\nAssert successful'):
        print(text)
        return True
