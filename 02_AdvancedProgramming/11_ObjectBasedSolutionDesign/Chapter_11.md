# Chapter 11: Object-based Solution Design

- [Notes](#notes)
  - [Fashion Shop Application](#fashion-shop-application)
    - [Application Data Design](#application-data-design)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

- The [previous
  chapter](../10_UseClassesToCreateActiveObjects/Chapter_10.qmd) looked
  at creating useful objects
- In this chapter we’ll explore how to create systems comprising large
  numbers of different but related objects
- We’ll also look at connecting objects via their methods

### Fashion Shop Application

- Consider the following scenario

> A friend who runs a fashion shop would like you to build an
> application to help manage her stock. She sells a large range of
> clothing items and wants to be able to track inventory. Her workflow
> is as follows, stock arrvies from suppliers, the details are entered
> in the system. When an item is sold it should be removed from the
> stock. She would also like to be produce reports indicating how many
> of each item are in stock.

- Working with the client you define the following information about how
  her stock operates

- Each item has a unique reference

- Each reference contains:

  - A description
  - A price
  - A number in stock
  - A list of delivery amounts and dates, and sales

- For now the client is happy to just print out the entire stock list

- Has indicated in future they may wish to have more analytics, e.g.

  - determine which item has the lowest stock

- Our prototype interface is then,

  ``` text
    Mary's Fashion Shop

    1. Create a new stock item
    2. Add stock to an existing item
    3. Sell stock
    4. Stock report
    5. Exit

    Enter your command:
  ```

- The above options are all pretty straightforward for now

#### Application Data Design

## Summary

## Questions and Answers
