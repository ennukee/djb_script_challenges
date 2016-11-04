# CS311 Homework #4
### Dylan Bowers (collab w/ Nikolai Narma, Chris Jones, Joe Isble, Craig Norton)

## Question 1

Assumptions: `cs` = Current Sum (subsequence). `la` = Last added (to `cs`). `rs` = Remaining set (of stuff that can be added). We will also assume if a base case if a call is made where `cs` is not empty and `la` is not nothing (i.e. `MSS([1,2],None,[3,4,5])`) then the recursive call will terminate with the sum of `cs`. There is also another base case in which `rs` is empty, in which you return the sum of `cs` as well.

For some set of values `set`, the recursive form for the Maximum Subsequence Sum (MSS) is...
```
MSS(cs, la, rs) = 
  max( 
    MSS(cs append set[0], set[0], set[1:]), 
    MSS(cs, None, set[1:]) 
  )
```

The resulting logic of the recursive calls will evaluate to two full gloss-overs of the `set`. O(2n) is still O(n), so the runtime remains as O(n).

*The syntax set[n:] means "all values at index n and forward, so if set = [1,2,3,4] then set[1:] = [2,3,4]*

(I really hope this question doesn't require a big explanation, I'm not sure what else to put here)

## Question 2

**Algorithm**

```
given a set of tasks S
sort S in descending order

let S1 be an empty array of tasks for machine 1
let S2 be an empty array of tasks for machine 2
active, inactive = S1, S2
for each task T in S
  add T to active
  if sum(active) > sum(inactive)
    swap active and inactive
  endif
endfor
return S1, S2
```

**Explanation**: Sort by largest size, add to each machine until it passes the other (strictly passes), then swap machines. Repeat this swapping until all tasks have been assigned. This algorithm works by minimizing the "gap" between the two machines, keeping their endpoints as close as possible. By doing this, you efficiently split the work  between the two machines and result in the shortest overall time possible.

**Runtime**: Sorting will take O(nlogn) runtime. The runtime of the algorithm portion is O(n), but because of the sort, the overall runtime of the algorithm is **O(nlogn)**. If we are under the assumption that set S has lengths `x1, x2, ..., xn` such that `x1 >= x2 >= ... >= xn` (i.e. the set S is already pre-sorted) then the algorithm is O(n)

## Question 3

**Algorithm**

```
m = 0
s = ""
for each character C in X:
  if the number of remaining characters in X <= m:
    return m
  for each character K in Y:
    length = 0
    str = ""
    while C = K
      increment to the next letter, add to length
      add C to str
    endwhile
    if length > m:
      s = str
      m = length
    endif
  endfor
  change C to whatever character is after the longest substring found for C
endfor
return m, s
```

**Explanation**: Iterate over X, for each character in X, iterate over Y. If it finds a matching character, begin incrementing indices on both until the characters are different. Record the number it incremented to and store it if it's higher than the last. Continue on whatever character you ended on.

For example: QABCDE vs ZABCEF, Q iteration finds nothing. A finds 'ABC' (store 3). Now we're on D, but since there's only 'DE' left to check and that is 2, which is <= 3 (the known longest), we stop.

**Runtime**: As expected, O(nm) in the case of there being no viable at all / length 1 substrings only.

## Question 4

I will be approaching this problem with the goal of maximizing the difference between the possible gains as a result of your move.

**Algorithm 1**

```
ASSUMPTIONS
 > turn = 0 means that it is Akshay's turn
 > turn = 1 means that it is Andrew's turn
 > `ak_gain` param refers to "Akshay's Total Gain" from that path
 > `an_gain` param refers to "Andrew's Total Gain" from that path

given a state_table ST
algorithm(ak_gain, an_gain, turn, remaining_set)
  L = length of remaining_set
  if the remaining set is empty
    return difference of ak_gain and an_gain
  endif
  
  if turn == 0 (akshay's turn)
    recurse on the two situations where akshay picks the front or end
    compare these two, pick the instance that is more of a gain
    if ST[remaining_set] doesn't exist yet or larger > known state in ST:
      ST[remaining_set] = (gain, the move that resulted in larger)
    endif
    
    return the most beneficial between the two recursion (for akshay)
  
  else (andrew's turn)
    recurse on the two situations where andrew picks the front or end
    compare these two, pick the instance that is more of a gain
    if ST[remaining_set] doesn't exist yet or larger > known state in ST:
      ST[remaining_set] = (gain, the move that resulted in larger)
    endif
  endif
endalgorithm

give state_table to Akshay
```

