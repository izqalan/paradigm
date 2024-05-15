import unittest
from unittest.mock import Mock
import a189289_a189310_a186277_LT4 as lt4  # import your module

# unittest saja-saja
# to run: python -m unittest

class TestDrawFunctions(unittest.TestCase):
  def setUp(self):
    self.mock_turtle = Mock()

  def test_drawTriangle(self):
    lt4.drawTriangle(self.mock_turtle, 0, 0, 100, "black", "white", "up")
    # Check if the methods were called with the correct arguments
    self.mock_turtle.pencolor.assert_called_with("black")
    self.mock_turtle.fillcolor.assert_called_with("white")
    self.mock_turtle.goto.assert_called()  # Add specific arguments if necessary
    self.mock_turtle.begin_fill.assert_called()
    self.mock_turtle.end_fill.assert_called()

  def test_drawRectangle(self):
    lt4.drawRectangle(self.mock_turtle, 0, 0, 100, 200, "black", "white")
    # Check if the methods were called with the correct arguments
    self.mock_turtle.pencolor.assert_called_with("black")
    self.mock_turtle.fillcolor.assert_called_with("white")
    self.mock_turtle.goto.assert_called()  # Add specific arguments if necessary
    self.mock_turtle.begin_fill.assert_called()
    self.mock_turtle.end_fill.assert_called()

if __name__ == '__main__':
  unittest.main()