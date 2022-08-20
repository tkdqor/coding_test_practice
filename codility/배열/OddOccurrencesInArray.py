# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def solution(A):
    
    A = sorted(A)

    while A:
        try : 
            a = A.pop()
            b = A.pop()
        except : 
            break

        if not a == b:
            break
            
    return a 

print(solution([9,3,9,3,9,7,9]))