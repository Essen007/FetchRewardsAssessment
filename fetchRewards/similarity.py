def compute_wer(text1="",text2=""):
    t1 = text1.split(" ")
    t2 = text2.split(" ")
    l1 = len(t1)
    l2 = len(t2)
    if l1 == 0 or l2 == 0:
        return max(l1,l2)

    dp1 = [i for i in range(l2 + 1)]
    dp2 = [1 for _ in range(l2 + 1)]
    result = dp1[-1]
    for i in range(1,l1 + 1):
        for j in range(1,l2+1):
            if t1[i-1] == t2[j-1]:
                dp2[j] = dp1[j - 1]
            else:
                dp2[j] = min(dp1[j - 1], dp1[j], dp2[j - 1]) + 1
        dp1 = dp2[:]
        dp2 = [i + 1 for _ in range(l2 + 1)]
        result = dp1[-1]

    return 100 - (result / l2) * 100
