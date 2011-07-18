import unittest
from fabric.decorators import *
from armstrong.apps.audio.backends.mutagen.tests import MutagenTestCase

@task 
def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(MutagenTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
