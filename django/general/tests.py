from django.test import TestCase
from django.urls import reverse


class TestWelcomeView(TestCase):
    """
    Test Welcome View
    """
    def test_welcome_empty_get(self):
        """
        Test the welcome page is returned
        """
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Welcome')

    def test_welcome_nonempty_get(self):
        """
        Test the welcome page is returned
        """
        url = reverse('welcome')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Welcome')


class TestProjectView(TestCase):
    """
    Test Project View
    """
    def test_project_empty_get(self):
        """
        Test the project page is returned
        """
        url = reverse('project')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Project')

    def test_project_nonempty_get(self):
        """
        Test the project page is returned
        """
        url = reverse('project')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Project')


class TestCookiesView(TestCase):
    """
    Test Cookies View
    """
    def test_cookies_empty_get(self):
        """
        Test the cookies page is returned
        """
        url = reverse('cookies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Cookies')
        self.assertContains(response, 'For information about cookies,')

    def test_cookies_nonempty_get(self):
        """
        Test the cookies page is returned
        """
        url = reverse('cookies')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Cookies')
        self.assertContains(response, 'For information about cookies,')


class TestAccessibilityView(TestCase):
    """
    Test Accessibility View
    """
    def test_accessibility_empty_get(self):
        """
        Test the accessibility page is returned
        """
        url = reverse('accessibility')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Accessibility')

    def test_accessibility_nonempty_get(self):
        """
        Test the accessibility page is returned
        """
        url = reverse('accessibility')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Accessibility')
