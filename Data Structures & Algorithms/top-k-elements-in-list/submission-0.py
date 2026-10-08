class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        sort_dic = {k: v for k,v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        new_list = []
        
        for i in sort_dic:
            if len(new_list) < k:
                new_list.append(i)

        return new_list