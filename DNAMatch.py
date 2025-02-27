def dna_match_bottomup(DNA1, DNA2):
    m = len(DNA1)
    n = len(DNA2)
    cache = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[m][n]

#str1 = "ATAGTTCCGTCAAA"
#str2 = "GTGTTCCCGTCAAA"
#print(dna_match_bottomup(str1, str2))

def dna_match_topdown_helper(str1, str2, m, n):

    while m >= 0:
        while n >= 0:
            if m == 0 or n == 0:
                return 0
            elif str1[m - 1] == str2[n - 1]:
                return dna_match_topdown_helper(str1, str2, m-1, n-1) + 1
            else:
                return max(dna_match_topdown_helper(str1, str2, m-1, n), dna_match_topdown_helper(str1, str2, m, n-1))

def dna_match_topdown(DNA1, DNA2):

    return dna_match_topdown_helper(DNA1, DNA2, len(DNA1), len(DNA2))

#str1 = "ATAGTTCCGTCAAA"
#str2 = "GTGTTCCCGTCAAA"
#print(dna_match_topdown(str1, str2))
