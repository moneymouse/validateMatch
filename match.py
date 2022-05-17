from util import safe_sum, safe_sum_s
# bg: the Binarizate pic of background
# pattern: the Binarizate pic of pattern
def match(bg,pattern):
    bg_row,bg_col = bg.shape
    pattern_row, pattern_col = pattern.shape

    min = []
    res = {}
    for i in range((bg_col-pattern_col+1)* (bg_row - pattern_row + 1)):
        x = i % (bg_col - pattern_col + 1)
        y = i // (bg_col - pattern_col + 1)
        result = safe_sum(bg[y:pattern_row + y,x:pattern_col + x],pattern)
        # print(x,y)
        min.append(result)
        if(res.get(result,False)): res[result].append((y,x))
        else: res[result] = [(y,x)]

    min.sort()

    most_min = pattern_row* pattern_col * 255
    poi = (0,0)
    for i in range(10):
        for y,x  in res[min[i]]:
            result = safe_sum_s(bg[y:pattern_row + y,x:pattern_col + x],pattern)
            if result < most_min:
                most_min = result
                poi = (y,x)
    return poi

# print(match(dst,get_pattern()))
