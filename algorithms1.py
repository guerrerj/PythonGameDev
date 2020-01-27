""" 
    Algorithm Complexity: 
        Space complexity - How much memory does it require?
        Time complexity - How much time does it take to complete?
        
    Set of input values it works on and produces the output. 
    Classification:
        Serial/Parallel
        Exact/Approximate - known predictable value or not
        Deterministic/non-deterministic - each step with exact decision or using successive guesses
                
    Search Algorithms:
        Finds specific data in a structure
        
    Sorting Algorithms:
    
    Computational Algorithms: 
        Calculating another set of data
        
    Collection Algorithms: 
        Working with collection of data
        
"""

# Euclid's Algorithm: Find the greates common factor/denominator(GCD)
#     of two integers
#     For two integers, a and b, where a> b divide a by b.
#     If the remainder r is 0 then stop. GCD is b
#     otherwise, set a to b and b to r, and repeat step 1 until r is 0

def gcd(a, b):
    while (b != 0):
        t = a
        a = b 
        b = t % b
    return a 

print(gcd(60,96)) # should be 12
print(gcd(20,8)) # should 4 


""" Understanding Algorithm Performance 
    How does algorithm responds to dataset size  as input grows
    Big-O notation - (order of operation)  - time scale to perform operation
    
    Many algorithms have different big O terms
    
    O(1) - constant time - looking up a single element in an array (doesnt depend on number of elements)
    O(log n) - logarithmic - finding an item in a sorted array with a binary search
    O(n) -  linear time - searching an unsorted array for a specific value
    O (n log n) - log linear - complex sorting algorithms like heap sort and merge sort
    O(n2) - Quadratic - simple sorting algorithms, such as bubble sort, selection sort, 
      
    Data Structures - organize information so that it can be processed. 
        Arrays
            Collection of elements identified by index or key
            Can be accessed random access function( no need to navigate structure)
            Multiple dimensions 
            Calculate item index O(1) - independent of size
            Insert or Delete item at beginning/ middle O(n) - must be moved
            at end - O(1)
            
            
        Linked Lists
            collection of data element called nodes
            contain reference to the next node in the list
            hold whatever data the application needs 
            Doubly linked list - points to both
            
            Elements can be easily inserted and removed
            underlying memory doesnt need to be reorganized
            can't do constant-time random item access
            Item lookup is linear in time complexity O(n) 
            
            
        Stacks and Queues
        Trees 
        Hash Tables    
        
    
 """
 
 # class for node for linked list
class Node(object):
    def __init__(self, val):
         self.val = val
         self.next = None
    def getData(self):
        return self.val 
    
    def setData(self, val):
        self.val = val 
    
    def getNext(self):
        return self.next  
    
    def setNext(self, next):
        self.next = next 
        
class LinkedList(object):
    def __init(self, head=None):
        self.head = head
        self.count = 0
        
    def getCount(self):
        return self.count 
    
    def insert(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
        self.count += 1
        
    def find(self, val):
        item = self.head 
        while (item != None):
            if item.getData()  == val:
                return item
            else:
                item = item.getNext()
        
        return None
    
    def deleteAt(self, idx):
        if idx > self.count - 1:
            return 
        if idx == 0:
            self.head = self.head.getNext() 
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.getNext()
                tempIdx += 1
            node.setNext(node.getNext().getNext())
            self.count -= 1 
        
    def dumpList(self):
        tempNode = self.head
        while(tempNode != None):
            print("Node: " , tempNode.getData())
            tempNode = tempNode.getNext()
        
itemList = LinkedList()
itemList.insert(30)
itemList.insert(23)
itemList.insert(2)
itemList.insert(599)
itemList.insert(43)
 
"""
    Stack is a collection that support push and pop operations
    The last item pushed is the first one popped
    Constant time operation
    
    Queues - collection that supports adding and removing 
    first item added is the first item out
    enqueue() dequeu() 
    
    Practical applications 
        stack - Expression processing  backtracking: browser backstack
        Queue - order processing, messaging, 
        
    Dictionaries(Hash Tables) 
       Associative arrays - maps  keys to values 
       Uses a hash function - assign key to unique slot
       two keys might have same value 
       Key to value mappings are unique
       Hash tables are typically very fast
       Small datasets, arrays are usually more efficient 
       Entries are not ordered. 
       Can grow or shrink to fit data that is needed 
       
       
"""
items1 = dict({"key1" : 1, "key2": 2})


"""
    Recursion - function that calls itself 
    Recursive functions need to have a breaking condition
    This prevents infinite loops and eventual crashes
    Each time function is called, old arguments are saved 
    Call stack    
"""

def countDown(x):
    if x == 0:
        print("Done")
        return
    else:
        print(x, "... ")
        countDown(x-1)
        print("Call stack is unwound")
        
countDown(10)

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr - 1)
    
