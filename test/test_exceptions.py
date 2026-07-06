#!/usr/bin/env python
#
# This file is part of pySerial - Cross platform serial port support for Python
# (C) 2026
#
# SPDX-License-Identifier:    BSD-3-Clause
"""\
Tests for the serial module exceptions.
"""

import pickle
import unittest
import serial


class Test_exceptions(unittest.TestCase):
    """Test serial module exceptions"""

    def test_port_not_open_error_default_message(self):
        err = serial.PortNotOpenError()
        self.assertEqual(str(err), 'Attempting to use a port that is not open')

    def test_port_not_open_error_custom_message(self):
        err = serial.PortNotOpenError('custom message')
        self.assertEqual(str(err), 'custom message')

    def test_port_not_open_error_pickle(self):
        err = serial.PortNotOpenError()
        restored = pickle.loads(pickle.dumps(err))
        self.assertEqual(str(restored), str(err))
        self.assertIsInstance(restored, serial.PortNotOpenError)


if __name__ == '__main__':
    import sys
    sys.stdout.write(__doc__)
    sys.argv[1:] = ['-v']
    # When this module is executed from the command-line, it runs all its tests
    unittest.main()
