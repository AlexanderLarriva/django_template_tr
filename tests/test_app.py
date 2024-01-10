from django.test import TestCase


class AppTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/about')
        self.assertContains(response, '/articles')

    def test_articles(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/index.html')
        self.assertContains(response, 'How to foo?')
        self.assertContains(response, 'F. BarBaz')
