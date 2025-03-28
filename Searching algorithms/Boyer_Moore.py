def boyer_moore(t, p):
    def create_last(p):
        l = {}
        for i in range(len(p)):
            l[p[i]] = i
        return l

    l = create_last(p)
    m = len(p)
    n = len(t)
    i = 0
    found = False  # Flag to track if pattern was found

    while i <= n - m:
        j = m - 1
        while j >= 0 and p[j] == t[i + j]:
            j -= 1
        if j == -1:
            print("Pattern found at index", i)
            found = True
            i += m
        else:
            i += max(1, j - l.get(t[i + j], -1))

    if not found:
        print("Pattern was not found")

boyer_moore("lilililiii", "lliii")
