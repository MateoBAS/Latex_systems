from sympy import symbols, Eq, solve, Matrix, simplify, Array, latex, real_root

def eliminar_fila_columna(matriz, indice):
    fila, columna = indice
    nueva_matriz = []
    for i in range(matriz.shape[0]):
        if i != fila:
            nueva_fila = []
            for j in range(matriz.shape[1]):
                if j != columna:
                    nueva_fila.append(matriz.row(i)[j])
            nueva_matriz.append(nueva_fila)
    return Matrix(nueva_matriz)

# Define el parametro 'a'
a, λ, μ, φ, x, y, z = symbols('a λ μ φ x y z')
incognitas=["x", "y", "z"]

# Crea una matriz vacia de 3x3
matriz = Matrix.zeros(3, 3)
matriz2 = Matrix.zeros(3,3)
matriz3 = Matrix.zeros(3,3)

# Solicita las entradas de la matriz una a una
'''for i in range(3):
    for j in range(3):
        entrada = input(f"Ingrese la entrada en la posicion ({i+1}, {j+1}): ")
        entrada = eval(entrada)  # Evalua la expresion ingresada
        matriz[i, j] = entrada
        
terminos_independientes = []

# Solicita los terminos independientes uno a uno
for i in range(3):
    termino = input(f"Ingrese el termino independiente de la ecuacion {i+1}: ")
    termino = eval(termino)  # Evalua la expresion ingresada
    terminos_independientes.append(termino)

# Imprime la lista de terminos independientes
print("Terminos independientes:", terminos_independientes)'''


label="r)"

with open('enunciado.txt', 'r') as file:
    # Lee todas las lineas del archivo
    lineas = file.readlines()

indices_m = [5,6,7]
lineas_m = [lineas[i] for i in indices_m]
lineas_i = lineas[11]
# Itera a traves de las lineas y divide cada linea en una lista usando la coma como delimitador
lineas_m_final = []
for linea in lineas_m: #5,6,7  11
    #valores = linea.strip().split(',')
    lineas_m_final.append(linea[:-1])

matriz = Matrix([eval(lineas_m_final[0]), eval(lineas_m_final[1]), eval(lineas_m_final[2])])
terminos_independientes = Array(eval(lineas_i))




for i in range(3):
    for j in range(3):
        matriz3[i,j]=matriz[i,j]

