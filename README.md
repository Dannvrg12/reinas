# N-Queens Problem Solver

![](https://github.com/Dannvrg12/reinas/blob/main/reinas/reinas.jpg)

## Purpose of the Project

This project aims to provide a solution to the N-Queens problem using backtracking.

## Introduction

The N-Queens problem is a classic combinatorial problem that involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.

### Solving with Backtracking

Backtracking is a common approach to solve the N-Queens problem. The algorithm explores possible placements of queens on the chessboard, backtracking when it determines that the current placement cannot lead to a solution.

The backtracking algorithm systematically explores the search space, trying out different configurations until a valid solution is found or all possibilities are exhausted.

## Usage

To use this solver, you can easily install the project package using the following code: ! pip install git+https://github.com/Dannvrg12/reinas. Once the package is installed, simply call the following functions: from reinas import es_seguro, from reinas import resolver_n_reinas_util, and from reinas import resolver_n_reinas. After calling these functions, you can use the following code as a starting point: n = i solutions = resolver_n_reinas(n) print(soluciones[0]).

For a breakdown of all possible solutions for the given 'n', you can use the following loop:for solution in soluciones:
    print(solution).
    It's important to clarify that this code works efficiently and "quickly" in environments like Google Colab up to n=13. For n>=13, you may need to use a more powerful environment such as Visual Studio for up to n=16. Beyond that, the code will take a bit more time, and for a certain n, it may no longer work properly.

 ## Interpretation of the Solution 
    
 [1, 5, 8, 6, 3, 7, 2, 4], This list represents a valid configuration of the N-queens board. Each index corresponds to a row, and the value at that index indicates the column where a queen is placed in that row.

In Row 0 (Index 0):

- 1: There is a queen in column 1 of row 0.

In Row 1 (Index 1):

- 5: There is a queen in column 5 of row 1.

In Row 2 (Index 2):

- 8: There is a queen in column 8 of row 2.

In Row 3 (Index 3):

- 6: There is a queen in column 6 of row 3.

In Row 4 (Index 4):

- 3: There is a queen in column 3 of row 4.

In Row 5 (Index 5):

- 7: There is a queen in column 7 of row 5.

In Row 6 (Index 6):

- 2: There is a queen in column 2 of row 6.

In Row 7 (Index 7):

- 4: There is a queen in column 4 of row 7.




Feel free to contribute, report issues, or suggest improvements!
