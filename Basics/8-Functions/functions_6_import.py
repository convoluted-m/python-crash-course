### Importing functions from other files

## Import a whole module from another file (bouquet.py)
import bouquet
# Pass values into the function. Use module name folowed by dot and function name.
bouquet.make_bouquet('small', 'lillies' )
bouquet.make_bouquet('medium', 'lilacs')

## Import only a function
from bouquet import make_bouquet
# Pass values into the function. No need for the module name.
make_bouquet('large', 'sunflowers' )

## Importing a function with an alias
from bouquet import make_bouquet as arrange
# Pass values
arrange('small', 'cornflowers' )

## Import all functions in a module with *
from bouquet import *
make_bouquet('large', 'asters' )




