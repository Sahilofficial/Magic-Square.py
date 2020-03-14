# Magic-Square.py
In recreational mathematics and combinatorial design, a magic square[1] is a {\displaystyle n\times n}n\times n square grid (where n is the number of cells on each side) filled with distinct positive integers in the range {\displaystyle 1,2,...,n^{2}}{\displaystyle 1,2,...,n^{2}} such that each cell contains a different integer and the sum of the integers in each row, column and diagonal is equal.[2] The sum is called the magic constant or magic sum of the magic square. A square grid with n cells on each side is said to have order n.
# Magic constant
The constant that is the sum of any row, or column, or diagonal is called the magic constant or magic sum, M. Every normal magic square has a constant dependent on the order n, calculated by the formula {\displaystyle M=n(n^{2}+1)/2}{\displaystyle M=n(n^{2}+1)/2}. This can be demonstrated by noting that the sum of {\displaystyle 1,2,...,n^{2}}{\displaystyle 1,2,...,n^{2}} is {\displaystyle n^{2}(n^{2}+1)/2}{\displaystyle n^{2}(n^{2}+1)/2}. Since the sum of each row is {\displaystyle M}M, the sum of {\displaystyle n}n rows is {\displaystyle nM=n^{2}(n^{2}+1)/2}{\displaystyle nM=n^{2}(n^{2}+1)/2}, which when divided by the order n yields the magic constant. For normal magic squares of orders n = 3, 4, 5, 6, 7, and 8, the magic constants are, respectively: 15, 34, 65, 111, 175, and 260. For example, a normal 6x6 square will always equate to 111 for each row, column, or diagonal.
# Algoritm
M = n(n^2+1)/2 

1- In any magic square, 1 is 1located at position (n/2, n-1).

2- Let's say the position of 1 i.e. (n/2, n-1) is (p, q), then next number which is 2 is located at (p-1, q+1) position.

   Anytime if the calculated row position becomes -1 then make it n-1 and if column position becomes n then make it O.
   
3- If the calculated position already contains a number then decrement the column by 2 and increment the row by 1.

4- If anytime row position becomes -1 and column becomes n, switch it to (0, n-2).
