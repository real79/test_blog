from django.test import TestCase

class TestListView(TestCase):
    def testMain(self):
        response=self.client.get('http://testserver/')
        assert response.status_code==200

