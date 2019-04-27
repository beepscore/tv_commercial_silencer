#!/usr/bin/env/python3

import unittest
import media_util
import os


class TestMediaUtil(unittest.TestCase):

    def test_duration_seconds_from_media_file(self):
        # use media files from package pydejavu

        filename1 = './src/pydejavu/mp3/Brad-Sucks--Total-Breakdown.mp3'
        actual = media_util.duration_seconds_from_media_file(filename1)
        self.assertAlmostEqual(actual, 138.997, places=2)

        filename2 = './src/pydejavu/mp3/The-Lights-Galaxia--While-She-Sleeps.mp3'
        actual = media_util.duration_seconds_from_media_file(filename2)
        self.assertAlmostEqual(actual, 248.036, places=2)

    def test_media_durations_second_dict_keys_dont_end_with_mp3(self):
        indirname = './src/pydejavu/mp3'
        media_dict_filename = './data/media_durations_test.json'
        # write media dictionary
        media_util.write_media_file_durations(indirname, media_dict_filename)
        media_duration_dict = media_util.media_durations_second_dict(media_dict_filename)
        self.assertIsNone(media_duration_dict.get('Brad-Sucks--Total-Breakdown.mp3'))
        self.assertIsNotNone(media_duration_dict.get('Brad-Sucks--Total-Breakdown'))
        # clean up
        os.remove(media_dict_filename)

    def test_media_durations_second_dict(self):
        indirname = './src/pydejavu/mp3'
        media_dict_filename = './data/media_durations_test.json'
        # write media dictionary
        media_util.write_media_file_durations(indirname, media_dict_filename)
        media_duration_dict = media_util.media_durations_second_dict(media_dict_filename)
        self.assertEqual(len(media_duration_dict), 5)
        self.assertAlmostEqual(media_duration_dict.get('Brad-Sucks--Total-Breakdown'),
                               138.997, places=2)
        self.assertAlmostEqual(media_duration_dict.get('The-Lights-Galaxia--While-She-Sleeps'),
                               248.036, places=2)
        # clean up
        os.remove(media_dict_filename)


