#student name:
#student number:

from multiprocessing.dummy import Array
import threading

def sortingWorker(firstHalf: bool) -> None:
    global sortedFirstHalf
    global sortedSecondHalf

    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    #bubble sort algorithm which iteratively checks to see if two adjacent elements are larger than each other 
    def bubbleSort(list):
        for i in range(len(list)-1): #iterate for every element
            for j in range(len(list)-i-1): 
                if list[j]>list[j+1]:
                    list[j+1],list[j] = list[j],list[j+1] #if second is smaller, swap both elements
        return list

    if (firstHalf):
        sortedFirstHalf = bubbleSort(testcase[0:len(testcase)//2]) #sorting first half
    else:
        sortedSecondHalf = bubbleSort(testcase[len(testcase)//2:len(testcase)]) #sorting second half


def mergingWorker() -> None:
    global SortedFullList

    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    #bubble sort 
    def bubbleSort(list):
        for i in range(len(list)-1): #iterate for every element
            for j in range(len(list)-i-1): 
                if list[j]>list[j+1]:
                    list[j+1],list[j] = list[j],list[j+1] #if second is smaller, swap both elements
        return list

    unsortedFullList = sortedFirstHalf + sortedSecondHalf 
    SortedFullList = bubbleSort(unsortedFullList) 

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,10,-3,3,2,9,22]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    thread0 = threading.Thread(target = sortingWorker, args = (True,))
    thread1 = threading.Thread(target = sortingWorker, args = (False,))
    thread2 = threading.Thread(target = mergingWorker)

    thread0.start()    
    thread1.start()

    thread0.join()    
    thread1.join()
    
    thread2.start()
    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)
    thread2.join()
    


