class Solution:
	def __init__(self):
		self.keyboard = {
			1 : 'qwertyuiop',
			2 : 'asdfghjkl',
			3 : 'zxcvbnm'
		}
	def findWords(self, words: 'List[str]') -> 'List[str]':
		result = []
		for word in words:
			if (self.checkInOneRow(word)):
				result.append(word)
		return result

	def checkInOneRow(self, word):
		row = 1
		for i in self.keyboard:
			if word[0].lower() in self.keyboard[i]:
				row = i
				break
		for char in word:
			if char.lower() not in self.keyboard[row]:
				return False
		return True