import heapq

heap = []

heapq.heappush(heap,2) #tambah node
heapq.heappush(heap,2)
heapq.heappush(heap,3)
heapq.heappush(heap,2)
heapq.heappush(heap,2)

print(heap)
print(f"item pertama : {heap[0]}")
print(heapq.heappushpop(heap, 3))	#Tambah lalu ambil minimum
print(heap)
heapq.heappop(heap) #hapus elemen minimum
print(heap)