from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:    

        def check(x):
            task_index = 0
            workers_under_strength = deque()
            remaining_pills = pills

            # only loop through last workers as they have highest strength as array is sorted
            for worker_index in range(num_workers - x, num_workers):
                while task_index < x and tasks[task_index] <= workers[worker_index] + strength:
                    workers_under_strength.append(tasks[task_index])
                    task_index += 1
            
                if not workers_under_strength:
                    return False
                
                # without pill
                if workers_under_strength[0] <= workers[worker_index]:
                    workers_under_strength.popleft()
                elif remaining_pills == 0:
                    return False
                # give the worker the hardest task
                else:
                    remaining_pills -= 1 
                    workers_under_strength.pop()
            
            return True

        num_tasks, num_workers = len(tasks), len(workers) 
        tasks.sort()
        workers.sort()
        left, right = 0, min(num_tasks, num_workers)
        res = None
        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res