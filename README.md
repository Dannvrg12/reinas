# N-Queens Problem Solver

![](http://github.com/Dannvrg12/reinas/blob/main/reinas/reinas.jpeg)

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

Feel free to contribute, report issues, or suggest improvements!
