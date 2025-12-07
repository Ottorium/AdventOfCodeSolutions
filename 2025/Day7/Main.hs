module Main where
import Part1 (solvep1)
import Part2 (solvep2)

main :: IO ()
main = do 
    input <- readFile "input.txt"
    putStrLn ("Part 1: " ++ solvep1 input)
    putStrLn ("Part 2: " ++ solvep2 input)
