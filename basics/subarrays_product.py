# Find the number of sub-arrays with product less than K

def calc_subarrays(n):
    cnt = 0
    for i in range(0, n + 1):
        cnt += (n - i)
    return cnt


def solve(AR, K):
    n = 0

    subarray_product = 1
    start_of_subarray = 0

    for i, num in enumerate(AR):
        prod = subarray_product * num
        if num > K:
            start_of_subarray += 1
            subarray_product = 1
        if prod > K:
            #  Count the subarrays
            n += calc_subarrays(i-n)
            print("plus", i, n)
            start_of_subarray = i if num < K else i+1
            subarray_product = num if num < K else 1

            #  Move the left pointer
            while start_of_subarray < i and subarray_product * num > K:
                start_of_subarray += 1
                subarray_product = subarray_product / AR[start_of_subarray]

            n -= calc_subarrays(i - start_of_subarray)
            print(" -> minus", i, start_of_subarray)
        else:
            subarray_product *= num

    n += calc_subarrays(len(AR) - start_of_subarray)
    print("plus", start_of_subarray, len(AR))
    return n


# AR = "30 38 36 94 19 29 44 12 29 30 77 5 44 64 14 39 7 41 5 19 29 89 70 18 18 97 25 44 71 84 91 100 73 26 45 91 6 40 55 87 70 83 43 65 98 8 56 5 49 12 23 29 100 44 47 69 41 23 12".split()
AR = "1 5 20 8 1 8".split()
AR = list(map(int, AR))
N = solve(AR, 100)
print(N)

# print(calc_subarrays(-4))