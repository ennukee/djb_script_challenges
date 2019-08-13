# (noob) => { return noob } JS
## How to reverse a string

There are a multitude of ways to do this, but my favorite way reverse a string in ES6 is to abuse the spread operator to convert a string to an array, then apply a reverse and join on it, like the following:

```js
let any_string = "SOME_STRING_VALUE";
let reversed_string = [...any_string].reverse().join('');
```

You can also do this with a few other "splitting" operations, like..

```js
let reversed_string = any_string.split('').reverse().join('');
let reversed_string = Array.from(any_string).reverse().join('');
```

Thanks for reading `(noob) => { return noob }` and if you liked the blog make sure to follow the Twitter at @ennukee for more code nerdings.
