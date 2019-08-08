"""Test suite """
import requests

class TestClass(object):

    def test_main_page(self):
        """Checks status code and response text in mainpage """
        response = requests.get('http://localhost:5000/')
        assert response.status_code == 200
        assert "Welcome to Piggybank" in response.text

    def test_registration_page(self):
        """Checks status code and response text in registration page """
        response = requests.get('http://localhost:5000/register')
        assert response.status_code == 200
        assert "Register to begin investing" in response.text

    def test_login_page(self):
        """Checks status code and response text in login page """
        response = requests.get('http://localhost:5000/login')
        assert response.status_code == 200
        assert "Login to view portfolio" in response.text

    def test_balance_api_access(self):
        """Checks status code and response text for balance api endpoint """
        response = requests.get('http://localhost:5000/api/balance/me')
        assert response.status_code == 401
        assert response.json()["response"] == "Unauthenticated. Please log in"

    def test_transaction_api_access(self):
        """Checks status code and response text for transaction api endpoint """
        response = requests.get('http://localhost:5000/api/transaction/me')
        assert response.status_code == 401
        assert response.json()["response"] == "Unauthenticated. Please log in"

    def test_portfolio_api_access(self):
        """Checks status code and response text for portfolio api endpoint """
        response = requests.get('http://localhost:5000/api/portfolio/me')
        assert response.status_code == 401
        assert response.json()["response"] == "Unauthenticated. Please log in"