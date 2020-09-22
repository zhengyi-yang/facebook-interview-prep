--https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---fibonacci-numbers/problem
module Main where

fib 1 = 0
fib 2 = 1
fib n = fib(n-1) + fib(n-2) -- Enter your code here to complete this function


main = do
    input <- getLine
    print . fib . (read :: String -> Int) $ input