def factorial(num):
    pass 

"""
    Sorting Data - 
    The Bubble Sort - 
        compares two elements and if larger the elements are swapped
        is simple to understand and implement 
        Performance O(n2)
        for loops inside for loops is usually n2
        not considered a practical way of sorting data  
        
        
    Merge Sort - divide and conquer algorithm
        breaks a dataset into individual pieces and merges them
        uses recursion to operate on data sets
        performs well on large sets of data 
        performance in general O (nlogn) 
        
        break array down until have one element arrays. 
        rebuild back original array with sorted elements
        
"""

def mergeSort(dataset):    
    if len(dataset) > 1:
        mid = len(dataset)/2 
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        
        mergeSort(leftarr)
        mergeSort(rightarr)
        
        i,j,k = 0
        
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i+=1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1 
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
            
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

"""
    QuickSort - divide and conquer algorithm like merge sort
        also uses recursion to perform sorting
        generally performs better than merge sort O(nlogn)
        operates in place on the data
        worst case is O(n2) when data is mostly sorted already 
        Main features - pivot point selection
            pick a pivot position 
            partition list to split 
            where two indices cross each other you split the array
            continue splitting the arrays until 
            all the work is done in partition step 
"""

def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)
        
        # now sort the two partitions
        quickSort(dataset, first, pivotIdx - 1)
        quickSort(dataset, pivotIdx + 1, last)
def parition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotValue = datavalues[first]
    
    # establish the upper and lower indexes
    lower = first + 1
    upper = last
    
    # start searching for the crossing point
    done = false
    while not done:
        while lower <= upper and datavalues[lower] <= pivotValue:
            lower += 1
            
        while datavalues[upper] >= pivotValue and upper>= lower:
            upper -= 1 
        
        if upper < lower: 
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
            
    # when the split point is found, exchange the pivot value with upper 
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp
    
    return upper 
        
""" 
    Searching for data 
    Unordered data: 
    O(n) - average search time increases by the number of items added
    
    Ordered/sorted data: 
        can perform binary search 
        two indices at beginning and end of list
        find middle index value rounded to bottom 
        Log(n) 
        
        whether to keep the data ordered or not 
        inefficient and slower may be better choice because
        might be more expensive to keep data ordered 
        
        return all(itemList[i] <= itemList[i+1] for i in range(len(itemList)-1) 
        // returns true if the condition holds for all the values
        // else it returns false 
        
        
"""

def binarySearch(item, itemList):
    listsize = len(itemList) - 1 
    
    lowerIdx = 0
    upperIdx = listsize
    
    while lowerIdx <= upperIdx:
        
        midPt = (lowerIdx + upperIdx) 
        
        if itemList[midPt] == item:
            return midPt
        
        if item  > itemList[midPt]:
            lowerIdx = midPt + 1 
        else:
            upperIdx = midPt - 1 
    if lowerIdx > upperIdx:
        return None
    
    
""" Remove duplicates - can use hash table 
    extract keys which will be unique
    
    result.set(filter.keys()) 
    Uses O(n) 
    
    Value counting with HashTable
    o(n) 
    
    Finding maximum value with recursion     
"""