class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        call_stack = []
        prev_rec_time = -1

        for log in logs:
            f_id, op, ts = log.split(":")
            f_id = int(f_id)
            ts = int(ts)

            if op == "start":
                if call_stack:
                    exclusive_times[call_stack[-1]] += ts - prev_rec_time
                call_stack.append(f_id)
                prev_rec_time = ts
            else:
                prev_f_id = call_stack.pop()
                exclusive_times[prev_f_id] += ts - prev_rec_time + 1
                prev_rec_time = ts + 1
        
        return exclusive_times