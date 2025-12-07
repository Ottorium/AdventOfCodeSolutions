module Part1 where
import Data.List.Split (splitOn)


solvep1 :: [Char] -> [Char]
solvep1 inp = show (fst (extendBeam (splitOn "\n" inp) 1))

extendBeam :: [[Char]] -> Int -> (Int, [[Char]])
--              grid    currentRow  timesSplit   grid
extendBeam g cr = if cr == length g - 1 then (0, g) else
    let result = extendBeamBy1 (g!!(cr - 1)) (g!!cr) (g!!(cr + 1)) in
    let ga = setNth g cr (snd result) in
    let recurs = extendBeam ga (cr + 1) in
    let n = fst result in
    (fst recurs + n, snd recurs)
    
    

extendBeamBy1 :: [Char] -> [Char] -> [Char] -> (Int, [Char])
--               rowBef   rowCurr   rowAfter timesSplit newRowCurr
extendBeamBy1 (_:rbs) (rc:rcsInitial) (_:ras) = if length rcsInitial == 1 then (0, rc:rcsInitial) else
    let r = extendBeamBy1 rbs rcsInitial ras in
    let n = fst r in
    let rcs = snd r in
    if head rcs == '^' && head rbs == '|' then
        (1 + n, '|':setNth rcs 1 '|')
    else
        if head rbs == '|' || head rbs == 'S' then 
            (n, rc:setNth rcs 0 '|')
        else
            (n, rc:rcs)
extendBeamBy1 _ _ _ = error "unreachable (one of the rows is empty in extendBeamBy1)"

setNth :: [a] -> Int -> a -> [a]
setNth [] _ _= []
setNth (_:ls) 0 r = r:ls
setNth (l:ls) i r = l : setNth ls (i-1) r