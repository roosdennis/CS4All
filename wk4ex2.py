def rot(c,n):
    if 'a' <= c <= 'z':          # lower-case
        c = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':        # upper-case
        c = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    return c
