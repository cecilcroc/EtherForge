# test_etherforge.py
"""
Tests for EtherForge module.
"""

import unittest
from etherforge import EtherForge

class TestEtherForge(unittest.TestCase):
    """Test cases for EtherForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherForge()
        self.assertIsInstance(instance, EtherForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
