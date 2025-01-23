class Solution(object):
    def scoreOfString(self, s):
        list2 = list(s)
        answer = 0
        for i in range(1, len(list2)):
            
            answer +=abs(ord(list2[i]) - ord(list2[i-1]))

        return answer
            
