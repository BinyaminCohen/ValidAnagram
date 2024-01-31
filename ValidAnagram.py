# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class ValidAnagram(object):
    def is_anagram(self, s, t):

        if len(s) != len(t):
            print(f"The string {t} isn't anagram.")

        else:
            for s_char in s:
                if s_char.strip() not in t.strip():
                    print(f"The string {t} isn't anagram.")
                    return None
            print(f"The string {t} is anagram.")


ValidAnagram().is_anagram("anagram", "nagaram")
ValidAnagram().is_anagram("rat", "car")
ValidAnagram().is_anagram("", "")



