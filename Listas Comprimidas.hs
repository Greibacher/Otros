--Listas por comprension--

{-Para generar una lista por comprensión se coloca
  entre corchetes, separando entre 2 miembros con 
  '|' quedando de la forma [operacion|condicion, condicion]
  una condicion y la vital es la de asignarle que valores deben cumplir la condicion de la forma
  variable <- [arreglo] Significa que los elementos de [arreglo] deberan cumplir todas las condiciones
  Por ejemplo [x^2 | x <- [2..5]]
-}

cuadradomayor = [x^2 | x <- [5..15], x^2 > 50]
cuadrado = [x^2 | x <- [5..15]]
todosmenos = [x | x <- [10..20], x/= 13, x /= 15, x/=19]
listaImpares n = [x|x<-[1..n],odd x, x<15]
interseccion xs ys = [xs !! ind | ind <- [0..(length xs)-1] , elem (xs !! ind) ys]
union xs ys = [lis !! ind | ind <- [0 .. length(xs) + length(ys) -2]] where lis = xs++ys
quitarrepetidos xs | length xs == 0 = []
		   | otherwise = if not(elem (head xs) (quitarrepetidos(tail xs))) 
				 then (head xs):quitarrepetidos(tail xs) else quitarrepetidos(tail xs)
		  
			  