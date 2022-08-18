# https://app.codility.com/programmers/lessons/1-iterations/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    answer = ''
    
    bin_N = bin(N)
    bin_N = bin_N[2:]
    
    idx_ls = []    
    for idx, i in enumerate(bin_N) :
        if i == '1' :
            idx_ls.append(idx)

    if len(idx_ls) < 2 :
        return 0
        
    else :        
        grap = []
        for i in range(len(idx_ls)-1) :
            grap.append(idx_ls[i+1] - idx_ls[i] -1)
        
        answer = max(grap)
        
        return answer

print(solution(1041))