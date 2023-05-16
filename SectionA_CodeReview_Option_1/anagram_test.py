import unittest

class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for i in strs:
            x = "".join(sorted(i))  # Here, sort the characters in the string i
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())

class AnagramTest(unittest.TestCase):
    def test_groupAnagrams(self):
        solution = Solution()

        # Test case 1
        input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        actual_output1 = solution.groupAnagrams(input1)
        expected_output1.sort()
        actual_output1.sort()
        self.assertEqual(actual_output1, expected_output1)



if __name__ == "__main__":
    unittest.main()
