import os
import sys
import shutil
sys.path.append('.')
import unittest
from unittest import mock

from  data_mock.google.cloud import storage as mock_storage

from sync_composer import sync_composer as sync_composer

CONTENT1= 'mock-contents'

class Mock1(mock_storage.Client):

    def register_initial_mock_data(self):
        self.register_mock_data(blob_name = 'blob1', 
                bucket_name = 'mock-bucket', contents = CONTENT1 )

@mock.patch('google.cloud.storage.Client', side_effect= Mock1 )
def test_not_sure(m1):
    sync_composer.sync_bucket(
        bucket_name = 'mock', 
        project = 'mock', 
        ignore_path= None, 
        verbosity = 3)


