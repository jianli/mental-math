mental-math implements deliberately inefficient arithmetic using naive mental heuristics.

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
>>> N(6000) * N(1000000)
6000000000
>>> N(20) * N(5)
100
>>> N(3) * N(222)
666
```

Some things are hard

```python
>>> N(33) * N(55)
Traceback (most recent call last):
  ...
ValueError: Could not calculate 33 * 55 in my head.
```
