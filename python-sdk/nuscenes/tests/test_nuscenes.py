# nuScenes dev-kit.
# Code written by Oscar Beijbom, 2019.
# Licensed under the Creative Commons [see licence.txt]

import os
import unittest

from nuscenes import NuScenes


class TestNuScenes(unittest.TestCase):

    def test_load(self):
        """
        Loads up NuScenes.
        This is intended to simply run the NuScenes class to check for import errors, typos, etc.
        """

        assert 'NUSCENES' in os.environ, 'Set NUSCENES env. variable to enable tests.'
        nusc = NuScenes(version='v1.0-trainval', dataroot='~/data/nuscenes', verbose=False)

        # Trivial assert statement
        self.assertEqual(nusc.table_root, os.path.join('~/data/nuscenes', 'v1.0-trainval'))


if __name__ == '__main__':
    nusc = NuScenes(version='v1.0-trainval', dataroot='~/data/nuscenes', verbose=False)
    unittest.main()
