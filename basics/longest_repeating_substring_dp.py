
def solve(string):
    max_len = 0
    index_of_max_len = 0
    last_visit = [0 for x in range(0, len(string))]
    for i, letter in enumerate(string):

        ends_here = [0 for x in range(0, len(string))]
        ends_here[i] = last_visit[i]

        for j in range(i+1, len(string)-1):
            if string[j+1] == letter:
                # print("matched", letter, i, j+1)
                ends_here[j+1] = last_visit[j] + 1
                if ends_here[j+1] > max_len:
                    max_len = ends_here[j+1]
                    index_of_max_len = j+1

        print(ends_here)
        last_visit = ends_here

    print(string[index_of_max_len - max_len + 1:index_of_max_len+1])

    return 0

solve("uygpnkazqfrpjvoaxdpcwmjobmskskfojnewxgxnnofwltwjwnnvbwjckdmeouuzhyvhgvwujbqxxpitcvograiddvhrrdsycqhkleewhxtembaqwqwpqhsuebnvfgvjwdvjjafqzzxlcxdzncqgjlapopkvxfgvicetcmkbljopgtqvvhbgsdvivhesnkqxmwrqidrvmhlubbryktheyentmrobdeyqcrgluaiihveixwjjrqopubjguxhxdipfzwswybgfylqvjzharvrlyauuzdrcnjkphclffrkeecbpdipufhidjcxjhrnxcxmjcxohqanxdrmgzebhnlmwpmhwdvthsfqueeexgrujigskmvrzgfwvrftwapdtutpbztygnsrxajjngcomikjzsdwssznovdruypcnjulkfuzmxnafamespckjcazxdrtdgyrqscczybnvqqcqcjitlvcnvbmasidzgwraatzzwpwmfbfjkncvkelhhzjchpdnlunmppnlgjznkewwuysgefonexpmmsbaopmdgzqmkqzxuvtqvnxbslqzkglzamzpdnsjolvybwxxttqognrbaiakqllszkhfzconnmoqklpeefsnsmouwqhodsgcfohe")
