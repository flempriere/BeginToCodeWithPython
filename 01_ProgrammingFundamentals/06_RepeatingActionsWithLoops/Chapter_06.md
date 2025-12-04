# Chapter 6: Repeating Actions with Loops

- [Notes](#notes)
  - [The `while` construction](#the-while-construction)
    - [Example: Investigating the `while`
      construction](#example-investigating-the-while-construction)
    - [Exercise: Create a Looping Selection
      Program](#exercise-create-a-looping-selection-program)
    - [Exercise: Create a Looping Countdown
      Program](#exercise-create-a-looping-countdown-program)
    - [Handling Invalid User Entry](#handling-invalid-user-entry)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### The `while` construction

- `while` allows a program to repeat blocks of statements
- structure is similar to an `if`

``` mermaid
block-beta
    columns 4
    space
    title["Breakdown of a While"]:2
    space

    block:Input
    columns 1
        while["while"]
        whileDescr["(start of the while construction)"]
    end

    block:MiddleOne
    columns 1
        condition["condition"]
        conditionDescr["(value that is True or False)"]
    end

    block:MiddleTwo
    columns 1
        colon[":"]
        colonDescr["Colon"]
    end

    block:Suite
    columns 1
        suite["Statement block"]
        suiteDescr["(statements)"]
    end

classDef BG stroke:transparent, fill:transparent
class title BG
class condition BG
class conditionDescr BG
class colon BG
class colonDescr BG
class while BG
class whileDescr BG
class suite BG
class suiteDescr BG
```

- if the condition evaluates `True` then the block of statements is run
  - After the statements are run, control returns to the start of the
    `while` loop
  - If the condition is *still* `True` then the loop runs again

#### Example: Investigating the `while` construction

*Use the python interpreter to run the following to understand the*
`while` *loop*

1. *Can we use a boolean value to control a* `while` *construction?*

    - *Yes, for example the block of statements in the* `while` *here
      shouldn’t run*

    ``` python
     while False:
         print("Loop")
     print("Outside the Loop")
    ```

        Outside the Loop

2. *Can a loop go on forever?*

    - *Yes, an control expression for a* `while` *that always evaluates*
      `True` *will cause the loop to run infinitely*

    ``` python
     while True:
         print("Loop")
     print("Outside the Loop")
    ```

    - *The above should only print* `"Loop"` *when executed*
    - *If you accidently do this you may need to use `CTRL+C`, `CRTL+Z`
      or an interrupt execution feature of your live environment to stop
      the execution*

3. *Will the following program ever print out the message,*
    `"Outside loop"`*?*

    ``` python
     while True:
         print("Inside Loop")
     print("Outside Loop")
    ```

    - *No, the above is a quintessential infinite loop*

4. *Will the following program ever print out the message,*
    `"Inside Loop"`*? How about* `"Outside loop"`*?*

    ``` python
     while False:
         print("Inside Loop")
     print("Outside Loop")
    ```

        Outside Loop

    - *The* `while` *never executes the statements inside so*
      `"Inside Loop"` *is never printed, but* `"Outside Loop"` *is.*

5. *What will the following program print?*

    ``` python
     flag = True
     while flag:
         print("Inside Loop")
         flag = False
     print("Outside Loop")
    ```

        Inside Loop
        Outside Loop

    - *When we first enter the loop* `flag` *is* `True` *so the loop
      executes and* `"Inside Loop"` *is printed*, `flag` *is then set*
      `False` *so on the next iteration of the loop, the loop doesn’t
      execute. We move to the next statement outside of the loop and
      print out* `"Outside Loop"`
    - *The pattern of using a control variable that is updated in the
      loop body in a* `while` *loop is very common*

6. *What will the following program print?*

    ``` python
     flag = True
     while flag:
         print("Inside Loop")
         Flag = False
     print("Outside Loop")
    ```

    - *This looks similar to the previous, but note the typo, we refer
      to* `Flag` **not** `flag` *inside the loop, which defines a*
      **new** *variable, instead of modifying the loop control. We thus
      get an infinite series of* `"Inside Loop"` *being printed.*

7. *What will the following program print?*

    ``` python
     count = 0
     while count < 5:
         print("Inside Loop")
         count = count + 1
     print("Outside Loop")
    ```

        Inside Loop
        Inside Loop
        Inside Loop
        Inside Loop
        Inside Loop
        Outside Loop

    - `count` *is initially set to* $0$*, at each iteration we print*
      `"Inside Loop"` *and increase the value of* `count` *by* $1$*. The
      loop stops once* `count` *reaches* $5$ *This means that*
      `"Inside Loop"` *should be printed* $5$ *times, followed by*
      `"Outside Loop"`

#### Exercise: Create a Looping Selection Program

*Use a* `while` *loop, to make a theme park selector that runs
continously. All you need to do is put all of the statements that
implement the theme park behaviour into a* `while True` *construction*

For usability our program won’t loop endlessly. We’ll say that any
number that it is not a valid ride number is code for quitting the
program. The relevant changes to the [Ride
Selector](../05_MakingDecisions/Chapter_05.qmd#selec)

#### Exercise: Create a Looping Countdown Program

*One of the examples [in the above question
set](#example-investigating-the-while-construction) involved a
count***up** *to* $5$*. Implement a program that counts down from* $10$
*to* $0$ *over* $10$ *seconds*

#### Handling Invalid User Entry

## Summary

## Questions and Answers
