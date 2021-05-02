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


class TestAboutProjectView(TestCase):
    """
    Test About: Project View
    """
    def test_about_project_get(self):
        """
        Test the project: about page is returned
        """
        url = reverse('about-project')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Project')


class TestAboutDatabaseView(TestCase):
    """
    Test About: Database View
    """
    def test_about_database_get(self):
        """
        Test the database: about page is returned
        """
        url = reverse('about-database')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Database')


class TestAboutTeamView(TestCase):
    """
    Test About: Team View
    """
    def test_about_team_get(self):
        """
        Test the project: team page is returned
        """
        url = reverse('about-team')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'John Lowe')


class TestAboutFundingView(TestCase):
    """
    Test About: Funding View
    """
    def test_about_funding_get(self):
        """
        Test the project: funding page is returned
        """
        url = reverse('about-funding')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Funding')


class TestAboutEventsView(TestCase):
    """
    Test About: Events View
    """
    def test_about_events_get(self):
        """
        Test the project: events page is returned
        """
        url = reverse('about-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Events')


class TestAboutOutputsView(TestCase):
    """
    Test About: Outputs View
    """
    def test_about_outputs_get(self):
        """
        Test the project: outputs page is returned
        """
        url = reverse('about-outputs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Outputs')


class TestHelpView(TestCase):
    """
    Test Help View
    """
    def test_help_get(self):
        """
        Test the help page is returned
        """
        url = reverse('help')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'LINGUINDIC')
        self.assertContains(response, 'Help')
        self.assertContains(response, 'currently under development')


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
