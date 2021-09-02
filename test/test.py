# Copyright 2021 David Sanchez-Wells (dvswells@gmail.com)
#
# This file is part of STEPInterpreter.
#
# STEPInterpreter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# STEPInterpreter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with STEPInterpreter.  If not, see <http://www.gnu.org/licenses/>.


import unittest
from classes.STEPFile import STEPFile
import os


# Relative path to test files library are created

Library_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'library')
STEPFile_path = os.path.join(Library_path, 'Part1.stp')
NoSTEPFile_path = os.path.join(Library_path, 'Part2.stp')

# Unittest class begin


class TestFileClass(unittest.TestCase):

    """ Tests for the File Class """

    def test_valid_path_is_passed(self):

        """ Check that a valid path is passed. """

        step = STEPFile()
        self.assertEqual(step.readstep(), "File path is null.")
        self.assertEqual(step.readstep(STEPFile_path), None)
        self.assertEqual(step.readstep('Nothing'), "File does not exist.")

    def test_file_is_step_format(self):

        """ Check that a step file is passed. This check only uses the file header,
            so it does not check that the file is fully STEP-formatted. """

        step = STEPFile()
        self.assertEqual(step.readstep(NoSTEPFile_path), "File is not a valid STEP file.")
        self.assertEqual(step.readstep(STEPFile_path), None)


if __name__ == '__main__':
    unittest.main()
