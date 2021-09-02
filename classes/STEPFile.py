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


class STEPFile:
    """
    A class to represent a STEP file.

    Attributes
    ----------
    path : str
        absolute path of the STEP file
    content : str
        content of the STEP file (plain text)

    Methods
    -------
    readstep(filepath=""):
        Reads a STEP file and updates

    """

    def __init__(self):
        STEPFile._path = ""
        STEPFile._content = ""

    def readstep(self, filepath=""):
        """
        readstep(file)

        Updates the File class path and content.

        Parameters
        ----------

        filepath : str
              Absolute path of the input file.

        Returns
        -------
        out : str
            "STEP file read process has ended."
        """

        if filepath == "":
            return "File path is null."

        STEPFile._path = filepath

        try:
            opened_file = open(STEPFile._path, 'r')
        except FileNotFoundError:
            return "File does not exist."

        if 'ISO-10303-21' not in opened_file.readline():
            return "File is not a valid STEP file."

        STEPFile._content = opened_file.read()

        opened_file.close()

        return "STEP file read process has ended."
