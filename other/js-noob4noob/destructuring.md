# (noob) => { return noob } JS
## Destructuring

Welcome back to "for noobs by a noob". In this article, I'll be talking about one of the coolest yet most confusing looking ES6 syntax: Array Destructuring (and objects!). 

**I encourage you to open your browser's console and plant some snippets in to follow along and test with!**

The purpose of array destructuring is to solve code in your codebase that may look like the following...

```js
userStore = {
   310: ["PLAYER", "Dylan", "Druid", "Balance", "120", "433"]
}
// ...
function getUserInformation(id) {
  return Object.values(this.userStore[id]);
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

## The Basics / FAQ

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

 * In the first case, we will simply ignore the presence of the third value and get `b = 1, c = 2`. The 3 is discarded. 
 * In the second case, we will return undefined for the fields that do not exist. So we'd get `d = 1, e = 2, f = 3, g = undefined`.
 
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
