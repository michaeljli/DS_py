class TreeNode:
	def __init__(self, key, val, left = None, right = None, parent = None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.leftChild or self.rightChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothChildren(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self, key, val, left, right):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self