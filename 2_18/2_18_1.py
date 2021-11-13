import unittest
from .tv_controller import TvController
CHANNELS = ["BBC", "Discovery", "TV1000"]


class TestTvController(unittest.TestCase):
    def setUp(self):
        self.tv_controller = TvController(CHANNELS)

    def test_first_channel(self):
        self.assertEqual(self.tv_controller.first_channel(), "BBC")

    def test_last_channel(self):
        self.assertEqual(self.tv_controller.last_channel(), "TV1000")

    def test_turn_channel(self):
        for i in range(len(CHANNELS)):
            self.assertEqual(self.tv_controller.turn_channel(i+1), CHANNELS[i])

    def test_next_channel(self):
        self.tv_controller.channel_id = 0          
        self.tv_controller.channel = "BBC"         
        self.assertEqual(self.tv_controller.next_channel(), "Discovery")

    def test_next_channel_last(self):
        self.tv_controller.channel_id = 2
        self.tv_controller.channel = "TV1000"
        self.assertEqual(self.tv_controller.next_channel(), "BBC")

    def test_previous_channel(self):
        self.tv_controller.channel_id = 1
        self.tv_controller.channel = "Discovery"
        self.assertEqual(self.tv_controller.previous_channel(), "BBC")

    def test_previous_channel_first(self):
        self.tv_controller.channel_id = 0
        self.tv_controller.channel = "BBC"
        self.assertEqual(self.tv_controller.previous_channel(), "TV1000")

