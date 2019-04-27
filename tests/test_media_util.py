#!/usr/bin/env/python3

import unittest
import media_util


class TestMediaUtil(unittest.TestCase):

    def test_duration_seconds_from_media_file(self):
        # use media files from package pydejavu

        filename1 = './src/pydejavu/mp3/Brad-Sucks--Total-Breakdown.mp3'
        actual = media_util.duration_seconds_from_media_file(filename1)
        self.assertAlmostEqual(actual, 138.997, places=2)

        filename2 = './src/pydejavu/mp3/The-Lights-Galaxia--While-She-Sleeps.mp3'
        actual = media_util.duration_seconds_from_media_file(filename2)
        self.assertAlmostEqual(actual, 248.036, places=2)

