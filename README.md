# Begin to Code with Python

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/flempriere/BeginToCodeWithPython/main.svg)](https://results.pre-commit.ci/latest/github/flempriere/BeginToCodeWithPython/main)
[![pages-build-deployment](https://github.com/flempriere/BeginToCodeWithPython/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://github.com/flempriere/BeginToCodeWithPython/actions/workflows/pages/pages-build-deployment)

This repository contains code fragments, notes and exercises from the book Begin to Code With Python by Rob Miles. The book is available at the [official Microsoft Press Store](https://www.microsoftpressstore.com/store/begin-to-code-with-python-9781509304523).

I started this repository to work through an easy and basic book before working on some more intermediate level python projects and books.

## Contents

### Part 1. Programming Fundamentals

- [Chapter 2: Python and Programming](./01_ProgrammingFundamentals/02_PythonAndProgramming/Chapter_02.md)
- [Chapter 3: Python Program Structure](./01_ProgrammingFundamentals/03_PythonProgramStructure/Chapter_03.md)
- [Chapter 4: Working with Variables](./01_ProgrammingFundamentals/04_WorkingWithVariables/Chapter_04.md)
- [Chapter 5: Making Decisions](./01_ProgrammingFundamentals/05_MakingDecisions/Chapter_05.md)
- [Chapter 6: Repeating Actions with Loops](./01_ProgrammingFundamentals/06_RepeatingActionsWithLoops/Chapter_06.md)
- [Chapter 7: Using Functions to Simplify Programs](./01_ProgrammingFundamentals/07_UsingFunctions/Chapter_07.md)
- [Chapter 8: Storing Collections of Data](./01_ProgrammingFundamentals/08_StoringCollectionsOfData/Chapter_08.md)

### Part 2. Advanced Programming

- [Chapter 9: Using Classes to Store Data](./02_AdvancedProgramming/09_UsingClasses/Chapter_09.md)
  - [Extension Exercises for Chapter 9](./02_AdvancedProgramming/09_UsingClasses/Chapter_09_ExtensionExercises.md)
- [Chapter 10: Use Classes to Create Active Objects](./02_AdvancedProgramming/10_UseClassesToCreateActiveObjects/Chapter_10.md)
- [Chapter 11: Object-Based Solution Design](./02_AdvancedProgramming/11_ObjectBasedSolutionDesign/Chapter_11.md)
- [Chapter 12: Python Applications](./02_AdvancedProgramming/12_PythonApplications/Chapter_12.qmd)

### Useful Python

>[!NOTE]
> Chapter 1 only provides basic information on installing *python* and assumes a Windows environment so is not covered in these notes
>

## Python Version and Writing Style

- The original book was written with *python 2.X* and *python 3.6* in mind.
- Currently we've written the code using *python 3.12.*
- Small changes have been made to the supplied code to resolve the following issues:
  1. `snaps` `get_string` function not allowing the user to actually supply input
  2. `snaps` `display_image` modified to deal with issues where `.png` files might not display
- In general the code style of the solutions is restricted to elements of the python language introduced up until that point
  - For some of the extension exercises we have gone beyond that by still restricting ourselves to concepts that have been
  introduced, e.g
    1. We use `random.choice` and `random.choices` to select random items from a list, **after** having been exposed to both the `random` and `list`
    libraries
    2. We use the string method `find` after having been introduced to the concept of string methods and substrings searching with
    `startswith`
    3. We use the `datetime` module to simplify arithmetic on date and time objects after having extensively used the `time` module
