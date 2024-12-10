let cherche x tab =
let n = Array . length tab in
let rec auxCh a b =
if a = b
then tab .( a ) = x
else let c = ( a + b ) /2 in
if tabl .( c ) < x
then auxCh ( c +1) b
else auxCh a c in
aux 0 (n -1) ;;
