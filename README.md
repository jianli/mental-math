`mental-math` does deliberately inefficient arithmetic using naive mental heuristics.

In other words, it aims to do arithmetic operations about as well, and using roughly the same methods, as an average human.

So far, only multiplication has been implemented.

## Examples

Some things are easy to do in your head

* Multiplying numbers from the multiplication table
```python
>>> N(-6) * N(7)
-42
```

* Multiplying by 0 or 1
```python
>>> N(0) * N(88888)
0
>>> N(1) * N(88888)
88888
```

* Multiplying powers of 10
```python
>>> N(600) * N(1000)
600000
>>> N(20) * N(5)
100
```

Other things not so much

* Multiplying really long numbers
```python
>>> N(3) * N(111111111)
Traceback (most recent call last):
  ...
ValueError: Those numbers are too long for me to remember!
```

* Most anything else
```python
>>> N(33) * N(55)
Traceback (most recent call last):
  ...
ValueError: Could not calculate 33 * 55 in my head.
```
