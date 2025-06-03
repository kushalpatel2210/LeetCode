class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        call_stack = []
        curr_time = -1

        for log in logs:
            function_id, operation, timestamp = log.split(":")
            function_id = int(function_id)
            timestamp = int(timestamp)

            if operation == 'start':
                if call_stack:
                    exclusive_times[call_stack[-1]] += timestamp - curr_time
                call_stack.append(function_id)
                curr_time = timestamp
            else:
                in_progress_function_id = call_stack.pop()
                exclusive_times[in_progress_function_id] += timestamp - curr_time + 1
                curr_time = timestamp + 1

        return exclusive_times