**Explanation**: This will recursively check down all viable paths, storing the result of each recursion IFF it is larger than the max known state (it also stores the move that resulted in it). It will consider **all** states because it will also store "Andrew's best move" (by inversing comparatives) which in reality would Akshay's best move if the order of first-turns got reversed.

**Runtime**: O(n^2), as requested by the problem. Each state will recurse on a scaling set of remaining states, resulting in ultimately a O(n^2) runtime.

Here is an example of this algorithm implemented in Python (though not perfect, it's getting there)

```py
state_table = {}
def algorithm1(ak_gain, an_gain, turn, remaining_set):
    print('{}, {}, {}'.format(ak_gain, an_gain, turn, remaining_set))
    L = len(remaining_set)
    if remaining_set == []:
        return ak_gain - an_gain

    if turn == 0:
        if_front = algorithm1(
            ak_gain + remaining_set[0],
            an_gain,
            (turn + 1) % 2,
            remaining_set[1:]
        )
        if_end = algorithm1(
            ak_gain + remaining_set[L - 1],
            an_gain,
            (turn + 1) % 2,
            remaining_set[:L-1]
        )
        print('>{}, {}'.format(if_front, if_end))

        cur_move = state_table.get(str(remaining_set), None)
        better_move = (if_front, 'Front') if if_front > if_end else (if_end, 'End')
        if not cur_move or better_move[0] > cur_move[0]:
            state_table[str(remaining_set)] = better_move

        return max(if_front, if_end)
    else:
        # Conditional comparators are reversed in this case because
        # our end result is based on akshay - andrew, so we want the
        # lowest value here.

        if_front = algorithm1(
            ak_gain,
            an_gain + remaining_set[0],
            (turn + 1) % 2,
            remaining_set[1:]
        )
        if_end = algorithm1(
            ak_gain,
            an_gain + remaining_set[L-1],
            (turn + 1) % 2,
            remaining_set[:L-1]
        )

        cur_move = state_table.get(str(remaining_set), None)
        better_move = (if_front, 'Front') if if_front < if_end else (if_end, 'End')
        if not cur_move or better_move[0] < cur_move[0]:
            state_table[str(remaining_set)] = better_move

        return min(if_front, if_end)

algorithm1(0, 0, 0, [5, 3, 7, 15, 5])
print(state_table)

# Output (you can ignore the first numbers, just pay attn to state and move)
# {'[15]': (19, 'End'), '[5, 3, 7, 15]': (-5, 'End'),
#  '[5]': (-1, 'End'), '[15, 5]': (-1, 'Front'),
#  '[3, 7, 15, 5]': (-1, 'Front'), '[7, 15, 5]': (-1, 'End'),
#  '[3]': (11, 'End'), '[7, 15]': (-5, 'End'),
#  '[3, 7, 15]': (11, 'End'), '[7]': (19, 'End'),
#  '[5, 3]': (-5, 'Front'), '[5, 3, 7, 15, 5]': (-1, 'Front'),
#  '[5, 3, 7]': (-5, 'End'), '[3, 7]': (-9, 'End')}
```

**Algorithm 2**

```
given a set S of denominations and the algorithm defined above
optimal_moves = algorithm1(0, 0, 0, S) 
We assume the above takes no runtime as per the project description

If Akshay simply does optimal_moves[STATE_OF_BOARD], then it will return a tuple including the optimal move.
```

**Explanation**: Accesses a hash generated by the first algorithm written and returns the desired move. 

**Runtime**: O(1), as hash accessing is only O(1). This is also the desired run-time by the problem description.

## Question 5

### Part (a)

We want the most commonly accessed keys to be the quickest to be reached (aka the top of the tree). So an optimal tree for this case would be

```
    x3
   /  \
  x2  x4
 /
x1
```

This will result in 3\*1 + 4\*2 + 6\*2 + 2\*3 = 3 + 8 + 12 + 6 = cost of 29. This is achieved from looking at all viable permutations of the node set and selecting the lowest possible one.

### Part (b)

Source used to help solve: `https://www.youtube.com/watch?v=u5eSBQQ4qVc`

This problem can be solved using **proof by contradiction**. If we say that either of the subtrees, L or R, are actually not an optimal MST we can go through the problem to eventually come out to a formula that contradicts the optimality of the entire tree.

We can define the cost of a tree to be the summation over all of its nodes, multiplying the the weight of the node `n` by `1 + distance to root node`. (i.e. `sum(i = 1 to n) weight(i) * (1 + distance to root)`). If we abstract this to our problem, which  has a root and two subtrees specified, we can say that the cost of this is equivalent to `weight of root + cost of L + cost of R`. If we go to say that either L or R are actually suboptimal, then that's equivalently saying that the entire tree is suboptimal, which contradicts the known optimality of the tree. This is because by saying one of the subtree is suboptimal, it is equally saying that the entire tree is suboptimal because the cost of the new tree would go down as a whole compared to the original tree.

### Part (c)

*The syntax set[n:] means "all values at index n and forward, so if set = [1,2,3,4] then set[1:] = [2,3,4]. Similarly, set[:n] is "up to but not including index n" so set[:3] of [1,2,3,4] is [1,2,3]*

```
algorithm(set, depth, current_tree)
  if set is empty
    return 0, current_tree
  endif
  
  min = 0, (empty tree)
  for i = 0 to length of set - 1
    r = cost of node set[i]*depth
        + algorithm(set[0:i], depth+1, (add node to tree structure))
        + algorithm(set[i+1:], depth+1, (add node to tree structure))
    if r[0] < min[0]
      min = r[0], r[1]
    endif
  endfor
  return min
end
```

**Explanation**: It will go through every possible situation for "root" nodes and then it will recurse on the resulting sub-trees (as it is in sorted order already). Because we know that the subtrees also have to be optimal, we recurse on those subtrees using the same algorithm. Eventually it will stem down to leaves for all scenarios and build its way back, prioritizing the optimal trees via `min`. At the end, it will return a large master tree that resulted in the optimal BST.

**Runtime**: O(n^3) due to the recursive O(n^2) calls and the initial O(n) for-loop causing an O(n^2) recursive call in each, resulting in O(n)O(n^2) = **O(n^3)**.

### Part (d)

It would depend on whether or not I knew my approach to 5c was right so I could look at improving the runtime from there.

## Question 6

### Part (a)

```
given an answer set y
for each node X in x
  append x to answer set y
endfor
return y
```

**Explanation**: Because the groupings do not matter (as the sum(s in S) |s| is always the length of the array), you can just return the same list that you were given.

**Runtime**: O(n) as you are doing an O(n) iteration over x and an O(1) action in which you append it to y, making an O(n)O(1) = **O(n)** total runtime.

### Part (b)

**Assumptions**
 * `c_sets` is a 2D array of the current groupings
 * `r_set` is the remaining values left to work with
 * The syntax set[n:] means "all values at index n and forward, so if set = [1,2,3,4] then set[1:] = [2,3,4]
 * The difference between `extend` and `append` is that `extend` adds an array where `append` adds a value. So in the situation of a value `a = [[1,2,3],[4,5]]` we say `a append 6` creates `[[1,2,3],[4,5,6]]` where `a extend 6` creates `[[1,2,3],[4,5],[6]]`
 * `min` evaluates based on the first available comparable value (in this case, it is `c`)
 * If a recursive call that `append`s `r_set[0]` will increase the average distance to be greater than the size of the set, then we will not consider the call as it will cause the grouping to have a negative impact.

```
algorithm(c_sets, r_set)
  if r_set is empty:
    c = 0
    for subset in c_sets
      avg = average of subset
      for each val in subset
        c += (val - avg)^2
        val = avg
      endfor
      c -= (size of subset)^2
    endfor
    
    return c, flatten(c_sets)
  endif
  
  return min(
    algorithm(
      c_sets append r_set[0]
      r_set[1:]
    ),
    algorithm(
      c_sets extend r_set[0],
      r_set[1:]
    )
  )
end
```

**Explanation**: This will recurse over possible combinations of groupings, ignoring blatant wrong ones (as per the assumptions). It will take the minimum of each recursive call until the calls reach termination and calculate the total cost. Once all the calls reach termination and start returning, we will be presented with the absolute minimum grouping along with the grouping used.

**Runtime**: The recursive passes and O(n^2) calculation upon termination will result in an overall **O(n^3)** runtime.

## Question 7

Mostly pseudo-code experimentation, so probably 15ish hours?
