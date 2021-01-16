factorial :: Integer -> Integer
factorial n | n < 0 = -1
	    | n == 0 = 1
	    | otherwise = n * factorial(n-1)


implicaciónSimple :: Bool -> Bool -> Bool
implicaciónSimple ant con = if (ant && (not con)) then False else True


deDecimalaBinario :: Integer -> [Integer]
deDecimalaBinario n | n < 0 = []
		    | n < 2 = [n]
		    | otherwise = deDecimalaBinario(r) ++ [v]
		    where 
			  v = n `mod` 2
			  r = n `div` 2


invertir :: [Integer] -> [Integer]
invertir lista | lista == [] = []
	       | length lista == 1 = lista
	       | otherwise = last lista: invertir (init lista) 


deBinarioaDecimal :: [Integer] -> Integer
deBinarioaDecimal lista = sum [(lis!!x) * (2 ^ y)| x <- ind, y <- ind, x == y]
			where lis = invertir lista
			      ind = [0..length lis-1]


implicaciónDoble :: Bool -> Bool -> Bool
implicaciónDoble ant con = implicaciónSimple ant con && implicaciónSimple con ant


razonamiento :: [Bool] -> [Bool]-> Bool
razonamiento preposiciones conclusiones = True 
