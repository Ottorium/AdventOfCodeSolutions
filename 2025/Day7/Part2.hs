module Part2 where
import Data.List.Split (splitOn)
import Data.Map (Map, (!))
import qualified Data.Map as Map

solvep2 :: [Char] -> [Char]
solvep2 inp = let g = splitOn "\n" inp in show (fst (f g 0 (head $ filter ((== 'S') . (head g!!)) [0..]) Map.empty))

f :: [[Char]] -> Int -> Int -> Map (Int, Int) Int -> (Int, Map (Int, Int) Int)
f g r c m
  | Map.member (r, c) m = (m!(r, c), m)
  | r >= length g - 1 = (1, m)
  | g!!(r + 1)!!c == '^'
  = let res1 = f g (r + 1) (c - 1) m in
    let m1 = snd res1 in
    let res2 = f g (r + 1) (c + 1) m1 in
    let resN = fst res1 + fst res2 in 
    let nm = Map.insert (r,c) resN (Map.union (Map.union m1 (snd res2)) m) in (resN, nm)
  | otherwise
  = let result = f g (r + 1) c m in
    let resN = fst result in
    let nm = Map.insert (r, c) resN (Map.union m (snd result)) in (resN, nm)