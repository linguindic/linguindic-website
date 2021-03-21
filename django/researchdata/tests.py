from django.test import TestCase
from django.urls import reverse


class TestAuthorListView(TestCase):
    """
    Test AuthorListView
    """
    def test_author_empty_get(self):
        """
        Test the author page is returned
        """
        url = reverse('browse-authors-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Authors')

    def test_author_nonempty_get(self):
        """
        Test the author page is returned
        """
        url = reverse('browse-authors-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Authors')


class TestLinguisticFieldListView(TestCase):
    """
    Test LinguisticFieldListView
    """
    def test_linguisticfield_empty_get(self):
        """
        Test the linguistic fields page is returned
        """
        url = reverse('browse-linguisticfields-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Fields')

    def test_linguisticfield_nonempty_get(self):
        """
        Test the linguistic fields page is returned
        """
        url = reverse('browse-linguisticfields-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Fields')


class TestLinguisticNotionListView(TestCase):
    """
    Test LinguisticNotionListView
    """
    def test_linguisticnotion_empty_get(self):
        """
        Test the linguistic notions page is returned
        """
        url = reverse('browse-linguisticnotions-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Notions')

    def test_linguisticnotion_nonempty_get(self):
        """
        Test the linguistic notions page is returned
        """
        url = reverse('browse-linguisticnotions-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Notions')


class TestLinguisticTraditionListView(TestCase):
    """
    Test LinguisticTraditionListView
    """
    def test_linguistictradition_empty_get(self):
        """
        Test the linguistic traditions page is returned
        """
        url = reverse('browse-linguistictraditions-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Traditions')

    def test_linguistictradition_nonempty_get(self):
        """
        Test the linguistic traditions page is returned
        """
        url = reverse('browse-linguistictraditions-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Linguistic Traditions')


class TestReferenceListView(TestCase):
    """
    Test ReferenceListView
    """
    def test_reference_empty_get(self):
        """
        Test the reference page is returned
        """
        url = reverse('browse-references-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'References')

    def test_reference_nonempty_get(self):
        """
        Test the reference page is returned
        """
        url = reverse('browse-references-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'References')


class TestSanskritWordListView(TestCase):
    """
    Test SanskritWordListView
    """
    def test_sanskritword_empty_get(self):
        """
        Test the sanskrit words page is returned
        """
        url = reverse('browse-sanskritwords-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Sanskrit Words')

    def test_sanskritword_nonempty_get(self):
        """
        Test the sanskrit words page is returned
        """
        url = reverse('browse-sanskritwords-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Sanskrit Words')


class TestTextListView(TestCase):
    """
    Test TextListView
    """
    def test_text_empty_get(self):
        """
        Test the texts page is returned
        """
        url = reverse('browse-texts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Texts')

    def test_text_nonempty_get(self):
        """
        Test the texts page is returned
        """
        url = reverse('browse-texts-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Texts')


class TestTextPassageListView(TestCase):
    """
    Test TextPassageListView
    """
    def test_textpassage_empty_get(self):
        """
        Test the text passages page is returned
        """
        url = reverse('browse-textpassages-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Text Passages')

    def test_text_nonempty_get(self):
        """
        Test the text passages page is returned
        """
        url = reverse('browse-textpassages-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Text Passages')
