def generateSquare(n):
    #1= 2-D array with all   # 2=slots set to 0
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]

    #3= initialize position of 1
    i = n / 2
    j = n - 1

    #4= Fill the magic square
    #5= by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:

            #6= next number goes out of
            #7=  right side of square
            if j == n:
                j = 0

            #8= next number goes
            #9=  out of upper side
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j -= 2
            i += 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num += 1

        j +=1
        i -=1  # 1st condition

    #10= Printing magic square
    print("Magic Squre for n =", n)
    print("Sum of each row or column",
          n * (n * n + 1) / 2, "\n")

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                  end='')

            #11= To display output
            #12= in matrix form
            if j == n - 1:
                print()
n = int(input("Enter The Order : "))

generateSquare(n)