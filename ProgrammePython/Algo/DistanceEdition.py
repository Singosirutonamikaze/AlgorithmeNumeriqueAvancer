def de_sol ( ch1 , ch2 ) :
    n1 , n2 =len( ch1 ) ,len( ch2 )
    T = de_tab ( ch1 , ch2 ) # fonction identique à de_bas_haut mais qui renvoie le tableau complet et non la dernière valeur
    dep =[]
    i , j = n1 , n2
    while i >0 and j >0: # tant qu ’on n’a pas atteint la 1 ière ligne ou la 1ière colonne
# on cherche l’opération qui coûte le moins ,
if T [i -1][ j -1]== T [ i ][ j ] -1:
op = f" substitution de { ch1 [i -1]} par { ch2 [j -1]} "
i , j =i -1 ,j -1
 dep . append ((1 ,1 , op ))
 elif T [i -1][ j ]== T [ i ][ j ] -1:
op = f" suppression de { ch1 [i -1]} "
i =i -1 # vers le haut
dep . append ((1 ,0 , op ))
elif T [ i ][ j -1]== T [ i ][ j ] -1:
 op = f" insertion de { ch2 [j -1]} "
 j =j -1 # vers la gauche
 dep . append ((0 ,1 , op ))
 elif T [i -1][ j -1]== T [ i ][ j ]: # aucun changement à effectuer
 op = f"{ ch1 [i -1]} inchangé "
22 i , j =i -1 ,j -1
23 dep . append ((1 ,1 , op ) )
24 while j !=0: # i=0 , on est dans la 1 ière ligne
25 op = f" insertion de { ch2 [j -1]} "
26 j =j -1 # vers la gauche
27 dep . append ((0 ,1 , op ) )
28 while i !=0: # j=0 , on est dans la 1 ière colonne
29 op = f" suppression de { ch1 [i -1]} "
30 i =i -1 # vers le haut
31 dep . append ((1 ,0 , op ) )
32 # 3è étape : solution
33 dep = dep [:: -1] # on inverse la liste des opérations
34 sol =[]
35 i , j =0 ,0
36 for k in range (len( dep ) ) :
37 di , dj , op = dep [ k ]
38 i = i + di
39 j = j + dj
40 sol . append ( op )
41 return sol
42 >>> de_sol (" chien "," niche ")
43 [’insertion de n’, ’insertion de i’, ’c inchangé ’, ’h inchangé ’, ’
suppression de i’, ’e inchangé ’, ’ suppression de n’]
44 >>> de_sol (" chien "," niches ")
45 [’insertion de n’, ’insertion de i’, ’c inchangé ’, ’h inchangé ’, ’
suppression de i’, ’e inchangé ’, ’ substitution de n par s’]
46 >>> de_sol (" carotte "," patate ")
47 [’ substitution de c par p’, ’a inchangé ’, ’ substitution de r par t’, ’
substitution de o par a’, ’t inchangé ’, ’ suppression de t’, ’e inchangé ’]