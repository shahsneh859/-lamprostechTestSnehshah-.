def romanToInt(s: str) -> int:
    # Dictionary of roman numerals
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Length of the given string
    n = len(s)
    num = roman[s[n - 1]]
    # Loop for each character from right to left
    for i in range(n - 2, -1, -1):
       
        if roman[s[i]] >= roman[s[i + 1]]:
            num += roman[s[i]]
        else:
            num -= roman[s[i]]
    return num
