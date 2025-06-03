class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        call_stack = []
        last_recorded_time = -1

        for log in logs:
            function_id, operation, timestamp = log.split(":")
            function_id = int(function_id)
            timestamp = int(timestamp)

            if operation == 'start':
                if call_stack:
                    exclusive_times[call_stack[-1]] += timestamp - last_recorded_time
                call_stack.append(function_id)
                last_recorded_time = timestamp
            else:
                in_progress_function_id = call_stack.pop()
                exclusive_times[in_progress_function_id] += timestamp - last_recorded_time + 1
                last_recorded_time = timestamp + 1

        return exclusive_times