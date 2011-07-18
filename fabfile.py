import unittest
from armstrong.dev.tasks import *
from armstrong.apps.audio.backends.mutagen.tests import MutagenTestCase

test_suite = unittest.TestLoader().loadTestsFromTestCase(MutagenTestCase)
