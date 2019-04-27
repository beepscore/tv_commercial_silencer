#!/usr/bin/env/python3

import unittest
import tv_service


class TestTvService(unittest.TestCase):

    def test_command_url_volume_decrease_increase(self):
        expected = 'http://10.0.0.4:5000/api/v1/tv/volume-decrease-increase/'
        actual = tv_service.command_url(tv_service.TVCommand.volume_decrease_increase)
        self.assertEqual(actual, expected)

