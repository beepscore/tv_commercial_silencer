#!/usr/bin/env/python3

import unittest
import media_util


class TestMediaUtil(unittest.TestCase):

    def test_duration_seconds_from_media_file(self):
        # use media files from package pydejavu
        filename = './src/pydejavu/mp3/Brad-Sucks--Total-Breakdown.mp3'
        actual = media_util.duration_seconds_from_media_file(filename)
        self.assertAlmostEqual(actual, 138.997, places=2)

