class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - 65] += 1

        most_frequent = max(counts) # count of most frequent task

        max_num = 0 #num tasks with count most_frequent 
        for count in counts:
            if count == most_frequent:
                max_num += 1


        return max(  (max_num) + ((most_frequent - 1) * (n + 1)) , len(tasks))