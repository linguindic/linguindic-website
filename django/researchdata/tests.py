from django.test import TestCase
from django.urls import reverse


class TestLinguisticNotionListView(TestCase):
    """
    Test LinguisticNotionListView
    """
    def test_linguisticnotion_empty_get(self):
        """
        Test the linguistic notions page is returned
        """
        url = reverse('research-linguisticnotion-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Notions')

    def test_linguisticnotion_nonempty_get(self):
        """
        Test the linguistic notions page is returned
        """
        url = reverse('research-linguisticnotion-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Notions')


class TestLinguisticNotionDetailView(TestCase):
    """
    Test LinguisticNotionDetailView
    """
    def test_linguisticnotion_empty_get(self):
        """
        Test the linguistic notions page is returned
        """
        url = reverse('research-linguisticnotion-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Notion')

    def test_linguisticnotion_nonempty_get(self):
        """
        Test the linguistic notions page is returned
        """
        url = reverse('research-linguisticnotion-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Notion')
