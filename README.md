# Pluto24 Language
Pluto24 is a highly customizable programming language, written in just **24 lines** of code.

## Syntax
```ats
<digit> => pushed to stack
<*:>    => function declaration
<&*>    => function reference
<:>     => comment (nameless function)
<*>     => calls the function
```


## Basic program
![basic](https://github.com/DrLoopFall/Pluto24/assets/120749263/c657fdbb-ff35-440b-86a9-c4245b5ca514)
Source [basic.pluto](/examples/basic.pluto)

## Builtin functions
```perl
add  => adds two integers
sub  => subtracts two integers
mul  => multiplies two integers
div  => divides two integers, using integer division
mod  => modulus of two integers
copy => copies the nth element
drop => drops the nth element
if   => runs the function(at 1) if condition(at 2) > 0
get  => reads a single byte into the stack
put  => prints a single byte from the stack
```

## Running Pluto programs
```console
$ python main.py <program.pluto, ...>
```

## Running examples
Programs under `/examples` assumes `std.pluto` is included

```console
$ python main.py std.pluto examples/hello.pluto
```

## std.pluto
This is an optional pluto library, which contains commonly used functions.

## operators.pluto
This library contains function alias as operators, enables the usage of operators
instead of keywords.

e.g. `1 2 add` => `1 2 +`

## Examples
### [hello.pluto](/examples/hello.pluto)
![hello](https://github.com/DrLoopFall/Pluto24/assets/120749263/371f4009-42ca-4d5e-b488-e51b37038ef7)

### [fib.pluto](/examples/fib.pluto)
![fib](https://github.com/DrLoopFall/Pluto24/assets/120749263/27305dfe-9d6c-4d56-afaf-16858e735c60)

### [max.pluto](/examples/max.pluto)
![max](https://github.com/DrLoopFall/Pluto24/assets/120749263/dbe81d07-12d9-47da-9ff2-4451581a9e21)

### [sum.pluto](/examples/sum.pluto)
![sum](https://github.com/DrLoopFall/Pluto24/assets/120749263/c933ce32-596c-4976-83e2-0e5df40efcba)

### [operators_sum.pluto](/examples/operators_sum.pluto)
![operators_sum](https://github.com/DrLoopFall/Pluto24/assets/120749263/a2709749-f9e3-4bf1-b3dd-051aaebc5cb4)
