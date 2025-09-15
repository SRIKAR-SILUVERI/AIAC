def rolling_mean(xs, w):
    # Guard invalid window size
    if w <= 0 or w > len(xs):
        return []
    
    sums = []
    for i in range(len(xs) - w + 1):   # ✅ fix: include last window
        window = xs[i:i+w]
        sums.append(sum(window) / w)
    return sums


# Sample Test
xs = [1, 2, 3, 4]
w = 2
print(rolling_mean(xs, w))