# (noob) => { return noob } JS
## ES6 Variable Types

Welcome to the first installment of  "for noobs by a noob", where I (a fellow noob) will teach you concepts that I learned, while I learned them. In this article we will discuss one of the most important introductory (and moderately annoying when working with old code that has a linter recently activated) aspects of JavaScript -- **ES6 variable types**.

And also your first taste into another of the more important JS concepts: **scope**.

If you're working with a corporate codebase using an automatic linter (eslint, sonarqube), you may find yourself being told to eradicate every var declaration off the face of the planet. Well, in most cases, they're not wrong. However, var *does* have some differences.

## What is `const` and `let`?

`const` and `let` are the new variable types introduced with ES6, they represent what many consider to be "traditional" variables where the following apply:

 * `const` is a "static" variable in which it cannot be reassigned once declared. This does **not** mean the value is immutable though.
 * Once a variable is defined with `let`, you cannot redeclare that variable.

```js
// valid
var a = 53;
var a = 97;

// invalid
let a = 53;
let a = 97;
```

 * Both `const` and `let` are "block-scoped" variables. This means that they can only be accessed within the scope that they were defined, whereas `var` can be accessed outside of the scope.

## Block Scope

The main difference between the ES6 var types and the old `var` is block scoping. Take a look at the following code snippet:

```js
let a = 35;
if (...) {
  // a is accessible in here
  let b = a;
}
// b is NOT accessible here
```

Valid scope is defined as the level in which declaration occurred as well as any blocks that nest deeper from the point declaration occurred. In the block above, if you wanted to be use `b` after assigning it a conditional value in the `if` block, then you must declare it outside of the `if` block, then assign it within.

```js
let a = 35, b; // define b here
if (...) {
  b = a;
}
// b is now accessible here.
```

However, `var` does not work like this.

```js
if (...) {
  var b = 35;
}
// b is accessible here
```

That is to say, if you want a value that is accessible regardless of scope, you **can** use `var`. The other use case is if you are in a long string of code and you wish to re-declare the variable for the sake of clarity, you should use `var` as well. For example,

<details><summary>Code snippet</summary>
<p>
  
```js
var a = 3;
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
// ...
var a = 7; // redeclaration for clarity
```

</p>
</details>
