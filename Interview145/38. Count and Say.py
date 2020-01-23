"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
题目讲的是后续的相应的 输出数字 依据的是它之前的 输出数字：

1：当它是 1 的时候，我们就返回字符串 '1'（1）

2：当它是 2 的时候，我们就对之前的 1 报数，即 1 个 1（11）

3：当它是 3 的时候，我们就对之前的 2 报数，即 2 个 1（21）

4：当它是 4 的时候，我们就对之前的 3 报数，即 1 个 2 、 1 个 1（1211）

5：当它是 5 的时候，我们就对之前的 4 报数，即 1 个 1 、 1 个 2 、 2 个 1（111221）

6：当它是 6 的时候，我们就对之前的 5 报数，即 3 个 1 、 2 个 2 、1 个 1（312211）

以此类推……
"""
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        for i in range(n-1):
            say = self.count(say)
        return say
            
    def count(self, say):
        count, i, res = 1, 1, ''
        while i < len(say):
            if say[i] != say[i-1]:
                res += str(count) + say[i-1]
                count = 1
            else:
                count += 1
            i += 1
        res += str(count) + say[i-1]
        return res
