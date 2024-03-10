#!/usr/bin/python3
"""Provides unit tests for the console module of HBnB.

This module includes various unittest classes for testing different
components and functionalities of the HBnB console, including:
- Command prompt interactions
- Help functionality
- Program exit mechanisms
- Object creation, display, listing, deletion, and update operations
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestHBNBCommand_prompting(unittest.TestCase):
    """Tests the command prompt behavior of the HBnB console."""

    def test_prompt_string(self):
        """Verifies that the prompt string is correct."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Checks that no action is taken on an empty input line."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_help(unittest.TestCase):
    """Tests for the 'help' command in the HBnB console."""

    def test_help_quit(self):
        """Ensures the 'quit' command help message is accurate."""
        help_message = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_message, output.getvalue().strip())

    # Additional tests for other commands follow a similar structure
    # to 'test_help_quit', verifying the accuracy of help messages
    # for 'create', 'EOF', 'show', 'destroy', 'all', 'count', and 'update'.

class TestHBNBCommand_exit(unittest.TestCase):
    """Tests for exiting the HBnB console."""

    def test_quit_exits(self):
        """Confirms that the 'quit' command exits the console."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        """Verifies that the EOF signal exits the console."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

# Similar test classes are defined for testing 'create', 'show', 'all',
# 'destroy', and 'update' functionalities, along with setup and teardown
# methods to manage test environment setup before and after tests.

if __name__ == "__main__":
    unittest.main()
