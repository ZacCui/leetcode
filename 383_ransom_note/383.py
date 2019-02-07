'''
	Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

	Each letter in the magazine string can only be used once in your ransom note.

	Note:
	You may assume that both strings contain only lowercase letters.

	canConstruct("a", "b") -> false
	canConstruct("aa", "ab") -> false
	canConstruct("aa", "aab") -> true
'''

class Solution:
	def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
		if not ransomNote:
			return True
		dic = {}
		for char in ransomNote:
			if char in dic:
				dic[char] += 1
			else:
				dic[char] = 1
		remainingWord = len(ransomNote)
		for char in magazine:
			if char in dic and dic[char] > 0:
				dic[char] -= 1
				remainingWord -= 1
				if not remainingWord:
					return True
		return False