#Approach

There are a few things going on here to understand. 

Hoisting and how JavaScript Builds its execution Environment:

JavaScript builds its execution environment in two passes

First the declaration pass sets up the runtime environment, scanning all variable and function delcarations and creating identifiers.

Second pass is the execution pass.


Function expressions vs. Function declarations.

A function expression is the use of declaring a variable and setting that variable to a function.

This is useful tool for creating lambda functions.

Note that they are different than function declarations and will be hoisted like a variable not like a function declaration.
