#!/usr/bin/env/python3

import unittest
import recognize_audio


class TestRecognizeAudio(unittest.TestCase):

    def test_time_remaining_seconds(self):
        duration_seconds = 60.0
        offset_seconds = 12.0
        sample_window_seconds = 5
        actual = recognize_audio.time_remaining_seconds(duration_seconds, offset_seconds, sample_window_seconds)
        self.assertAlmostEqual(actual, 43.0, places=2)

