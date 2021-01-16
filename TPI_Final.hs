--Funciones del trabajo practico del paradigma funcional--

--1)--
porcentaje:: Integer-> Float
porcentaje codigo | codigo == 1 = 0.15
		  | codigo == 2 = 0.1
		  | codigo == 3 = 0.07
		  | codigo == 4 = 0.01
		  | otherwise = 0

--2)--
total_cobrar :: (Float, Integer) -> Float
total_cobrar (precio, codigo) = precio + imp_del
				where imp_del =  precio * (porcentaje codigo)
			
--3)--
vuelto :: Float -> Float -> Float
vuelto total dinero = if dinero >= total then (dinero - total) else -1

--4)--
montos_totales:: [Float] -> [Integer] -> [Float]
montos_totales (imp : imps) (cod : cods) |(length imps /= length cods) = []
					 |imps == [] = monto:[]
 					 |otherwise = monto: montos_totales imps cods
					  where monto = total_cobrar (imp, cod)

--5)--
vuelto_clientes :: [Float] -> [Float] -> [Float]
vuelto_clientes montos dinero = if(length montos /= length dinero)
					then [] 
					else [vuelto(montos !! ind)(dinero !! ind) |
											ind <- [0..(length montos)-1],
											vuelto(montos !! ind)(dinero !! ind) /= 0] 
