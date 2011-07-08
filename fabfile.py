import unittest
from fabric.decorators import task

@task 
def test():
    from armstrong.apps.audio.backends.mutagen.tests import * 
    unittest.main()
