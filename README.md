mental-math does deliberately inefficient arithmetic using naive mental heuristics.

In other words, it aims to do arithmetic operations about as well, and using roughly the same methods, as an average human.

So far, only multiplication has been implemented.

## Examples

Some things are easy to do in your head

```python
>>> N(-1) * N(-3)
3
>>> N(0) * N(88888)
0
>>> N(1) * N(88888)
88888
>>> N(6) * N(7)
42
>>> N(600) * N(1000)
600000
>>> N(20) * N(5)
100
>>> N(3) * N(222)
666
```

Some things are hard

```python
>>> multiply(3, 111111111)
Traceback (most recent call last):
  ...
ValueError: Those numbers are too long for me to remember!
>>> N(33) * N(55)
Traceback (most recent call last):
  ...
ValueError: Could not calculate 33 * 55 in my head.
```
