class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        max_num = num_str
        for d in num_str:
            if d != '9':
                max_num = max_num.replace(d, '9')
                break
        
        min_num = num_str
        # if first digit is non '1'
        if min_num[0] != '1':
            min_num = min_num.replace(num_str[0], '1')
        else:
            # first digit is 1 so find the next occurence of digit that is non 1 or 0 and 
            # replace it with 0
            for d in num_str[1:]:
                if d not in '01':
                    min_num = min_num.replace(d, '0')
                    break
        
        return int(max_num) - int(min_num)
