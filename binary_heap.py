class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):

        while i // 2 > 0:

            if self.heapList[i] < self.heapList[i // 2]:


                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):

        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):

        # while we are not at the end of the list/tree
        while (i * 2) <= self.currentSize:

            mc = self.minChild(i) # either 'right' or 'left' child has lowest value

            # if child has lowest value, then switch
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp

            i = mc # start search again

    def minChild(self,i):

        # if 'right' child does not exist ==> index is greater than size of heap, then use 'left' child
        if i * 2 + 1 > self.currentSize:
            return i * 2

        # 'right' child exist
        else:
            # compare 'left' and 'right' child values; return index of lowest value
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1] # root is our lowest value element
        self.heapList[1] = self.heapList[self.currentSize] # root is assigned as size of heap ???
        self.currentSize = self.currentSize - 1 # decrement the size
        self.heapList.pop() # remove last element ???
        self.percDown(1) # bubble down root element
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
