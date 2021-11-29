def partition(n):
    if n <= 0:
        return 0
    elif n in {1,2,3}:
        return n
    else:
        psum = 0
        k = 1
        while n > k*(3*k-1)//2:
            psum += (-1)**(k+1)*(partition(n-k*(3*k-1)//2)+partition(n-k*(3*k+1)//2))
            k += 1
        return psum