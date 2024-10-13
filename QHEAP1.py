# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

heap = []
elements_set = set()

Q = int(input().strip())

for _ in range(Q):
    query = input().strip().split()
    
    if query[0] == '1':
        x = int(query[1])
        heapq.heappush(heap, x)
        elements_set.add(x)
        
    elif query[0] == '2':
        x = int(query[1])
        elements_set.remove(x)
        
    elif query[0] == '3':
        while heap[0] not in elements_set:
            heapq.heappop(heap)
        print(heap[0])