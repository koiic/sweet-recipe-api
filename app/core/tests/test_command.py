from unittest.mock import patch

from django.test import TestCase
from django.core.management import call_command
from django.db.utils import OperationalError


class CommandTest(TestCase):

    def test_wait_for_db_ready_succeds(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait for db')
            self.assertEqual(gi.call_count, 1)


    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """testing wait for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
