import operator


def solve(string):
    appearances = {}

    for i, letter in enumerate(string):
        if letter not in appearances:
            appearances[letter] = [i]
        else:
            appearances[letter].append(i)

    max_len = 0
    index_of_max_len = 0
    last_visit = [0 for x in range(0, len(string))]

    for i, letter in enumerate(string):
        ends_here = [0 for x in range(0, len(string))]
        ends_here[i] = last_visit[i]

        letter_found_here = list(filter(lambda o: o > i, appearances[letter]))
        for pos in letter_found_here:
            ends_here[pos] = last_visit[pos-1] + 1
            if ends_here[pos] > max_len:
                max_len = ends_here[pos]
                index_of_max_len = pos

        print(ends_here)
        last_visit = ends_here
    return string[index_of_max_len - max_len + 1:index_of_max_len+1]


solve("uygpnkazqfrpjvoaxdpcwmjobmskskfojnewxgxnnofwltwjwnnvbwjckdmeouuzhyvhgvwujbqxxpitcvograiddvhrrdsycqhkleewhxtembaqwqwpqhsuebnvfgvjwdvjjafqzzxlcxdzncqgjlapopkvxfgvicetcmkbljopgtqvvhbgsdvivhesnkqxmwrqidrvmhlubbryktheyentmrobdeyqcrgluaiihveixwjjrqopubjguxhxdipfzwswybgfylqvjzharvrlyauuzdrcnjkphclffrkeecbpdipufhidjcxjhrnxcxmjcxohqanxdrmgzebhnlmwpmhwdvthsfqueeexgrujigskmvrzgfwvrftwapdtutpbztygnsrxajjngcomikjzsdwssznovdruypcnjulkfuzmxnafamespckjcazxdrtdgyrqscczybnvqqcqcjitlvcnvbmasidzgwraatzzwpwmfbfjkncvkelhhzjchpdnlunmppnlgjznkewwuysgefonexpmmsbaopmdgzqmkqzxuvtqvnxbslqzkglzamzpdnsjolvybwxxttqognrbaiakqllszkhfzconnmoqklpeefsnsmouwqhodsgcfohe")

# words = solve("uygpnkazqfrpjvoaxdpcwmjobmskskfojnewxgxnnofwltwjwnnvbwjckdmeouuzhyvhgvwujbqxxpitcvograiddvhrrdsycqhkleewhxtembaqwqwpqhsuebnvfgvjwdvjjafqzzxlcxdzncqgjlapopkvxfgvicetcmkbljopgtqvvhbgsdvivhesnkqxmwrqidrvmhlubbryktheyentmrobdeyqcrgluaiihveixwjjrqopubjguxhxdipfzwswybgfylqvjzharvrlyauuzdrcnjkphclffrkeecbpdipufhidjcxjhrnxcxmjcxohqanxdrmgzebhnlmwpmhwdvthsfqueeexgrujigskmvrzgfwvrftwapdtutpbztygnsrxajjngcomikjzsdwssznovdruypcnjulkfuzmxnafamespckjcazxdrtdgyrqscczybnvqqcqcjitlvcnvbmasidzgwraatzzwpwmfbfjkncvkelhhzjchpdnlunmppnlgjznkewwuysgefonexpmmsbaopmdgzqmkqzxuvtqvnxbslqzkglzamzpdnsjolvybwxxttqognrbaiakqllszkhfzconnmoqklpeefsnsmouwqhodsgcfohe")
# print(words)
# longest = ""
# for word, pos in words.items():
#     if len(word) > len(longest):
#         longest = word
#     if len(word) == len(longest) and pos < words[longest]:
#         longest = word
#
# print(longest if longest else -1)
