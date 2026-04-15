class Solution(object):
    """
        simplified solution - didnt pass all of the tests

        def canConstruct(self, ransomNote, magazine):
        ransomNote = ransomNote.lower()
        magazine = magazine.lower()

        if ransomNote in magazine:
            return True
        else:
            return False
    """

    """
        doesnt account for repeating letters
        
            def canConstruct(self, ransomNote, magazine):
        ransomNote = ransomNote.lower()
        magazine = magazine.lower()

        previousLetter = ransomNote[0]
        counter = 0

        for ransomLetter in ransomNote:
            for magazineLetter in magazine:
                if ransomLetter == magazineLetter:
                    counter += 1
                    break
        
        if counter == len(ransomNote):
            return True
        else:
            return False
    """
    def canConstruct(self, ransomNote, magazine):
            magazine = list(magazine)

            for letter in ransomNote:
                if letter in magazine:
                    magazine.remove(letter)  # use the letter once
                else:
                    return False

            return True


if __name__ == '__main__':
    solution = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(solution.canConstruct(ransomNote, magazine))

    ransomNote = "ab"
    magazine = "aab"
    print(solution.canConstruct(ransomNote, magazine))

    ransomNote = "aa"
    magazine = "aab"
    print(solution.canConstruct(ransomNote, magazine))

    ransomNote = "aab"
    magazine = "baa"
    print(solution.canConstruct(ransomNote, magazine))