with open('Solucion.tex', 'w') as f:
    
    #Librerias necesarias, margenes...

    f.write("\\documentclass{article}\n\\author{Mateo Bouchet Agudo}\n\\title{Ejercicios resueltos}\n\n")
    f.write("\\usepackage[top=2.5cm, bottom=2.5cm, left=3cm, right=3cm]{geometry}\n\\usepackage{amsmath}\n")
    f.write("\\usepackage{amsfonts}\n\\usepackage{amssymb}\n\\usepackage{mathtools}\\usepackage{physics}\n")
    f.write("\\usepackage{cancel}\n\\usepackage{graphicx}\n\\usepackage{float}\n\\usepackage{ragged2e}\n\n")
    f.write("\\newcommand\\undermat[2]{%\n  \\makebox[0pt][l]{$\\smash{\\underbrace{\\phantom{%\n    ")
    f.write("\\begin{matrix}#2\\end{matrix}}}_{\\text{$#1$}}}$}#2}\n\n")
    f.write("\\begin{document}\n\n\\maketitle\n\n\\justify\n\n")
    
    f.write("\\begin{enumerate}")
    #f.write(f"{label}")       
    f.write("\n\\textbf{Discute el siguiente sistema en funci\\'on del valor del par\\'ametro $a$}\n")
    
    f.write("$$")
    f.write("\\left \\{\\begin{array}{ll}")
    for i in range(3):
        ecuacion = Eq(matriz[i, 0]*x + matriz[i, 1]*y + matriz[i, 2]*z, terminos_independientes[i])
        f.write("\\mathbf{")
        f.write(f"{latex(ecuacion)}")
        f.write("}\\\\")
    f.write("\\end{array}\\right.")
    f.write("$$\n\\end{enumerate}\n")
    
    
    f.write("En primer lugar, vamos a obtener la matriz asociada al sistema.\n")
    f.write("$$")
    f.write("\\overbrace{\\left(\\begin{array}{ccc|c}")
    f.write(f"{latex(matriz[0,0])} & {latex(matriz[0,1])} & {latex(matriz[0,2])} & {latex(terminos_independientes[0])} \\\\")
    f.write(f"{latex(matriz[1,0])} & {latex(matriz[1,1])} & {latex(matriz[1,2])} & {latex(terminos_independientes[1])} \\\\")
    f.write("\\undermat{A}{")
    f.write(f"{latex(matriz[2,0])} & {latex(matriz[2,1])} & {latex(matriz[2,2])}")
    f.write("} & ")
    f.write(f"{latex(terminos_independientes[2])} \\\\")
    f.write("\\end{array}\\right)}^{A*}")
    f.write("\\rightarrow \\begin{array}{cc} \\text{donde A es la matriz del sistema} \\\\\\text{y A* la matriz ampliada} \\end{array}")
    f.write("$$\\\\\n\n")
    
    # Calcula el determinante
    determinante = matriz.det()
    
    ecuacion = Eq(determinante, 0)
    
    # Resuelve la ecuacion
    soluciones = solve(ecuacion)
    
    soluciones = [solucion for solucion in soluciones if solucion.as_real_imag()[1] == 0]
        
    print(soluciones)
        
    cadena="c"*len(soluciones)
    hay_solucion=True
    
    f.write("Vamos a estudiar el rango de la matriz A. Para ello, vamos a usar el determinante. Si det(A) = 0, entonces Rg(A) $<$ 3. En otro caso, Rg(A) = 3.\n")
    f.write("$$")
    f.write("\\begin{vmatrix}")
    f.write(f"{latex(matriz[0,0])} & {latex(matriz[0,1])} & {latex(matriz[0,2])} \\\\")
    f.write(f"{latex(matriz[1,0])} & {latex(matriz[1,1])} & {latex(matriz[1,2])}\\\\")
    f.write(f"{latex(matriz[2,0])} & {latex(matriz[2,1])} & {latex(matriz[2,2])}")
    f.write("\\end{vmatrix}=0\\to ")
    f.write(f"{latex(determinante)}=0\\to")
    if len(soluciones) == 0:
        f.write("\\nexists \\text{ soluci\\'on}")
        hay_solucion=False
    else:
        f.write("\\left\\{\\begin{array}{")
        f.write(f"{cadena}")
        f.write("}")
        for i in range(len(soluciones)):
            if i==(len(soluciones)-1):
                f.write(f"a_{i+1}={latex(soluciones[i])}")
            else:
                f.write(f"a_{i+1}={latex(soluciones[i])}\\\\")

        f.write("\\end{array}\\right.")
    f.write("$$\n\n")
    
    if hay_solucion==False:
        f.write("Puesto que no hay ning\\'un valor que haga que det(A) = 0, entonces Rg(A) = 3 $\\forall$a. ")
        f.write("Adem\\'as, puesto que A esta contenida en A*, Rg(A*) = 3. ")
        f.write("Como Rg(A) = Rg(A*) = n$^{\\text{o}}$ inc\\'ognitas = 3, seg\\'un el teorema de Rouch\\'e-Frobenius, el sistema ser\\'a compatible determinado.\n ")
        f.write("La soluci\\'on la podemos hallar empleando la regla de Cramer\n")
        for k in range(3):
            f.write("$$\n")
            for i in range(3):
                for j in range(3):
                    matriz2[i,j]=matriz[i,j]

            for i in range(3):
                matriz2[i, k] = terminos_independientes[i]

            determinante2 = matriz2.det()
            print(f"{incognitas[k]}=", determinante2/determinante,"     ", latex(simplify(determinante2/determinante)))
            f.write(f"{incognitas[k]}=")
            f.write("\\frac{\\begin{vmatrix}")
            f.write(f"{latex(matriz2[0,0])} & {latex(matriz2[0,1])} & {latex(matriz2[0,2])} \\\\")
            f.write(f"{latex(matriz2[1,0])} & {latex(matriz2[1,1])} & {latex(matriz2[1,2])}\\\\")
            f.write(f"{latex(matriz2[2,0])} & {latex(matriz2[2,1])} & {latex(matriz2[2,2])}")
            f.write("\\end{vmatrix}}{|A|}=")
            f.write(f"{latex(determinante2/determinante)}={latex(simplify(determinante2/determinante))}")
            f.write("$$\n\n")
    else:
        f.write("Si a $\\neq$ ")
        for i in range(len(soluciones)):
            f.write(f"${latex(soluciones[i])}$, ")
        f.write("entonces Rg(A) = 3. Adem\\'as, como A est\\'a contenida en A*, Rg(A*) = Rg(A) = n$^{\\text{o}}$ inc\\'ognitas = 3. ")
        f.write("Por tanto, seg\\'un el teorema de Rouch\\'e-Frobenius, el sistema ser\\'a compatible determinado y ")
        f.write("la soluci\\'on general la podemos obtener empleando la regla de Cramer.\n")
        for k in range(3):
            f.write("$$\n")
            for i in range(3):
                for j in range(3):
                    matriz2[i,j]=matriz[i,j]

            for i in range(3):
                matriz2[i, k] = terminos_independientes[i]

            determinante2 = matriz2.det()
            print(f"{incognitas[k]}=", determinante2/determinante,"     ", latex(simplify(determinante2/determinante)))
            f.write(f"{incognitas[k]}=")
            f.write("\\frac{\\begin{vmatrix}")
            f.write(f"{latex(matriz2[0,0])} & {latex(matriz2[0,1])} & {latex(matriz2[0,2])} \\\\")
            f.write(f"{latex(matriz2[1,0])} & {latex(matriz2[1,1])} & {latex(matriz2[1,2])}\\\\")
            f.write(f"{latex(matriz2[2,0])} & {latex(matriz2[2,1])} & {latex(matriz2[2,2])}")
            f.write("\\end{vmatrix}}{|A|}=")
            f.write(f"{latex(determinante2/determinante)}={latex(simplify(determinante2/determinante))}")
            f.write("$$")
            
        f.write("\\\\\n\n")
        
        
        #En este punto hemos mostrado la solucion general. Hay  que explicar los casos particulares
        # Imprime las soluciones
        print("Las soluciones para la ecuacion determinante = 0 son:")
        for solucion in soluciones:
            print("a =", solucion)

        print("Si a distinto de esos valores, la solucion del sistema es:")
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    matriz2[i,j]=matriz[i,j]

            for i in range(3):
                matriz2[i, k] = terminos_independientes[i]

            determinante2 = matriz2.det()
            print(f"x_{k}=", determinante2/determinante,"     ", latex(simplify(determinante2/determinante)))

        for l in range(len(soluciones)):
            matriz_evaluada = matriz.subs(a,soluciones[l])
            terminos_independientes_evaluados = [termino.subs(a, soluciones[l]) for termino in terminos_independientes]
            
            f.write(f"Si a = ${latex(soluciones[l])}$, la matriz que obtenemos es la siguiente:\n")
            f.write("$$\n")
            f.write("\\left(\\begin{array}{ccc|c}")
            f.write(f"{latex(matriz_evaluada[0,0])} & {latex(matriz_evaluada[0,1])} & {latex(matriz_evaluada[0,2])} & {latex(terminos_independientes_evaluados[0])} \\\\")
            f.write(f"{latex(matriz_evaluada[1,0])} & {latex(matriz_evaluada[1,1])} & {latex(matriz_evaluada[1,2])} & {latex(terminos_independientes_evaluados[1])}\\\\")
            f.write(f"{latex(matriz_evaluada[2,0])} & {latex(matriz_evaluada[2,1])} & {latex(matriz_evaluada[2,2])} & {latex(terminos_independientes_evaluados[2])}")
            f.write("\\end{array}\\right)")
            f.write("$$\n\n")

            RgA=matriz_evaluada.rank()
            
            f.write(f"Nos podemos dar cuenta que el Rg(A) = {RgA} ya que ")
            if(RgA==0):
                f.write("todos los elementos de A son nulos. ")
            if(RgA==1):
                f.write("s\\'olo existe una fila linealmente independiente (todos los menores 2x2 son 0). ")
            if(RgA==2):
                f.write("existe un menor 2x2 que es distinto de 0. ")
                for i in range(3):
                    for j in range(3):
                        nueva_matriz=eliminar_fila_columna(matriz_evaluada, (i,j))
                        if nueva_matriz.det() != 0:
                            f.write(f"Si tomamos el menor en la posici\\'on ({i+1}, {j+1}):\n\n")
                            f.write("$$\n")
                            f.write("\\begin{vmatrix}")
                            f.write(f"{latex(nueva_matriz[0,0])} & {latex(nueva_matriz[0,1])}\\\\")
                            f.write(f"{latex(nueva_matriz[1,0])} & {latex(nueva_matriz[1,1])}")
                            f.write("\\end{vmatrix} = ")
                            f.write(f"{latex(nueva_matriz.det())} \\neq 0")
                            f.write("$$\n\n")
                            break
                    else:
                        continue
                    break
                                     
            #Quiero sustituir 
            compatible=True
            for k in range(3):
                for i in range(3):
                    for j in range(3):
                        matriz2[i,j]=matriz_evaluada[i,j]

                for i in range(3):
                    matriz2[i, k] = terminos_independientes_evaluados[i]
                print(f"Cuando a={soluciones[l]}, tenemos que la matriz")
                print(matriz2)
                print(f"tiene rango {matriz2.rank()}")
                if(RgA<matriz2.rank()):
                    compatible=False
                    for i in range(3):
                        for j in range(3):
                            matriz3[i,j]=matriz2[i,j]
                    #matriz3=matriz2
    
            if(compatible==False):
                print("El sistema es incompatible si a = ", soluciones[l])
                print(matriz3)
                f.write(f"En lo referente a A*, existe un menor {matriz3.rank()}x{matriz3.rank()} que es distinto de 0. Por ejemplo ")
                if matriz3.rank() == 1:
                    for i in range(3):
                        if terminos_independientes_evaluados[i] != 0:
                            f.write(f"el t\\'erimino {latex(terminos_independientes_evaluados[i])} \\neq 0. ")
                            f.write("Esto implica que Rg(A*) = 1 $>$ Rg(A). Por tanto, seg\\'un el teorema de Rouch\\'e-Frobenius, el sistema es incompatible.\n\n ")
                            break
                if matriz3.rank() == 2:
                    for i in range(3):
                        for j in range(3):
                            nueva_matriz=eliminar_fila_columna(matriz3, (i,j))
                            if nueva_matriz.det() != 0:
                                f.write("\n$$\n")
                                f.write("\\begin{vmatrix}")
                                f.write(f"{latex(nueva_matriz[0,0])} & {latex(nueva_matriz[0,1])}\\\\")
                                f.write(f"{latex(nueva_matriz[1,0])} & {latex(nueva_matriz[1,1])}")
                                f.write("\\end{vmatrix} = ")
                                f.write(f"{latex(nueva_matriz.det())} \\neq 0")
                                f.write("$$\n\n")
                                f.write("Esto implica que Rg(A*) = 2 $>$ Rg(A). Por tanto, seg\\'un el teorema de Rouch\\'e-Frobenius, el sistema es incompatible.\n\n ")
                                break
                        else:
                            continue
                        break
                if matriz3.rank() == 3:
                    f.write("$$\n")
                    f.write("\\begin{vmatrix}")
                    f.write(f"{latex(matriz3[0,0])} & {latex(matriz3[0,1])} & {latex(matriz3[0,2])} \\\\")
                    f.write(f"{latex(matriz3[1,0])} & {latex(matriz3[1,1])} & {latex(matriz3[1,2])}\\\\")
                    f.write(f"{latex(matriz3[2,0])} & {latex(matriz3[2,1])} & {latex(matriz3[2,2])}")
                    f.write("\\end{vmatrix} = ")
                    f.write(f"{latex(matriz3.det())} \\neq 0")
                    f.write("$$\n\n")
                    f.write("Esto implica que Rg(A*) = 3 $>$ Rg(A). Por tanto, seg\\'un el teorema de Rouch\\'e-Frobenius, el sistema es incompatible.\\\\\n\n")  

            else:
                print("Si a = $",latex(soluciones[l]),"$")
                f.write(f"Adem\\'as, el Rg(A*) = Rg(A) = {RgA} ya que no encontramos ning\\'un menor {RgA+1}x{RgA+1} distinto de 0 en la matriz ampliada. ")
                f.write("Empleando el teorema de Rouch\\'e-Frobenius, ya que Rg(A) = Rg(A*) $\\neq$ n$^{\\text{o}}$ inc\\'ognitas = 3, concluimos que el sistema es compatible indeterminado")
                f.write(f"de orden {3-RgA}.\n\n")
                f.write("Para encontrar la soluci\\'on vamos a hacer Gauss por filas. \n")
                print(matriz_evaluada)
                # Aplica el metodo de eliminacion de Gauss por filas (sin pivoteo parcial)
                cambios=0
                
                f.write("$$\n")
                f.write("\\left(\\begin{array}{ccc|c}")
                f.write(f"{latex(matriz_evaluada[0,0])} & {latex(matriz_evaluada[0,1])} & {latex(matriz_evaluada[0,2])} & {latex(terminos_independientes_evaluados[0])} \\\\")
                f.write(f"{latex(matriz_evaluada[1,0])} & {latex(matriz_evaluada[1,1])} & {latex(matriz_evaluada[1,2])} & {latex(terminos_independientes_evaluados[1])}\\\\")
                f.write(f"{latex(matriz_evaluada[2,0])} & {latex(matriz_evaluada[2,1])} & {latex(matriz_evaluada[2,2])} & {latex(terminos_independientes_evaluados[2])}")
                f.write("\\end{array}\\right)")
                cambios+=1
                for i in range(3):
                    # Verifica si el pivote es cero y, en ese caso, intercambia con otra fila
                    if matriz_evaluada[i, i] == 0:
                        fila_intercambio = None
                        for j in range(i + 1, 3):
                            if matriz_evaluada[j, i] != 0:
                                fila_intercambio = j
                                break

                        if fila_intercambio is not None:
                            matriz_evaluada.row_swap(i, fila_intercambio)
                            aux=terminos_independientes_evaluados[i]
                            terminos_independientes_evaluados[i]=terminos_independientes_evaluados[fila_intercambio]
                            terminos_independientes_evaluados[fila_intercambio]=aux
                            f.write("\\xrightarrow{")
                            f.write(f"F_{i+1}\\leftrightarrow F_{fila_intercambio+1}")
                            f.write("}")
                            f.write("\\left(\\begin{array}{ccc|c}")
                            f.write(f"{latex(matriz_evaluada[0,0])} & {latex(matriz_evaluada[0,1])} & {latex(matriz_evaluada[0,2])} & {latex(terminos_independientes_evaluados[0])} \\\\")
                            f.write(f"{latex(matriz_evaluada[1,0])} & {latex(matriz_evaluada[1,1])} & {latex(matriz_evaluada[1,2])} & {latex(terminos_independientes_evaluados[1])}\\\\")
                            f.write(f"{latex(matriz_evaluada[2,0])} & {latex(matriz_evaluada[2,1])} & {latex(matriz_evaluada[2,2])} & {latex(terminos_independientes_evaluados[2])}")
                            f.write("\\end{array}\\right)")
                            cambios+=1
                            if cambios >= 3:
                                f.write("$$\n$$")
                                cambios=0
                            print(f"Intercambio Fila {i+1} y Fila {fila_intercambio+1}:")
                            print(matriz_evaluada)
                        else:
                            #print(f"No se encontro un elemento no nulo en la columna {i+1}. Saltando a siguiente columna...")
                            continue

                    # Eliminacion hacia adelante
                    for j in range(i + 1, 3):
                        factor = matriz_evaluada[j, i] / matriz_evaluada[i, i]
                        matriz_evaluada[j, :] -= factor * matriz_evaluada[i, :]
                        terminos_independientes_evaluados[j] -= factor * terminos_independientes_evaluados[i]
                        if factor != 0:
                            f.write("\\xrightarrow{")
                            if factor < 0:
                                f.write(f"F_{j+1}\\to F_{j+1}+{latex(abs(factor))}F_{i+1}")
                            else:
                                f.write(f"F_{j+1}\\to F_{j+1}-{latex(factor)}F_{i+1}")
                            f.write("}")
                            f.write("\\left(\\begin{array}{ccc|c}")
                            f.write(f"{latex(matriz_evaluada[0,0])} & {latex(matriz_evaluada[0,1])} & {latex(matriz_evaluada[0,2])} & {latex(terminos_independientes_evaluados[0])} \\\\")
                            f.write(f"{latex(matriz_evaluada[1,0])} & {latex(matriz_evaluada[1,1])} & {latex(matriz_evaluada[1,2])} & {latex(terminos_independientes_evaluados[1])}\\\\")
                            f.write(f"{latex(matriz_evaluada[2,0])} & {latex(matriz_evaluada[2,1])} & {latex(matriz_evaluada[2,2])} & {latex(terminos_independientes_evaluados[2])}")
                            f.write("\\end{array}\\right)")
                            cambios+=1
                            if cambios >= 3:
                                f.write("$$\n$$")
                                cambios=0
                        print(f"Eliminacion hacia adelante - Fila {j+1} - Factor: {factor}:")
                        print(matriz_evaluada)
                f.write("$$\n\n")

                # Imprime la matriz escalonada resultante
                #print("Matriz escalonada:")
                #print(matriz_evaluada)
                
                f.write("Con la matriz escalonada es trivial obtener la soluci\\'on al sistema: ")
                ecuaciones = []
                sols = []

                # Construye las ecuaciones utilizando los coeficientes y terminos independientes
                for i in range(3):
                    ecuacion = Eq(matriz_evaluada[i, 0]*x + matriz_evaluada[i, 1]*y + matriz_evaluada[i, 2]*z, terminos_independientes_evaluados[i])
                    ecuaciones.append(ecuacion)

                # Resuelve el sistema de ecuaciones
                sol = solve(ecuaciones)
                
                #print("Las soluciones parametricas del sistema son:")
                var = {x,y,z}
                varsol = set()
                for v in var:
                    if v in sol:
                        varsol.add(v)
                ha = var-varsol

                cnt = 0
                for h in ha:
                    if cnt==0:
                        subst = λ
                    elif cnt == 1:
                        subst = μ
                    else:
                        subst = φ
                    sol[h] = subst

                    for v in varsol:
                        try:
                            sol[v] = sol[v].subs(h,subst)
                            cnt+=1
                        except:
                            pass
                
                
                # Mostrar las soluciones
                
                solucion_x=latex(sol[x]).replace("λ", "\\lambda")
                solucion_y=latex(sol[y]).replace("λ", "\\lambda")
                solucion_z=latex(sol[z]).replace("λ", "\\lambda")
                solucion_x=solucion_x.replace("μ", "\\mu")
                solucion_y=solucion_y.replace("μ", "\\mu")
                solucion_z=solucion_z.replace("μ", "\\mu")
                solucion_x=solucion_x.replace("φ", "\\varphi")
                solucion_y=solucion_y.replace("φ", "\\varphi")
                solucion_z=solucion_z.replace("φ", "\\varphi")
                
                f.write("$$\n")
                f.write("\\left\\{\\begin{array}{lll}")
                f.write(f"x = {solucion_x}\\\\ y = {solucion_y}\\\\ z = {solucion_z}")
                f.write("\\end{array}\\right.")
                f.write("$$\\\\\n\n")
    f.write("\n\\end{document}")
    

