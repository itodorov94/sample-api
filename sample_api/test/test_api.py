import sys
from os.path import isfile, join, abspath, dirname
import logging
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))) + "/sample_api")
from test import BaseTestCase

class TestSeachAPI(BaseTestCase):
    """PetController integration test stubs"""


    def test_search_application_with_all_params(self):
        """Test case for finding application by passing all params

        Finds Pets by tags
        """
        query_string = [('appName', 'via_desktop'), ('os', 'macos'), ('version', "9")]
        response = self.client.open(
            '/api/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_application_with_no_params(self):
        response = self.client.open(
            'api/search', 
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8') )

    def test_search_application_with_wrong_param_value(self):
        query_string = [('appName', 'wrong_value')]
        response = self.client.open(
            'api/search', 
            method='GET',
            query_string=query_string)
        self.assert400(response,
                        'Response body is : ' + response.data.decode('utf-8') )
    
    def test_download_application_with_no_param(self):
        response = self.client.open(
            'api/download', 
            method='GET')
        self.assert400(response,
                        'Response body is : ' + response.data.decode('utf-8') )

    def test_download_application_with_correct_param(self):
        query_string = [('file_identifier', 'correct_value')]
        response = self.client.open(
            'api/search', 
            method='GET',
            query_string=query_string)
        self.assert200(response,
                        'Response body is : ' + response.data.decode('utf-8') )
    

if __name__ == '__main__':
    import unittest
    unittest.main()
