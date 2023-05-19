# Pluto24 Language
Pluto24 is a highly customizable programming language, written in just **24 lines** of code.

## Syntax
```
<digit> => pushed to stack
<*:>    => function declaration
<&*>    => function reference
<:>     => comment (function with no name)
<*>     => calls the function
```

## Basic program
```
: declares a function `add5`
add5: 5 add : adds 5 to last element of the stack

: program entry point
main: 10 add5 : calls add5 with argument 10

: stack should be [15] after running the program
```

## Builtin functions
```
add  => adds two integers
sub  => subtracts two integers
mul  => multiplies two integers
div  => divides two integers, using integer division
mod  => modulus of two integers
copy => copy element at nth index
drop => drop element at nth index
if   => runs the function(at 1) if condition(at 2) > 0
get  => reads a single byte into the stack
put  => prints a single byte from the stack
```

## Running Pluto programs
```console
$ python main.py <program.pluto, ...>
```

## Running examples
Programs under `/example` assumes `std.pluto` is included

```console
$ python main.py std.pluto example/hello.pluto
```

## std.pluto
This is an optional pluto library, which contains commonly used functions.

## operators.pluto
This library contains function alias as operators, enables the usage of operators
instead of keywords to use e.g. `1 2 +` instead of `1 2 add`

Example of `sum.pluto` using `operators.pluto`
```
sum: sum.run 1 --
sum.run: 1 - 1 ++ &sum.add ?
sum.add: <-> 3 ++ + 3 -- <-> sum.run
```
