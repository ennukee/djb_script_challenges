# (noob) => { return noob } JS
## Array Destructuring

Welcome back to "for noobs by a noob", where I (a fellow noob) will teach you concepts that I learned, while I learned them. In this article, I'll be talking about one of the coolest yet most confusing looking ES6 syntax: Array Destructuring (and objects in a later article). 

**I encourage you to open your browser's console and plant some snippets in to follow along and test with!**

The purpose of array destructuring is to solve code in your codebase that may look like the following...

```js
userStore = {
   310: ["PLAYER", "Dylan", "Druid", "Balance", "120", "433"]
}
// ...
function getUserInformation(id) {
  return this.userStore[id];
}

function userString(id) {
  const userInfo = getUserInformation(310);
  const name = userInfo[1];
  const class = userInfo[2];
  const level = userInfo[3];
  return `${name} - ${level} ${class}`
}

// ...
userString(310)
```

In particular, we are looking at the code 
```js
  const userInfo = getUserInformation(310);
  const name = userInfo[1];
  const class = userInfo[2];
  const level = userInfo[3];
```

## How is it done?

In array destructuring, we can skip this code spaghetti and assign directly the values we are looking for, assuming we know the format of the code being returned to us. Let us dive into a super simplistic example before we return to the above code.

```js
let a = [1, 2, 3, 4, 5]
```

If we wanted to access and utilize the values at index 1, 3 and 4, how would we go about doing that? Well, pre-ES6 we would simply access each index and assign its own variable (i.e. `var b = a[1], c = a[3], d = a[4]`). However, in ES6 we can utilize array destructuring to easily do this from the first line. You could replace the 2-4 lines of code needed above with simply...

```js
let [, b, , c, d] = [1, 2, 3, 4, 5];
```

The whitespace here is for readability reasons, you could also easily write `let [,b,,c,d]` instead. Welcome to the future.

## The Syntax / FAQ

Now that we've seen it used, let's talk about it and its common confusions.

### What happens if the array is too big/small?

I'm assuming what you're asking is what happens if either of the following were to occur:

```js
let a = [1, 2, 3];

// What happens in these two cases?
let [b, c] = a; 
let [d, e, f, g] = a;
```

Does this throw any errors? Issues at all? **Nope**. 

 * In the first case, we will simply ignore the presence of the third value and get `b = 1, c = 2`. The 3 is discarded. **Unaccounted-for values are ignored**.
 * In the second case, we will return undefined for the fields that do not exist. So we'd get `d = 1, e = 2, f = 3, g = undefined`. **Overly-accounted-for variables will be given undefined** (or their default zero value, like \[\] or {})

### Skipping items?

We saw it in the first example, but you can skip items **by writing nothing where there would otherwise be a variable**. So,

```js
let [a, b, c] = [1, 2, 3]
// If you don't care for 2...
let [a, , c] = [1, 2, 3]
```

I recommend maintaining whitespace, as it helps readability and understanding when viewing this.

### What if we have an unknown length array and we want all items past a point?
 
This uses a concept that you may have seen in function declarations called the **gather** operator. Otherwise known as the **spread** operator under different cases. [See my article on this here](#).
 
Just as quick rundown for this operator, it is used to either **gather** extra items or **spread** out an array of items. Some use cases:
 
```js
let a = [1, 2, 3]
function b(c, ...d) {
   return d // [2, 3]
}
b(...a) // b(1, 2, 3)
```

This is the same syntax used for gathering values in a destructuring. As usual, it must be at the **end** of the structuring. 
```js
let a = [1, 2, 3]
let [b, ...c] = a;
// b = 1
// c = [2, 3]
```

Keep in mind that this gather operation **will always be an array regardless of match count**. So, for example...

```js
let a = [1, 2, 3]
let [b, c, d, ...e] = a;
// b = 1, c = 2, d = 3, e = []
// ...
let [b, c, ...d] = a;
// b = 1, c = 2, d = [3]
```

### Default values

If you've ever set a default value for a function parameter, you'll get this quite quickly. For this, all you must do is apply an `= default_value` to the right of the variable you want a default value for. For example,

```js
let [b, c, d = 5] = [1]
// b = 1, c = undefined, d = 5
```

You can also do this for the rest operator to prevent the empty array case.

```js
let [b, c, d = [1, 2, 3]] = [5];
// b = 5, c = undefined, d = [1, 2, 3]
```

## Underlying Code

### State Preservation

One thing many people skip over is the underlying code involved in this operation.

Firstly, the state of the operation is preserved prior to the assignments. That is to say, you can swap values or do something with data you want to keep but also reassign the variable for early on. For example,

```js
let a = 3, b = 5;
[a, b] = [b, a] // b = 5, a = 3

let a = 3, b = 4, c = 5, d = 6;
[a, b, c, d] = [d, a, a, a]
// Even though a = d is the first "connection", all of b, c, d will be assigned the old value of a
// a = 6, b = c = d = 3
```

### Return value / Triggering the syntax

Imagine you run into the following code at work:

```js
let a = [b, c, d] = [1, 2, 3, 4, 5, 6]
```

What does this return? What are the values of a, b, c and d? I'll give you a minute. Scroll down when you're ready to go on.

Before I reveal the answer, ask yourself, is this valid syntax? We have an array-looking item in the middle of a two-pronged assignment operation. Well, **it is valid**. The item in the middle is not actually an array object, it's a destructuring assignment. As long as this destructuring syntax is on the receiving end of an assignment operation (i.e. on the left side of an equals), it will trigger destructuring.

Now... what *are* the values of a, b, c and d then? The only real confusing bit is what `a` will end up as, it should be relatively straight-forward that `b = 1, c = 2, d = 3`. So, is `a = [1, 2, 3]` or is `a = [1, 2, 3, 4, 5, 6]`? If you said the latter, you would be correct. The return value of a destructuring operation is not the destructured array but rather the original array that was destructured.

**However**, keep in mind that variables in the second step of this destructuring will actually need to be pre-defined before being used. So in actuality, my snippet above isn't entirely valid since I never wrote out the variable definitions of b, c or d. The correct statement would be:

```js
let b, c, d;
let a = [b, c, d] = [1, 2, 3, 4, 5, 6];
```

## Wrapping it back around

Now that we've gone through all the fundamental information we need to know for array destructuring, let us return to the original example. For the following code, how would you rewrite it using destructuring?

<details><summary>Original code</summary>
<p>
   
```js
function userString(id) {
  const userInfo = getUserInformation(310);
  const name = userInfo[1];
  const class = userInfo[2];
  const level = userInfo[3];
  return `${name} - ${level} ${class}`
}
```

</p>
</details>

<details><summary>Answer</summary>
<p>
   
```js
function userString(id) {
  const [, name, class, level] = getUserInformation(310);
  return `${name} - ${level} ${class}`
}
```

</p>   
</details>

## Closing 

Thanks for reading `(noob) => { return noob }` and if you liked the blog make sure to follow the Twitter at @ennukee for more code nerdings.
