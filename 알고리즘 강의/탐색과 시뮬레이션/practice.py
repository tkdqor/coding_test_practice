def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    position = 0
    while c:
        try:
            if c[position] == 0:
                if c[position + 2] == 0:
                    position += 2
                    jump += 1
                elif c[position + 1] == 0:
                    position += 1
                    jump += 1
            if position == len(c)-1:
                return jump
        except:
            break
    position += 1
    jump += 1
    return jump

print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))