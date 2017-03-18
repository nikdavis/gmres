I have two issues:
 - not setting up from_mm matrix right -> a is empty
 - Gmres is breaking down due to xn being out of dimension with pn
     on overconstrained matrices
 - review Gmres, htw do we do it with overconstrained matrices -- moar qr?
