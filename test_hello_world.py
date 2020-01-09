import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):
  def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True
  def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
  def test_greeting_message(self):
    response = self.app.get('/')
    greet = hello_world.wrap_html('Welcome to CI/CD')
    self.assertEqual(response.data, greet)
if __name__ == '__main__':
  unittest.main()
