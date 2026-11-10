import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash map để count {num1: count1, num2: count2,...}
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Min Heap lấy giá trị count(freq) và num để push vào heap và pop giá trị min khi vượt top k
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Lấy kết quả từ heap
        res = []
        for i in range(k):
            # item pop ra tuple chứa (freq, num)
            item = heapq.heappop(min_heap)
            # item[1] sẽ lấy phần tử num từ tuple ra
            res.append(item[1])
        return res