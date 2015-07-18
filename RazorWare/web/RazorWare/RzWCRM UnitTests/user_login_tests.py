__author__ = 'David Boarman on 6/23/2015, (c) 2015, RazorWare, LLC'

import json
import unittest

from urllib import request


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.__url = "http://localhost:8000/razorcrm/rzm_login"
        self.__jbrad_acct = "123-joe-8a35c518"

    def test_send_login_request(self):
        data = json.dumps({
            'user_id': "jbrad",
            'password': "test"
        })
        jdata = data.encode('utf-8')

        req = request.Request(self.__url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        req.add_header('Content-Length', len(jdata))

        with request.urlopen(self.__url, jdata) as f:
            response = json.loads(f.read().decode('utf-8'))

        self.assertTrue("result" in response, "fail: response does not have result")

        if "result" in response and response['result']:
            self.assertTrue(response['result'], "fail: response result false")
            self.assertEqual(self.__jbrad_acct, response['acct_id'], "fail: response result account")
            self.assertEqual(True, response['active'], "fail: response account not active")
            self.assertEqual(False, response['reset'], "fail: response account is reset-enabled")
        else:
            self.fail("fail: {response}".format(response=response))


if __name__ == '__main__':
    unittest.main()
