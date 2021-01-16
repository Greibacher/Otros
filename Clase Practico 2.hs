-- Uso del if then else--
mayor n1 n2 = if n1 > n2 then n1 else n2
menor n1 n2 | n1 < n2 = n1
	    | otherwise = n2

validar_negativo n| n >= 0 = n 
		  | otherwise = 0

--Listas resumidas-- 
--[li..ls]--

factorial n = product[1..n]