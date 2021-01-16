--Funcion Recursiva que suma--
sumar::[Integer] -> Integer

--Caso Base--
sumar [] = 0

--Caso Recursivo--
sumar (x:xs) = x + sumar xs

--Función que retorna una lista--

lista :: (Integer, Integer, Integer) -> [Integer]

--Se agrega al primer elemento ls a la lista--
lista (li, ls, s) | li > ls = res
		  | li <= ls = res ++ [li]
 		  	where res = []