# Chapter 12: Python Applications

- [Notes](#notes)
  - [Advanced Functions](#advanced-functions)
    - [References to Functions](#references-to-functions)
      - [Use Function References in the BTCInput
        Module](#use-function-references-in-the-btcinput-module)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### Advanced Functions

- Python functions are powerful and can be used in some interesting ways

#### References to Functions

- We’ve seen that we can use references to functions much like variables

- e.g. `map` in [Chapter
  10](../10_UseClassesToCreateActiveObjects/Chapter_10.qmd#the-python-map-function)
  took a reference to a function and applied it element-wise to a list

  - Another example was
    [`filter`](../11_ObjectBasedSolutionDesign/Chapter_11.qmd#filter-on-tags)

- Let’s explore this in more detail, consider the following code snippet
  (see
  [SimpleFunctionReferences.py](./Examples/01_SimpleFunctionReferences/SimpleFunctionReferences.py))

  ``` python
    # Example 12.1 Simple Function References

    def func_1():
        print("Hello from function 1")

    def func_2():
        print("Hello from function 2")

    x = func_1
    x()
    x = func_2
    x()
  ```

      Hello from function 1
      Hello from function 2

- We have two functions `func_1` and `func_2`

- We can assign the variable `x` to refer to and call each of these in
  turn

  - The dereference operator `()` called on `x` resolves to the function
    it references

- The variable is effectively another name for the function

- We still have to call it properly, e.g. (see
  [InvalidFunctionReferences.py](./Examples/02_InvalidFunctionReferences/InvalidFunctionReferences.py))

  ``` python
    # Example 12.2 Invalid Function References

    def func_1():
        print("Hello from func_1")

    x = func_1
    x(99)
  ```

      TypeError: func_1() takes 0 positional arguments but 1 was given
      ---------------------------------------------------------------------------
      TypeError                                 Traceback (most recent call last)
      Cell In[2], line 7
            4     print("Hello from func_1")
            6 x = func_1
      ----> 7 x(99)

      TypeError: func_1() takes 0 positional arguments but 1 was given

- The above generates an error as expected, because `x` is given an
  argument `99`

- `func_1` takes no arguments

- The error resolves to the original function name (here `func_1`)

##### Use Function References in the BTCInput Module

## Summary

## Questions and Answers
