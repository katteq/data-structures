def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here

    i = len(our_string) - 1
    res = ''
    while i >= 0:
      res += our_string[i]
      i -= 1

    return res


def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here

    str1_letters = str1.replace(" ", "").lower()
    str2_letters = str2.replace(" ", "").lower()

    if len(str1_letters) != len(str2_letters):
      return False

    for letter in str1_letters:
      if letter in str2_letters:
        str2_letters = str2_letters.replace(letter, "", 1)

    return True if str2_letters == "" else False


print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
