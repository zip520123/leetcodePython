# String Compression
# O(n) time | O(1) space
def compress(self, chars: List[str]) -> int:
    curr_char = chars[0]
    count = 0
    j = 0
    for char in chars:
        if curr_char == char:
            count += 1
        else:
            chars[j] = curr_char
            j += 1
            if count != 1:
                s = str(count)
                for n in s:
                    chars[j] = n
                    j += 1

            curr_char = char
            count = 1

    chars[j] = curr_char
    j += 1
    if count != 1:
        s = str(count)
        for n in s:
            chars[j] = n
            j += 1
    return j

# O(n) time | O(1) space
def compress(self, chars: List[str]) -> int:
    
    l, r = 0, 0
    while r < len(chars):
        curr_char = chars[r]
        count = 0
        while r < len(chars) and chars[r] == curr_char:
            count += 1
            r += 1
        chars[l] = curr_char
        l += 1
        if count > 1:
            s = str(count)
            for n in s:
                chars[l] = n
                l += 1
    return l