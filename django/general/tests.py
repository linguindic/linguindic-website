from django.test import TestCase
from django.urls import reverse


class TestWelcomeView(TestCase):
    """
    Test Welcome View
    """
    def test_welcome_get(self):
        """
        Test the welcome page is returned
        """
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Welcome')


class TestProjectAboutView(TestCase):
    """
    Test Project: About View
    """
    def test_project_about_get(self):
        """
        Test the project: about page is returned
        """
        url = reverse('project-about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'About')


class TestProjectTeamView(TestCase):
    """
    Test Project: Team View
    """
    def test_project_team_get(self):
        """
        Test the project: team page is returned
        """
        url = reverse('project-team')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Team')


class TestProjectFundingView(TestCase):
    """
    Test Project: Funding View
    """
    def test_project_funding_get(self):
        """
        Test the project: funding page is returned
        """
        url = reverse('project-funding')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Funding')


class TestProjectEventsView(TestCase):
    """
    Test Project: Events View
    """
    def test_project_events_get(self):
        """
        Test the project: events page is returned
        """
        url = reverse('project-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Events')


class TestProjectOutputsView(TestCase):
    """
    Test Project: Outputs View
    """
    def test_project_outputs_get(self):
        """
        Test the project: outputs page is returned
        """
        url = reverse('project-outputs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Outputs')


class TestCookiesView(TestCase):
    """
    Test Cookies View
    """
    def test_cookies_get(self):
        """
        Test the cookies page is returned
        """
        url = reverse('cookies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Cookies')
        self.assertContains(response, 'For information about cookies,')


class TestAccessibilityView(TestCase):
    """
    Test Accessibility View
    """
    def test_accessibility_get(self):
        """
        Test the accessibility page is returned
        """
        url = reverse('accessibility')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Accessibility')
