import heapq

arr =[]
heapq.heappush(arr, 10)
heapq.heappush(arr, 3)
heapq.heappush(arr, 1)
heapq.heappush(arr,4)



while arr:
    print(heapq.heappop(arr))

#순서를 바꾸기 : 튜플 이용 

arr = [10,2,3,7,5,9]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))