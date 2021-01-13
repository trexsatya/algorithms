
# https://practice.geeksforgeeks.org/problems/stepping-numberswrong-output1813/1

class Solution:
    def next_stepping_number(self, num, dig, pos_dig, min_num, max_num, step_numbers):
        # print(num, dig,  pos_dig)
        if pos_dig == 0:
            if min_num <= num + dig <= max_num:
                # print(num + dig)
                step_numbers.add(num + dig)
            return
        if dig < 9:
            self.next_stepping_number(num + dig*(10**pos_dig), dig+1, pos_dig-1, min_num, max_num, step_numbers)

        if dig > 0:
            self.next_stepping_number(num + dig*(10**pos_dig), dig-1, pos_dig-1, min_num, max_num, step_numbers)

    def num_digs(self, x):
        if x == 0:
            return 1
        num = 0
        while x:
            x = x // 10
            num += 1
        return num


    def stepping_numbers_for_x_digits(self, num_digs, min_num, max_num, step_numbers):
        for i in range(0, 10):
            self.next_stepping_number(0, i, num_digs-1, min_num, max_num, step_numbers)

    def steppingNumbers (self, n, m):
        step_numbers = set()
        for i in range(self.num_digs(n), self.num_digs(m)+1):
            self.stepping_numbers_for_x_digits(i, n, m, step_numbers)
        return len(step_numbers)



ob = Solution()
ans = ob.steppingNumbers(0, 21)
print(ans)
