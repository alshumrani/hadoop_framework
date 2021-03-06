# /*
#    Copyright 2011, Lightbox Technologies, Inc
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
# */

import shellLinkParser
import unittest

class testgetShowCommand(unittest.TestCase):
  """
  getShowCommand requires input of a 32-bit unsigned int
  ShowCommand has three known values: 0x00000001, 0x00000003, 0x00000007
  """
	knownValues = ((1, 'SW_SHOWNORMAL'),
					(3, 'SW_SHOWMAXIMIZED'),
					(7, 'SW_SHOWMINNOACTIVE'))
					
	UnknownValues = ((0, 'SW_SHOWNORMAL'),
					(2, 'SW_SHOWNORMAL'),
					(4, 'SW_SHOWNORMAL'),
					(5, 'SW_SHOWNORMAL'),
					(6, 'SW_SHOWNORMAL'),
					(8, 'SW_SHOWNORMAL'),
					(10, 'SW_SHOWNORMAL'),
					(78, 'SW_SHOWNORMAL'),
					(285, 'SW_SHOWNORMAL'),
					(1263, 'SW_SHOWNORMAL'),
					(4093, 'SW_SHOWNORMAL'),
					(11758, 'SW_SHOWNORMAL'),
					(31970, 'SW_SHOWNORMAL'))

	def testKnownValues(self):
		"""getShowCommand should give known result with known input"""
		for value, name in self.knownValues:
			result = shellLinkParser.getShowCommand(value)
			self.assertEqual(name, result)
			
	def testUnknownValues(self):
		"""getShowCommand MUST return SW_SHOWNORMAL with anything other than known values"""
		for value, name in self.randomValues:
			result = shellLinkParser.getShowCommand(value)
			self.assertEqual('SW_SHOWNORMAL', result)
			
  def testTooLarge(self):                                          
      """getShowCommand should fail with larger than 32-bit number"""
      self.assertRaises(shellLinkParser.OutOfRangeError, shellLinkParser.getShowCommand, 4294967296)
      
  def testNegative(self):                                          
      """getShowCommand should fail with a negative number"""
      self.assertRaises(shellLinkParser.OutOfRangeError, shellLinkParser.getShowCommand, -1)
		
	def testgetShowCommandCase(self):
		"""getShowCommand should always return uppercase"""
		for value in (1, 3, 7):
			name = shellLinkParser.getShowCommand(value)
			self.assertEqual(name, name.upper())

if __name__ == "__main__":
	unittest.main()
