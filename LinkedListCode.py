
class Node(object): #More of Classes and Objects>>Please refer to https://www.w3schools.com/python/python_classes.asp

	def __init__(self, data): # This class node represents a single linkedlist
		self.data = data; # 'data' represent the actual data to be stored in the list
		self.nextNode = None; # .nextNode represent the link to next node in the linkedlist
		
class LinkedList(object):
#use the __init__ to reference the first node of the linkedlist; 
	def __init__(self): 
		self.head = None; # At the beginning it is None, because it is empty list
		self.size = 0; # No items in the linkedlist
		
	# O(1) !!! Can you guess why we like LinkedLists? :)	
	def insertStart(self, data): # To insert data into the LinkedList
	
		self.size = self.size + 1;
		newNode = Node(data);
		
		if not self.head:
			self.head = newNode;
		else:
			newNode.nextNode = self.head; #Update the reference
			self.head = newNode;
			
	def remove(self, data): # To remove data from the LinkedList
	
		if self.head is None:
			return;
			
		self.size = self.size - 1;
		
		currentNode = self.head;
		previousNode = None;
		
		while currentNode.data != data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;
			
		if previousNode is None:
			self.head = currentNode.nextNode;
		else:
			previousNode.nextNode = currentNode.nextNode;			
		
	# O(1)	
	def size1(self):
		return self.size;
		
	# O(N) not good !!!	
	def size2(self):
		
		actualNode = self.head;
		size = 0;
		
		while actualNode is not None:
			size+=1;
			actualNode = actualNode.nextNode;
			
		return size;
		
	# O(N) Linear running time because we have to move through all nodes till we find 
	#the last nodewhich is pointing to Null (None)
	def insertEnd(self, data): # To insert a node at the end of the LinkedList
	
		self.size = self.size + 1;
		newNode = Node(data);
		actualNode = self.head;
		
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode; #Find the last node in the LinkedList
			
		actualNode.nextNode = newNode; # insert a new node accordingly
		
	def traverseList(self):
	
		actualNode = self.head;
		
		while actualNode is not None:
			print("%d " % actualNode.data);
			actualNode = actualNode.nextNode;


			
linkedlist = LinkedList();

linkedlist.insertStart(12);
linkedlist.insertStart(122);
linkedlist.insertStart(3);
linkedlist.insertEnd(31);

linkedlist.traverseList();

linkedlist.remove(3);
linkedlist.remove(12);
linkedlist.remove(122);
linkedlist.remove(31);

print(linkedlist.size1());



