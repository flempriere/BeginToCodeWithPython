# Begin to Code with Python

This repository contains code fragments, notes and exercises from the book Begin to Code With Python by Rob Miles. The book is available at the [official Microsoft Press Store](https://www.microsoftpressstore.com/store/begin-to-code-with-python-9781509304523).

I started this repository to work through an easy and basic book before working on some more intermediate level python projects and books.

## Structure

This repository is structured as follows,

1. [`samples`](./samples/)
    - A github submodule linking to the original code provided by the book's author Rob Miles
    - We mostly use this for the `snaps.py` "library" used in several cases
2. *Part* - A Folder Collecting Chapters with similar themes
    1. *Chapter* - A Folder collecting a specific Chapter
        1. `Chapter_XX.md` - A markdown file containing notes, and descriptions of examples and exercises. Structured as follows,
            1. *Examples* - Explanations of examples and links to the code
            2. *Exercises* - Explanations of exercises and links to the code
            3. *Notes* - More detailed notes summarising the Chapter contents and contextualising examples and exercises
            4. *Summary* - End of Chapter summary of key take aways
            5. *Questions and Answers* - Frequently asked or important discussion questions posed by the book at the end of each Chapter
        2. `Examples` - A folder containing any examples from the book
        3. `Exercises` - A folder containing exercise code, often modified from the examples

## Contents

### [Programming Fundamentals](./01_ProgrammingFundamentals/)

- [Chapter 2: Python and Programming](./01_ProgrammingFundamentals/02_PythonAndProgramming/Chapter_02.md)
- [Chapter 3: Python Program Structure](./01_ProgrammingFundamentals/03_PythonProgramStructure/Chapter_03.md)
- [Chapter 4: Working with Variables](./01_ProgrammingFundamentals/04_WorkingWithVariables/Chapter_04.md)

### Useful Python

>[!NOTE]
>Chapter 1 only provides basic information on installing *python* and assumes a Windows environment. So we have ignored it.

## Python Version

The original book was written with *python 2.X* and *python 3.6* in mind. Currently we've written for *python 3.12* but may change this if compatibility issues arise.
