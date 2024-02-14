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
![basic](https://github.com/DrLoopFall/Pluto24/assets/120749263/814db245-63e0-414c-95b8-b39f3dec7ccd)
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
instead of keywords to use e.g. `1 2 +` instead of `1 2 add`

## Examples
### [hello.pluto](/examples/hello.pluto)
![hello](https://github.com/DrLoopFall/Pluto24/assets/120749263/d4a517ba-4402-4699-a7d3-6aea180403cc)

### [fib.pluto](/examples/fib.pluto)
![fib](https://github.com/DrLoopFall/Pluto24/assets/120749263/b11c6dcc-f75a-420c-92fc-39e9903159e2)

### [max.pluto](/examples/max.pluto)
![max](https://github.com/DrLoopFall/Pluto24/assets/120749263/5ef76d25-b22d-4f0e-9d3a-979cb7bcd5fb)

### [sum.pluto](/examples/sum.pluto)
![sum](https://github.com/DrLoopFall/Pluto24/assets/120749263/b5dea694-18f3-4523-b771-c830a219c740)

### [operators_sum.pluto](/examples/operators_sum.pluto)
![operators_sum](https://github.com/DrLoopFall/Pluto24/assets/120749263/b6300620-e31c-4d8a-996a-0067b2e89661)
