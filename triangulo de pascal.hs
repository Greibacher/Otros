sumatoria :: [Integer] -> [Integer]
sumatoria xs | len == 0 = []
             | len == 1 = xs
	     | otherwise = [xs !! i + xs !! j | i <- [0..len-1], j <- [0..len-1], j == i+1]
	       where len = (length xs)


trianguloPascal :: Integer -> [Integer]
trianguloPascal n | n == 1 = [1]
		  | n == 2 = [1, 2, 1]
		  | otherwise = [1] ++ sumatoria(trianguloPascal(n-1)) ++ [1]