#!/usr/bin/python3
"""Defines unit tests for console.py.

Unit test classes:
    ConsoleCommandTest_Prompt
    ConsoleCommandTest_Help
    ConsoleCommandTest_Exit
    ConsoleCommandTest_Create
    ConsoleCommandTest_Show
    ConsoleCommandTest_All
    ConsoleCommandTest_Destroy
    ConsoleCommandTest_Update
"""
import os
import sys
import unittest
from models import db
from models.engine.disk_storage import DiskStorage
from cli import ConsoleCommand
from io import StringIO
from unittest.mock import patch


class ConsoleCommandTest_Prompt(unittest.TestCase):
    """Unit tests for testing command line interface prompt of the ConsoleCommand."""

    def test_prompt_text(self):
        self.assertEqual("(hbnb) ", ConsoleCommand.prompt)

    def test_no_input(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop(""))
            self.assertEqual("", fake_output.getvalue().strip())


class ConsoleCommandTest_Help(unittest.TestCase):
    """Unit tests for testing help command in ConsoleCommand."""

    def test_help_quit(self):
        help_text = "Exits the application."
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help quit"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_create(self):
        help_text = ("Syntax: create <ModelName>\n"
                     "Creates a new instance of ModelName and prints its id.")
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help create"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_EOF(self):
        help_text = "Exits the application on EOF signal."
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help EOF"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_show(self):
        help_text = ("Syntax: show <ModelName> <id> or <ModelName>.show(<id>)\n"
                     "Displays the string representation of an instance based on the ModelName and id.")
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help show"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_destroy(self):
        help_text = ("Syntax: destroy <ModelName> <id> or <ModelName>.destroy(<id>)\n"
                     "Deletes an instance based on the ModelName and id.")
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help destroy"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_all(self):
        help_text = ("Syntax: all <ModelName> or <ModelName>.all()\n"
                     "Displays all instances of a given ModelName or all instantiated objects if no ModelName is provided.")
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help all"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_count(self):
        help_text = ("Syntax: count <ModelName> or <ModelName>.count()\n"
                     "Retrieves the number of instances of a ModelName.")
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help count"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_update(self):
        help_text = ("Syntax: update <ModelName> <id> <attribute_name> <attribute_value> or"
                     " <ModelName>.update(<id>, <attribute_name>, <attribute_value>) or"
                     " <ModelName>.update(<id>, <dictionary>)\n"
                     "Updates an instance based on the ModelName and id by adding or updating attributes.")
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help update"))
            self.assertEqual(help_text, fake_output.getvalue().strip())

    def test_help_overview(self):
        help_text = ("Documented commands (type help <topic>):\n"
                     "========================================\n"
                     "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertFalse(ConsoleCommand().cmdloop("help"))
            self.assertEqual(help_text, fake_output.getvalue().strip())
