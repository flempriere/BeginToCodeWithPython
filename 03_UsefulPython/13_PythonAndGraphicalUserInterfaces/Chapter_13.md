# Chapter 13: Python and Graphical User Interfaces

- [Notes](#notes)
  - [Create a Graphical User Interface with
    Tkinter](#create-a-graphical-user-interface-with-tkinter)
    - [Make Something Happen: Build our First User
      Interface](#make-something-happen-build-our-first-user-interface)
    - [Code Analysis: Building a Graphical User
      Interface](#code-analysis-building-a-graphical-user-interface)
  - [Create a Graphical Application](#create-a-graphical-application)
    - [Lay out a Grid](#lay-out-a-grid)
      - [Use Sticky Formatting](#use-sticky-formatting)
      - [Use Padding](#use-padding)
      - [Span Grid Cells](#span-grid-cells)
    - [Create an Event Handler
      Function](#create-an-event-handler-function)
    - [Code Analysis: Writing an Event
      Handler](#code-analysis-writing-an-event-handler)
    - [Create a Main Loop](#create-a-main-loop)
  - [Handle Errors in a Graphical User
    Interface](#handle-errors-in-a-graphical-user-interface)
  - [Make Something Happen: Fahrenheit to Centigrade and
    Back](#make-something-happen-fahrenheit-to-centigrade-and-back)
  - [Draw on a Canvas](#draw-on-a-canvas)
    - [Make Something Happen: Investigate Events and
      Drawing](#make-something-happen-investigate-events-and-drawing)
  - [Tkinter Events](#tkinter-events)
  - [Create a Drawing Program](#create-a-drawing-program)
    - [Code Analysis: Drawing on a
      Canvas](#code-analysis-drawing-on-a-canvas)
    - [Make Something Happen: Make the Drawing Program Draw
      Ovals](#make-something-happen-make-the-drawing-program-draw-ovals)
  - [Enter Multiline Text](#enter-multiline-text)
    - [Make Something Happen: Investigate the Text
      Object](#make-something-happen-investigate-the-text-object)
  - [Group Display Elements in
    Frames](#group-display-elements-in-frames)
  - [Create an Editable `StockItem` Using a
    GUI](#create-an-editable-stockitem-using-a-gui)
    - [Code Analysis: Creating a
      `StockItemEditor`](#code-analysis-creating-a-stockitemeditor)
    - [Code Analysis: The `load_into_editor`
      Method](#code-analysis-the-load_into_editor-method)
    - [Code Analysis: The `get_from_editor`
      Method](#code-analysis-the-get_from_editor-method)
    - [Code Analysis: Editing Stock
      Items](#code-analysis-editing-stock-items)
  - [Create a Listbox Selector](#create-a-listbox-selector)
    - [Make Something Happen: Investigating the `Listbox`
      Object](#make-something-happen-investigating-the-listbox-object)
    - [Create a `StockItem` Selector](#create-a-stockitem-selector)
      - [Code Analysis: Selecting Stock
        Items](#code-analysis-selecting-stock-items)
  - [An Application with a Graphical User
    Interface](#an-application-with-a-graphical-user-interface)
    - [Setting up the File Structure and the Basic Graphical User
      Interface](#setting-up-the-file-structure-and-the-basic-graphical-user-interface)
    - [Adding Selection and Editing](#adding-selection-and-editing)
      - [Adding Editing](#adding-editing)
      - [Setup Selector](#setup-selector)
      - [Setting up a Stock Level Adjuster
        Component](#setting-up-a-stock-level-adjuster-component)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### Create a Graphical User Interface with Tkinter

- Our previous programs have been text-based interfaces
- Python lets us create *Graphical* user interfaces
- Graphical UI’s typically consist of buttons, text fields etc.
  - This is called the *front-end*
  - Connects to behaviours in the underlying program (the *back-end*)
- Graphical User Interfaces are typically implemented by representing
  graphical elements as objects
  - Interactions translate to method calls
    - e.g. changing a label text
- Tkinter is a built-in module in python for designing a user interface
  - Represents UI elements through a class hierarchy
  - Tkinter itself wraps a library called Tk
  - Tk is a user interface toolkit

#### Make Something Happen: Build our First User Interface

*Familiarise yourself with the basics of TKinter and graphical
interfaces by working through the following steps in the python
interpreter*

1. *Enter the following command*

    ``` python
     from tkinter import *
    ```

    - As discussed before this imports everything from the `TKinter`
      module into the main namespace
      - No need to preface the Tkinter components with the `Tkinter`
        namespace
    - Again, you should be careful about using this
      - Increases the chance of naming collisions between different
        parts of the program

2. *Create a* **root** *window by running the following statement*

    ``` python
     root = Tk()
    ```

    - Root window acts as a container for display elements
    - Should create a new window when executed
      - Look’s something like below
      - Tk uses the native OS windowing system
      - So may look different if your OS is different

![Tk Root Window](./Examples/01_IntroToTkinter/root.png)

1. *Create a* `Label` *by executing the following statement*

    ``` python
     hello = Label(root, text="hello")
    ```

    - User’s can’t interact with a `Label`

    - But does display text on a window

    - A program can change the text on a label

      - e.g. in response to user input

    - `Label` has two parameters

      1. parent

          - the object *within* which the label is displayed
          - Here we use the root
          - We can use multiple levels of nesting to create complex
            objects

      2. text

          - the actual text to display on the label

    - Should observe that after executing the above we don’t see the
      label text

    - We have created the label

    - We also need to specify how to display it

    - Two mechanisms

      1. `pack`

          - packs elements together
          - can supply hints e.g. `LEFT` or `TOP` to control where the
            pack occurs

      2. `grid`

          - lay elements out on a grid
          - Does mean you need to plan the UI layout
          - `grid` method on graphical elements lets us specify how to
            place the object on a grid

2. *Display the* `Label` `hello` *on the window by using the* `grid`
    *method as shown below*

    ``` python
     hello.grid(row=0, column=0)
    ```

    - Tells the program to display the `hello` label at the grid
      coordinate `(0, 0)` (top left corner)
    - Should now see the label displayed
    - The window should shrink to the size of the label

    ![Tk Window with Label](./Examples/01_IntroToTkinter/label.png)

3. *Add another label* `Goodbye` *by executing the following*

    ``` python
     goodbye = Label(root, text="goodbye")
     goodbye.grid(row=1, column=0)
    ```

    - Display now has two labels
    - Labels are left aligned
    - The hello label is slightly offset more than the goodbye label
      - We can use settings to fix this

    ![Tk Window with Two
    Labels](./Examples/01_IntroToTkinter/two_labels.png)

    - The next step is to allow the user to initiate actions in a
      program
    - E.g. using a button
    - When pressed a button can link to some behaviour to be executed
    - How do we link this behaviour?
      - We create a function encapsulating the behaviour
      - The button is passed the function as a function reference
      - When the button is pressed it calls the function

4. *Define a function for your button. Execute the following commands*

    ``` python
     def been_clicked():
         print("click")
    ```

    - Simple function
    - When called it just prints `click`

5. *Create a button, and connect the* `been_clicked` *function to it.
    Run the following statements*

    ``` python
     btn = Button(root, text="Click me", command=been_clicked)
    ```

    - This creates a `Button` called `btn`
    - We specify it to be attached to the `root` window
    - We set the button text to `"Click me"`
    - We then link the `been_clicked` function via the `command`
      argument
    - Now we add the button to the display

    ``` python
     btn.grid(row=2, column=0)
    ```

    ![Tk Window with a Button](./Examples/01_IntroToTkinter/button.png)

    - Click the button a few times and you should see output like,

          >>> click
          click
          click

    - Each click results in a call to `been_clicked`

    - We often refer to the functions connected to GUI elements as
      *event handlers*

      - They *handle* the *external events* of the user

6. *How do we modify a widget, such as changing the text? Work through
    the following*

    - Display elements provide a `config` method

    - Can be used to change or configure their attributes

    - We can rename the `hello` label as follows,

      ``` python
        hello.config(text="New Hello")
      ```

      ![Updated hello label](./Examples/01_IntroToTkinter/new_label.png)

    - What if we want to read input from the user?

      - We can use an `Entry` widget
      - The `Entry` widget reads a line of text from the user

7. *Create an* `Entry` *widget by executing the following statements*

    ``` python
     ent = Entry(root)
     ent.grid(row=3, column=0)
    ```

    - The `Entry` widget `ent` is created at the bottom of the program

    - The initial text line is empty

      ![Tk Window with Entry
      widget](./Examples/01_IntroToTkinter/entry.png)

    - However, we can type something in, say the classic `Hello, World!`

      ![Entry with text
      entered](./Examples/01_IntroToTkinter/entry_with_text.png)

    - The next question is how do we read the text into our program?

      - The `Entry` object supports a `get` method

      - `get` returns the text of the element

      - Running this on our `Entry` object we should see,

        ``` python
          print(ent.get())
        ```

            hello world

      - Try playing with this yourself

We’ve combined all these steps into one
[program](./Examples/01_IntroToTkinter/basic_ui.py)

#### Code Analysis: Building a Graphical User Interface

*Consider the following questions about graphical user interfaces*

1. *What happens if we change the size of the window on the desktop?*

    - By default, we can resize a window

    - But the widgets themselves in the window do not resize

    - We can prevent the widget from being resized

      ``` python
        root.resizable(width=False, height=False)
      ```

    - `resizable` method controls if a window can be resized

    - You can also have a window be resizable and have the components
      size and position change automatically

2. *What happens if we close the window we created?*

    - We created our window in the interpreter
      - Window disappears when closed on the desktop
    - For a program
      - Can define ways to get control when the user tries to close the
        program

3. *Will the window look the same on different systems?*

    - No
    - The general UI will look the same
    - However, modern tk uses the windowing system of the host machine
    - These can vary for different systems

4. *What happens if an event handler function connected to a button
    takes a long time to complete?*

    - Function connect to the button runs
    - Button is “stuck down” until the function finishes executing
    - All other controls also not available
    - Generally event handlers should be responsive
      - Python supports *threading* or multiple threads of execution
        which can execute simultaneously
      - Each thread can run a different program
      - An event handler could spawn a separate thread to start a new
        program
    - Threads will not be discussed more broadly in these notes

5. *What happens if I put two items in the same cell in a grid?*

    - The most recent one will be drawn over the older one
    - The new one blocks the old one
    - This is generally a bad idea

6. *Can we update the contents of elements on the screen from within an
    event handler?*

    - Yes
    - This is how applications work

- They key takeaway here is that user interactions are *events*
- These *events* end up as calls to functions inside a program
- This notion of wiring widgets to actions is similar to the idea of
  wiring up an electronic device
- We design the UI then connect the UI components to event handlers

### Create a Graphical Application

- We’ll now demonstrate our first meaningful graphical program

- Let’s create a simple adding program

  - User provides two numbers
  - Program outputs the result

- The full code is given by
  [adder.py](./Examples/02_AddingMachine/adder.py)

  ![Adding Program](./Examples/02_AddingMachine/Images/adder.png)

- User enters two numbers

- Presses the result button

- Result is then displayed below

- We’ll start creating an application

  - We’ll start with an `Adder` class to hold the application

  ``` python
    class Adder:
        """GUI-based adding machine

        Call `display` to initiate the display

        Notes
        -----
        Uses `Tkinter` as the GUI framework
        """

        def display(self):
            """
            Display the user interface

            Returns
            -------
            None
            """
  ```

- `display` provides the method for handling providing the UI

  - We’ll fill this in later

- We’ll add some script code to get this to run as a main program

  ``` python
    if __name__ == "__main__":
        app = Adder()
        app.display()
  ```

- This allows the code to loaded as a module (e.g. for `pydoc`)

- Also executable as a main program

- Now need to implement the adding machine

#### Lay out a Grid

- Let’s plan out the UI as a grid
- The below figure overlays the final grid
  - We can see some of the components seem to span multiple columns
  - We’ll look at how to implement this latter

  ![Adding Program Grid](./Examples/02_AddingMachine/Images/grid.png)
- Let’s look at what widgets we need
  - 3 Labels (first number, second number, result)
  - 2 Entries (first number, second number)
  - 1 Button (Calculate result)
- Let’s build the first *component*
  - Labelling the numbers

  ``` python
    first_number_label = tkinter.Label(root, text="First Number")
    first_number_label.grid(sticky=tkinter.E, padx=5, pady=5, row=0, column=0)

    second_number_label = tkinter.Label(root, text="First Number")
    second_number_label.grid(sticky=tkinter.E, padx=5, pady=5, row=1, column=0)
  ```

- These create and position the number labels
- They are positioned at the top of the widget (row zero and row one
  respectively)
- You can see we have `sticky`, `padx` and `pady` as extra positioning
  parameters to the `grid` call

##### Use Sticky Formatting

- When using grid we often want to combine widgets of different sizes in
  the same columns
- Layout sizes a column to the largest element
- By default items are centre-aligned
- *sticky* lets you define a direction the widget should try to *stick*
  or prioritise
  - Given by compass directions
  - `tkinter.E` stickies the label to the east or close to the adjacent
    `tkinter.Entry` widget
  - To *stretch* a widget you can sticky an item in multiple directions
    - This is because sticky directions can be added together

##### Use Padding

- Padding adds extra space around a component
- Useful to prevent a component being drawn right up against a boundary
- Padding can be defined for both the $x$ and $y$ directions

##### Span Grid Cells

- We need a two column grid to but the number entry labels and entry
  boxes next to each other

- We’d like the calculate result button and the displayed result to take
  up the whole row

- We can merge columns by using the `columnspan` argument

  ``` python
    add_button = tkinter.Button(root, text="Add numbers", command=do_add)
    add_button.grid(sticky=tkinter.E + tkinter.W, row=2, column=0, columnspan=2, padx=5, pady=5)
  ```

- `do_add` is a function we’ll define later to read the two numbers and
  perform the addition

- `columnspan=2` tells the program to draw `add_button` as spanning two
  columns

- By making the button sticky in east and west it will be drawn across
  the entire row

- Last steps are to add the `Entry` widgets and the result `Label`

  ``` python
    first_number_entry = tkinter.Entry(root, width=10)
    first_number_entry.grid(sticky=tkinter.E, padx=5, pady=5, row=0, column=0)

    second_number_entry = tkinter.Entry(root, width=10)
    second_number_entry.grid(sticky=tkinter.E, padx=5, pady=5, row=1, column=0)

    result_label = tkinter.Entry(root, text="Result")
    result_label.grid(sticky=tkinter.E + tkinter.W, padx=5, pady=5, row=3, column=0, columnspan=2)
  ```

#### Create an Event Handler Function

- Now need to define our function connected to the result button
  `do_add`

- We can define this local to `display` since no other part of the
  program needs it

- Event handler needs to read the text from the two number entry widgets

- Then needs to convert these to numbers

- Then add them

- Then update the results label with the result

- The implementation is given below,

  ``` python
    class Adder:
        ...
        def display(self):
            # create the screen elements
            def do_add():
                # get first number
                first_number_text = first_number_entry.get()
                first_number = float(first_number_text)

                # get second number
                second_number_text = second_number_entry.get()
                second_number = float(second_number_text)

                # add them and update the display
                result = first_number + second_number
                result_label.config(text = str(result))
  ```

#### Code Analysis: Writing an Event Handler

*Answer the following questions about an event handler*

1. *Why is the event handler defined inside the display function?*

    - The event handler function (`do_add`) needs access to display
      elements defined in `display`
    - Functions defined inside a function have access to the variables
      of the enclosing scope
    - Could define `do_add` as part of the `Adder` class
      - But would then have to maintain references to all the display
        elements outside of the display function

2. *What happens if the user doesn’t type in a valid number before
    pressing the Add numbers button?*

    - `float` fails to convert the result
    - This raises an exception
    - The user won’t see the exception directly
      - We may see it in logging or debug output
    - The display won’t update properly though because the `do_add`
      method will abort
    - In the future well look at ways to provide the user with warning
      or error popups

#### Create a Main Loop

- In the first shell example, we could see everything just worked
- This was because the shell read input, processed it then waited for
  more input
- If we run our program as written, we’ll see a similar thing where the
  script just ends
  - We can’t just use `sleep` as before because this will freeze the
    program
  - The user should still be able to interact
- To keep the display active we need to set up a *main loop*
  - Code for making the program wait and then respond to user input

    ``` python
      root.mainloop()
    ```

- `mainloop` fetches events and sends it onto functions created to deal
  with events
- When the close button is pressed the `mainloop` ends
- `mainloop` is typically the last statement
  - The program usually ends then too

### Handle Errors in a Graphical User Interface

- Our program works, but it’s simple

- Doesn’t handle invalid input

- If we enter strings the program will appear not work

  - This is because `float` throws an exception trying to convert
    strings

- We could add exception handling as we’ve done before

  ``` python
    def do_add():
        first_number_text = first_number_entry.get()
        try:
            first_number = float(first_number_text)
        except ValueError:
            result_label.config(text="Invalid first number")

        second_number_text = second_number_entry.get()
        try:
            second_number = float(second_number_text)
        except ValueError:
            result_label.config(text="Invalid second number")
  ```

- We could do a something identical for the second number

- This has one problem

  - If both the first and second number are invalid, only the first is
    flagged

- We want to build a more complex error string that reports all the
  errors

  ``` python
    def do_add():
        error_message = ""
        first_number_text = first_number_entry.get()
        try:
            first_number = float(first_number_text)
        except ValueError:
            error_message = "Invalid first number\n"

        second_number_text = second_number_entry.get()
        try:
            second_number = float(second_number_text)
        except ValueError:
            error_message += "Invalid second number"

        if error_message != "":
            result_label.config(text=error_message)
        else:
            result = first_number + second_number
            result_label.config(text = str(result))
  ```

- We can use an empty error string to detect if we’ve encountered an
  error

- This lets different error sections contribute to the overall output

- We can further extend this by providing a visual indicator of where
  the error has occurred

  - For example, by setting the background red, and the text blue

    ``` python
      first_number_entry.config(background="red", foreground="blue")
    ```

  - In this case we also have to remember to reset the background, when
    the user corrects the input

- The final implementation can be found in
  [AddingMachineWithExceptions](./Examples/03_AddingMachineWithExceptions/adder.py)

  ![Adding Machine with
  Exceptions](./Examples/03_AddingMachineWithExceptions/excepted_adder.png)

  ### Display a Message Box

- An alternative technique could be to use a message or dialog box

- Forces the user to acknowledge the error

- We can use Tkinter’s `messagebox`

  ``` python
    from tkinter import messagebox
  ```

- `messagebox` has three levels for displaying messages (functions)

  - `showinfo`
  - `showwarning`
  - `showerror`

- Only difference is the icon

- UI is locked until the user clears the message

- All have the same function signature, see below

  ``` python
    messagebox.showinfo("Rob Miles", "Rob Miles is awesome")
  ```

  ![An example message box with an information
  notice](./Examples/04_AddingMachineWithMessageBox/info_message_box.png)

- We can add this to our Adder program

  - Instead of setting the result with the error text, we display a
    message box
  - To help the user we’ll also keep the background highlighting

  ![The Adder program with invalid input highlighting and an error
  message
  box](./Examples/04_AddingMachineWithMessageBox/adder_message_box.png)

### Make Something Happen: Fahrenheit to Centigrade and Back

*In this challenge you will be provided with a half-finished program.
Your goal is to complete the program. The program should allow the user
to convert back and forth between fahrenheit and centigrade. The final
program should look like the below,*

![Final Fahrenheit to Celsius
Implementation](./Exercises/01_FahrenheitToCelcius/final_implementation.png)

*Currently it looks like*

![Initial Fahrenheit to Celsius
Implementation](./Exercises/01_FahrenheitToCelcius/initial_implementation.png)

*The starter code is*

``` python
"""
Exercise 13.1 Fahrenheit to Celsius

Provides a graphical interface for converting between fahrenheit and centigrade
"""

import tkinter


class Converter:
    """
    GUI-based Fahrenheit to Celsius converter (and vice-versa)

    Call `display` to initiate the display

    Notes
    -----
    Uses `Tkinter` as the GUI framework
    """

    def display(self):
        """
        display the user interface

        Returns
        -------
        None
        """
        root = tkinter.Tk()

        cent_label = tkinter.Label(root, text="Celsius:")
        cent_label.grid(row=0, column=0, padx=5, pady=5, stick=tkinter.E)

        cent_entry = tkinter.Entry(root, width=5)
        cent_entry.grid(row=0, column=1, padx=5, pady=5)

        fah_entry = tkinter.Entry(root, width=5)
        fah_entry.grid(row=2, column=1, padx=5, pady=5)

        def fahrenheit_to_celsius():
            """
            Convert from Fahrenheit to celsius and display the result

            Returns
            -------
            None
            """
            fah_string = fah_entry.get()
            fah_float = float(fah_string)
            result = (fah_float - 32) / 1.89
            cent_entry.delete(0, tkinter.END) # remove old text
            cent_entry.insert(0, str(result))

        def celsius_to_fahrenheit():
            """
            Convert from Celsius to Fahrenheit and display the result

            Returns
            -------
            None
            """
            cent_string = cent_entry.get()
            cent_float = float(cent_string)
            result = cent_float * 1.8 + 32

        fahrenheit_to_celsius_button = tkinter.Button(root, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
        fahrenheit_to_celsius_button.grid(row=1, column=0, padx=5, pady=5)

        root.mainloop()

if __name__ == "__main___":
    app = Converter()
    app.display()
```

This program uses a new feature, we use an `Entry` element to get the
user specified fahrenheit or celsius temperature. When we click the
appropriate button we need to overwrite what was in the other `Entry`
label.

`Entry` supports sophisticated text editing, but we only want to
overwrite the text. We can’t just redefine the text like we would for a
`Label`

First we use `delete` to remove the old text.

``` python
    cent_entry.delete(0, tkinter.END) # remove the old text
```

The first argument is the index to delete from (inclusive), and the
second is the index to delete to. `tkinter.END` is used to delete up to
the end of the line

We can then add the new text using `insert`

``` python
    cent_entry.insert(0, str(result))
```

This has a slightly different syntax. We indicate the index we want to
insert the string at, and then the string we want to insert

You can find the [starter code
here](./Exercises/01_FahrenheitToCelcius/FahrenheitToCelcius_starter.py),
and should have a go at yourself before reading the solution below

Let’s first tidy up the already implemented Fahrenheit to Celsius code.
We want to add proper error handling code. We’ve already seen how to do
this with the [Message Box](#display-a-message-box).

``` python
        def fahrenheit_to_celsius():
            """
            Convert from Fahrenheit to celsius and display the result

            Returns
            -------
            None
            """
            try:
                fah_string = fah_entry.get()
                fah_entry.config(background="white", foreground="black")
                fah_float = float(fah_string)
            except ValueError:
                tkinter.messagebox.showerror(title="Temperature Converter", message="Fahrenheit must be a number")
                fah_entry.config(background="red", foreground="blue")
                return

            result = (fah_float - 32) / 1.8
            cent_entry.delete(0, tkinter.END) # remove old text
            cent_entry.insert(0, "{0:.2f}".format(result))
            cent_entry.config(background="white", foreground="black")
```

- This should look pretty familiar, we use a `try...except` block to
  catch invalid input
  - On invalid input we display an error box
  - We also set the background for the entry element to be red and the
    text to be blue
  - This means we have to reset the entry element to the normal look
    after a successful read (in case it had been set as an error)
- Once we have validated all the input we can then update the text in
  the other entry box
- Here we have to be careful that if the user was previously typing
  here, then it might to have be set to an error highlight
- So here we also want to set it back to normal
- Lastly you’ll notice we’ve updated the string we pass to `insert` to
  `"{0:.2f}".format(result)`
  - This allows means that the result will only be displayed to two
    decimal places

Next, we want to finish defining the reverse function for converting
celsius to fahrenheit. This is pretty much identical to the previous
function. Just swapping the roles of the entry boxes

``` python
        def celsius_to_fahrenheit():
            """
            Convert from celsius to Fahrenheit and display the result

            Returns
            -------
            None
            """
            try:
                cent_string = cent_entry.get()
                cent_entry.config(background="white", foreground="black")
                cent_float = float(cent_string)
            except ValueError:
                tkinter.messagebox.showerror(title="Temperature Converter", message="Celsius must be a number")
                cent_entry.config(background="red", foreground="blue")
                return
            result = cent_float * 1.8 + 32
            fah_entry.delete(0, tkinter.END)
            fah_entry.insert(0, "{0:.2f}".format(result))
            fah_entry.config(background="white", foreground="black")
```

We then need to add the button to connect to this function

``` python
    celsius_to_fahrenheit_button = tkinter.Button(root, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
    celsius_to_fahrenheit_button.grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()
```

Of course the last thing to do is add the Fahrenheit label and then
perform some tidying up. Namely we want the `Entry` boxes to stretch to
fill the whole column (so we use `tkinter.E + tkinter.W` in the `stick`
parameter)

``` python
def display(self):
    """
    display the user interface

    Returns
    -------
    None
    """
    root = tkinter.Tk()

    cent_label = tkinter.Label(root, text="Celsius:")
    cent_label.grid(row=0, column=0, padx=5, pady=5, stick=tkinter.E)

    fah_label = tkinter.Label(root, text="Fahrenheit:")
    fah_label.grid(row=2, column=0, padx=5, pady=5, stick=tkinter.E)

    cent_entry = tkinter.Entry(root, width=5)
    cent_entry.grid(row=0, column=1, padx=5, pady=5, stick=tkinter.E + tkinter.W)

    fah_entry = tkinter.Entry(root, width=5)
    fah_entry.grid(row=2, column=1, padx=5, pady=5, stick=tkinter.E + tkinter.W)
```

The final working implementation can be found in
[FahrenheitToCelsius.py](./Exercises/01_FahrenheitToCelcius/FahrenheitToCelcius.py)

### Draw on a Canvas

- GUI’s typically work by recognising *events* or interactions
- For example, we could recognise when a user has clicked on a screen to
  draw something
- Let’s create a basic drawing program

#### Make Something Happen: Investigate Events and Drawing

*Investigate events in* `Tkinter` *by working through the following
activity. Start by opening the python interpreter*

1. *Import Tkinter*

    ``` python
        import tkinter
    ```

2. *Create a window on the screen*

    ``` python
        root = tkinter.Tk()
    ```

3. *Create a* `Canvas`

    - A `Canvas` is a display component that acts as a container for
      other display elements

    - Elements can be drawn and positioned on a canvas

    - When creating the canvas we need to specify the size

    - *Enter the following to create a canvas*

      ``` python
        c = Canvas(root, width=500, height=500)
      ```

    - *place the canvas on the display, by entering the following*

      ``` python
        c.grid(row=0, column=0)
      ```

4. *Add functionality to the canvas*

    - The canvas currently just appears as a square

    - We need to attach functionality to the canvas

    - Similar to how we attach a function to a button

    - Start by defining our action function

    - *Define the function below*

      ``` python
        def mouse_move(event):
            print(event.x, event.y)
      ```

    - Above function receives a single argument (`event`)

      - `event` has two attributes, `x` and `y`
      - These are the positions of the mouse when the event is triggered

    - This function simply prints out the position of the mouse when the
      event is triggered

    - Now we need to connect the event to this function

      - This process is called *binding*

    - display objects contain a `bind` method used to bind events
      triggered on them to a function

    - *Enter the following to bind the* `<B1-motion>` *event on the
      canvas to your function*

      ``` python
        c.bind("<B1-Motion>", mouse_move)
      ```

    - `<B1-Motion>` corresponds to mouse movement with the `B1` button
      held down (left-button typically)

    - `bind` returns a unique string to identify the binding

      - This string can be used to track and recover a binding later
      - e.g. If we wanted to disable it
      - String’s are typically machine specific

5. *Try out the new functionality*

    - Click and drag your mouse on the canvas
    - You should see a stream of coordinates in the output
    - In graphics typically the top left corner is `(0, 0)`
      - Indices increase *down* the screen and to the *right*

6. *Convert the canvas to a drawing program*

    - We want our canvas to support drawing something!

    - `Canvas` provides a method `create_rectangle` to draw a rectangle
      on a screen

    - *Enter the following to draw a rectangle*

      ``` python
        c.create_rectangle(100, 100, 300, 200, outline="blue", fill="blue")
      ```

    - `create_rectangle` takes four arguments, corresponding to the
      `(x, y)` coordinates of the top left and the bottom right corner
      respectively

    - `outline` lets us optionally set the outline colour of the
      rectangle (default is black)

    - `fill` sets the fill in colour of the block (default black)

    - `create_rectangle` returns an integer

    - This is an id for the drawn rectangle

    - We can use this to manipulate the rectangle

    - *Delete the rectangle*

      ``` python
        c.delete(1)
      ```

    - The ability to manipulate the objects on a canvas is very powerful

    - *Redefine a new function for the mouse press event*

      ``` python
        def mouse_move_draw(event):
            c.create_rectangle(event.x - 5, event.y -5, event.x + 5, event.y + 5, fill="red", outline="red")
      ```

    - The above draws a $10 \times 10$ pixel rectangle centred around
      the mouse click location

    - *Bind this new function to the canvas*

      ``` python
        c.bind("<B1-Motion>", mouse_move_draw)
      ```

    - Now attempt to draw on the canvas, you should see something like
      below

      ![The basic drawing canvas](./Examples/05_Canvas/basic_canvas.png)

The final result can be found in
[Canvas.py](./Examples/05_Canvas/basic_canvas.png)

### Tkinter Events

- Events are powerful and flexible
- Consider the event tag from before `"<B1-Motion>"`
  - It consists of two parts

    1. The first part is the *modifier* (`B1`)
        - Condition required for event to generate
        - Here the condition is that the primary mouse button is clicked
    2. The second part is the *detail*
        - Thing that produces the event (here moving the mouse)

  - We could for example use the event `"<Motion>"`

    - This produces events for every mouse move
- Below is a table of common and useful events and modifiers

| Modifier | Action                     | Detail        | Action                |
|----------|----------------------------|---------------|-----------------------|
| Control  | Control key pressed        | Motion        | Mouse moved           |
| Shift    | Shifty key pressed         | ButtonPress   | Mouse button pressed  |
| B1-B4    | corresponding mouse button | ButtonRelease | Mouse button released |
|          |                            | KeyPress      | Key pressed           |
|          |                            | KeyRelease    | Key released          |
|          |                            | MouseWheel    | Mouse wheel moved     |

- Different actions may create different event information
- Events delivered when a key is pressed identify the key
- Events delivered by the mouse contain its coordinates
- Multiple modifiers can create complex events with multiple modifiers

### Create a Drawing Program

- Let’s create a more sophisticated version of our drawing program

  1. User can draw with a mouse
  2. Change the drawing colour with the keyboard
  3. clear the canvas

``` python
"""
Example 13.6 Drawing Program

A simple drawing program where the user can

1. Draw
2. Change brush colour
3. Clear the canvas
"""

import tkinter


class Drawing:
    """
    GUI element for a drawing program

    Notes
    -----
    Uses `tkinter` for the GUI framework
    """

    def display(self):
        """
        Display the Drawing Program

        Returns
        -------
        None
        """
        root = tkinter.Tk()
        canvas = tkinter.Canvas(root, width=500, height=500)
        canvas.grid(row=0, column=0)

        draw_colour = "red"

        def mouse_move(event):
            """
            Draw a 10 by 10 pixel rectangle centred on the mouse

            Parameters
            ----------
            event
                the triggering event

            Returns
            -------
            None
            """
            canvas.create_rectangle(
                event.x - 5,
                event.y - 5,
                event.x + 5,
                event.y + 5,
                fill=draw_colour,
                outline=draw_colour,
            )

        canvas.bind("<B1-Motion>", mouse_move)

        def key_press(event):
            """
            Change the drawing program state in response to a key press

            Parameters
            ----------
            event
                key press that triggered the function

            Returns
            -------
            None
            """
            nonlocal draw_colour
            ch = event.char.upper()
            if ch == "C":
                canvas.delete("all")
            elif ch == "R":
                draw_colour = "red"
            elif ch == "G":
                draw_colour = "green"
            elif ch == "B":
                draw_colour = "blue"

        canvas.bind("<KeyPress>", key_press)
        canvas.focus_set()

        root.mainloop()


if __name__ == "__main__":
    app = Drawing()
    app.display()
```

The output should look something like this,

![A more sophisticated drawing program supporting multiple
colours](./Examples/06_DrawingProgram/improved_canvas.png)

and can be found in
[DrawingProgram.py](./Examples/06_DrawingProgram/DrawingProgram.py)

#### Code Analysis: Drawing on a Canvas

*To understand the code above, work through the following questions*

1. *What is the* `draw_colour` *variable used for?*

    - `draw_colour` holds the current draw colour

    - Many colours are recognised by name

    - There are other methods for specifying colours too, such as by
      hexcode

      ``` python
        draw_colour = "#FFFF00"
      ```

      - The hexcode is three two-digit hex values
      - Correspond to the amount of red, green and blue respectively
      - The above corresponds to yellow

    - The Tcl wiki maintains a page with the [colour
      names](https://wiki.tcl-lang.org/page/Color+Names%2C+running%2C+all+screens)

    - The program starts with `draw_colour` corresponding to red, and
      uses the keys `R`, `G`, `B` to switch colours

2. *How do you clear the canvas?*

    - We can delete specific items if we keep track of the ID
    - `delete` can accept `"all"` as its argument
      - In this case all elements are deleted
      - This effectively clears the canvas
    - In our program this is assigned to the `C` key

3. *In the* `key_press` *function, you’ve created a* `nonlocal`
    *variable called* `draw_colour`*. What does this mean?*

    ``` python
        def key_press(event):
            nonlocal draw_colour
    ```

    - `key_press` needs to be able to change the value of `draw_colour`
    - `draw_colour` is declared in the outer `display` function scope
    - `draw_colour` is therefore not a global variable so we can’t use
      `global` to connect the function to the variable
    - `nonlocal` acts similar but means the variable exists in the
      enclosing scope

4. *What does the call of* `focus_set` *do?*

    - By default python doesn’t know what application a key press should
      be sent to
      - Or which component of an application
    - `focus_set` tells python that this component should receive the
      keyboard events
    - This is independent of which window is actually focused
      (i.e. currently being looked at) by the user

#### Make Something Happen: Make the Drawing Program Draw Ovals

*The* `Canvas` *object provides a method called* `create_oval`*, which
can be used to draw ovals. It has a different set of arguments from the*
`create_rectangle` *method. Make a version of the drawing program that
draws ovals. You could even allow the artist to swap between brushes by
pressing S for square brush and O for an oval brush*

Let’s first implement the oval drawing mechanics. From the `tkinter`
website, we can see that `create_oval` has a similar function signature
to create_rectangle, but there is different semantic meaning. The oval
is drawn inscribed in a rectangle defined by the upper left corner (the
first two arguments) and the lower right corner (bottom two arguments).

So we can define a function to draw an oval in response to an event as
follows,

``` python
    def mouse_move_oval(event):
        """
        Draw an oval inscribed in an 10 x 10 pixel rectangle centred on
        the mouse

        Parameters
        ----------
        event
            the triggering event
        """
        canvas.create_oval(
            event.x - size,
            event.y - size,
            event.x + size,
            event.y + size,
            fill=draw_colour,
            outline=draw_colour,
        )
```

Now we need to add the functionality to switch between the two brushes.
By default our program binds the `<B1-Motion>` event to drawing a
square. We need to make this binding change. We’ll add additional
keypress events to the `key_press` function `S` and `O` to switch the
brush. Each of these events will have to rebind the appropriate function
to the `<B1-Motion>` event. To help the user we’ll add a text label
below the canvas that indicates the current brush. For symmetry we’ll
add a second label below this one that indicates the current colour. So
we then need to update the `key_press` function to properly update these
labels.

The final `key_press` function then looks like,

``` python
        def key_press(event):
            """
            Change the drawing program state in response to a key press

            Parameters
            ----------
            event
                key press that triggered the function

            Returns
            -------
            None
            """
            nonlocal draw_colour
            nonlocal size
            ch = event.char.upper()
            if ch == "C":
                canvas.delete("all")
            elif ch == "R":
                draw_colour = "red"
                colour_label.config(text="Colour: {0}".format(draw_colour))
            elif ch == "G":
                draw_colour = "green"
                colour_label.config(text="Colour: {0}".format(draw_colour))
            elif ch == "B":
                draw_colour = "blue"
                colour_label.config(text="Colour: {0}".format(draw_colour))
            elif ch == "S":
                canvas.bind("<B1-Motion>", mouse_move_square)
                brush_label.config(text="Brush: square")
            elif ch == "O":
                canvas.bind("<B1-Motion>", mouse_move_oval)
                brush_label.config(text="Brush: oval")
            elif ch == "+":
                size = min(size + 5, 50)
                size_label.config(text="Size: {0}".format(size))
            elif ch == "-":
                size = max(size - 5, 5)
                size_label.config(text="Size: {0}".format(size))

            elif ch == "H":
                tkinter.messagebox.showinfo(
                    title="Simple Canvas",
                    message="""Controls:
C - clear canvas
R - change colour to red
B - change colour to blue
G - change colour to green
S - change brush to square brush
O - change brush to oval brush
+ - increase brush size
- - decrease brush size

Right click to erase""",
                )
```

You’ll notice that there are three extra bound events that have not been
discussed. The first two are the `+` and `-` keys which we bind the
increasing and decreasing the brush size respectively. Our original
drawing code always draw the box as a $10 \times 10$ box around the
triggering event. We’ll now let the user control that. We make `size` a
variable, and the user can use `+` to increase the brush size in
increments of $5$ up to $50$, and decrease the `size` using `-` down to
$5$. This `size` takes the place of the hardcoded `event.x + 5`
statements in `mouse_move_oval`.

The next addition you should notice is the `H` key. This simply uses
`messagebox` to display a dialog to the user listing out all the
controls.

The last functionalty we want to implement is erasing. We want the user
to be able to erase over previously drawn elements using the right mouse
button. This corresponds to the `<B3-Motion>` event. Now we could try
and right some code that tracks all the drawn elements and tries to
locate which element is being dragged over and delete it, but an easy
work around is to simply paint over the top with a new rectange that
uses the background colour. So in this case, from the `tkinter` docs we
can see that we can set the `Canvas` background colour to white using
`bg="white"` in the `Canvas` constructor. We can then define our `erase`
function as,

``` python
        def erase(event) -> None:
            """
            Erase the canvas

            Parameters
            ----------
            event
                triggering event

            Notes
            -----
            Erase is implemented by drawing a white rectangle centred on the mouse
            """
            canvas.create_rectangle(
                event.x - size,
                event.y - size,
                event.x + size,
                event.y + size,
                fill="white",
                outline="white",
            )
```

We then simply bind this to the the `<B3-Motion>` event and we’ve got
our erase. This fairly straightforward set of steps gives us a fairly
complete and good looking little drawing program. You can see the full
code in
[DrawingProgram.py](./Exercises/02_AdvancedDrawingProgram/DrawingProgram.py).
An example of the program looks like below,

![The improved drawing program supporting multiple colours, brush sizes,
help and the ability to
erase](./Exercises/02_AdvancedDrawingProgram/advanced_canvas.png)

### Enter Multiline Text

- `Entry` only supports a single line of text
- Powerful, but not sophisticated enough for all tasks, e.g. a text
  editor
- `Text` supports pages of text
  - Similar to `Entry`
  - Some differences

#### Make Something Happen: Investigate the Text Object

*Investigate the* `Text` *object using the python interpreter. Work
through the following steps*

1. *Import tkinter*

    ``` python
     import tkinter
    ```

2. *Create a Tkinter window*

    ``` python
     root = tkinter.Tk()
    ```

3. *Create a* `Text` *object*

    ``` python
     t = tkinter.Text(width=80, height=10)
    ```

    - Creates a `Text` object, assigned to `t`

    - `width` and `height` correspond to *characters* (width) and
      *lines* (height) **not** pixels

    - *position the object on the window*

      ``` python
        t.grid(row=0, column=0)
      ```

      ![The `Text` widget](./Examples/07_Text/text.png)

    - `Text` gives a lot of control over editing the content

    - `Text` let’s us extract it’s contents using `get` like `Entry`

      - But has a more sophisticated functions signature

    - Refer to characters by their row and column positions

4. *Demonstrate the use of* `get` *to extract text from the* `Text`
    *widget*

    ``` python
     t.get("1.0", tkinter.END)
    ```

        Hello, World!\nAnother line of text\n

    - This returns all of the text starting at row $1$, column $0$ and
      through the `tkinter.END` of the `Text`.

    - If you want to get a specific slice of text, you can instead pass
      another string of the form `"row.column"`, e.g.

    - To slice the second row, we write

      ``` python
        t.get("2.0", "3.0")
      ```

          Another line of text\n

5. *Demonstrate the use of the* `delete` *method to remove text*

    - `delete` removes text from a `Text` widget

    - Has an identical signature to get, e.g.

      ``` python
        t.delete("1.0", tkinter.END)
      ```

    - deletes all text

6. *Demonstrate the use of the* `insert` *method to add text*

    - We can add text by defining the start position

    - Then supply the string we want to insert, e.g.

      ``` python
        t.insert("1.0", "New line 1\nNew line 2")
      ```

    - This inserts text into the `Text` box at the start, `\n` results
      in splitting the lines

### Group Display Elements in Frames

- `grid` helps us define how we want to layout a complete window
- Often we want to lay out subcomponents on a bigger component first
  - That component is then embedded into the window
- `Frame` is an object for acting as a root for a set of elements
  - Can be used to define how objects are displayed within it
- The goal will be to create a graphical version of our [fashion shop
  program](../../02_AdvancedProgramming/11_ObjectBasedSolutionDesign/Chapter_11.qmd#fashion-shop-application)
- We can use a `Frame` to define a layout for editing a `StockItem`
- The `Frame` object can then be included in higher level graphical
  objects
  - `Frame` acts very similar to the `Tk` object for the main window

  - We can use it in places that need a root window rather than the `Tk`
    object as below

    ``` python
      frame = tkinter.Frame(root)
      stock_ref_label = tkinter.Label(frame, text="Stock ref:")
      stock_ref_label.grid(sticky=tkinter.E, row=0, column=0, padx=5, pady=5)
    ```

  - `stock_ref_label` is now part of the `frame` object

    - Positioned in the top left corner of the frame
    - This frame component can then be reused elsewhere

  - Note that the `stock_ref_label` and other components of the frame
    won’t show up until the frame itself is attached to some other frame
    or window

### Create an Editable `StockItem` Using a GUI

- Now let’s start creating a graphical version of our Fashion Shop
  Program

- First goal is to create an editable `StockItem`

- We need the GUI presentation of it to,

  1. Clear the editor display
  2. Put a `StockItem` on display for editing
  3. Load a `StockItem` from the display after editing

- This object will be called `StockItemEditor`

- Let’s start by stubbinng out the class

``` python
"""
Example 13.8 Stock Item Editor

Implements a graphical editor object for editing `StockItem` objects
"""


class StockItemEditor:
    """
    Graphical Editor for a StockItem

    Notes
    -----
    Implemented as a `Tkinter` Frame
    """

    def __init__(self, root):
        """
        Create a new `StockItemEditor`

        Parameters
        ----------
        root
            Tkinter root frame for the editor
        """
        pass

    def clear_editor(self):
        """
        Clears the editor window

        Returns
        -------
        None
        """
        pass

    def load_into_editor(self, item):
        """
        Load a `StockItem` into the edit display



        Parameters
        ----------
        item : StockItem
            stock reference to be loaded
        """
        pass

    def get_from_editor(self, item):
        """
        Get an updated `StockItem` from the editor

        Parameters
        ----------
        item : StockItem
            stock reference to update

        Raises
        ------
        ValueError
            raised if the price entry cannot be converted to a number
        """
        pass
```

- Implement the methods one by one

- Start with `__init__`

- Needs to

  - Create display objects
  - Add them to the frame

- Editor exists at the start of the program

  - Item’s are loaded into the editor

- An alteranative design might be to load an editor when we bring up an
  item

  ``` python
    def __init__(self, root):
        """
        Create a new `StockItemEditor`

        Parameters
        ----------
        root
            Tkinter root frame for the editor
        """
        self.frame = tkinter.Frame(root)

        stock_ref_label = tkinter.Label(self.frame, text="Stock ref:")
        stock_ref_label.grid(sticky=tkinter.E, row=0, column=0, padx=5, pady=5)
        self._stock_ref_entry = tkinter.Entry(self.frame, width=30)
        self._stock_ref_entry.grid(sticky=tkinter.W, row=0, column=1, padx=5, pady=5)

        price_label = tkinter.Label(self.frame, text="Price:")
        price_label.grid(sticky=tkinter.E, row=1, column=0, padx=5, pady=5)
        self._price_entry = tkinter.Entry(self.frame, width=30)
        self._price_entry.grid(sticky=tkinter.W, row=1, column=1, padx=5, pady=5)

        self._stock_level_label = tkinter.Label(self.frame, text="Stock level: 0")
        self._stock_level_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        tags_label = tkinter.Label(self.frame, text="Tags:")
        tags_label.grid(sticky=tkinter.E + tkinter.N, row=3, column=0, padx=5, pady=5)
        self._tags_text = tkinter.Text(self.frame, width=50, height=5)
        self._tags_text.grid(row=3, column=1, padx=5, pady=5)
  ```

- The `__init__` creates a bunch of elements, namely,

  1. A label, entry pair for the stock item reference number,
  2. A label, entry pair for the stock item price
  3. A label for the current stock level
  4. A label, text pair for the stock item tags

- We can then create and run our program with this element,

  ``` python
    root = tkinter.Tk()
    stock_frame = StockItemEditor(root)
    stock_frame.frame.grid(row=0, column=0)

    root.mainloop()
  ```

#### Code Analysis: Creating a `StockItemEditor`

*Answer the following questions about how* `StockItemEditor` `__init__`
*method*

1. *Why do only some of the display elements have a* `self` *element in
    front of them*

    - We only need to keep a reference to display elements we later want
      to interact with
      - e.g. the various entry boxes and the stock level label
      - The former we’ll want to extract and/or update the text from and
        the later we want to update the text
      - Other display elements like static labels we don’t need to
        change, so no need to keep the reference

2. *What is the frame attribute of the* `StockItemEditor` *class used
    for?*

    - The frame contains the objects that make up the editing display

    - Program creating the display needs to use the frame to position
      the entire component in the larger display

    - `frame` is simply an attribute to hold the `Frame` object
      reference

    - e.g. when we actually position the frame,

      ``` python
        stock_frame.frame.grid(row=0, column=0)
      ```

- Next, the `clear_editor` method

  - Two use cases,
  - Loading a new element (clear any previous element first)
  - When finished editing an element

  ``` python
      def clear_editor(self):
        """
        Clears the editor window

        Returns
        -------
        None
        """
        self._stock_ref_entry.delete(0, tkinter.END)
        self._price_entry.delete(0, tkinter.END)
        self._tags_text.delete("0.0", tkinter.END)
        self._stock_level_label.config(text="Stock level: 0")
  ```

  - Straightforward, justt clear all the text and set the stock level
    label to zero

- Next we implement `load_into_editor` which loads a `StockItem`

- Need to copy the values from the supplied `StockItem` into the editor

  ``` python
    def load_into_editor(self, item):
        """
        Load a `StockItem` into the edit display

        Parameters
        ----------
        item : StockItem
            stock reference to be loaded
        """
        self.clear_editor()
        self._stock_ref_entry.insert(0, item.stock_ref)
        self._price_entry.insert(0, str(item.price))
        self._stock_level_label.config(text="Stock level {0}".format(item.stock_level))
        self._tags_text.insert("0.0", item.text_tags)
  ```

  - We call the method and pass the `StockItem`

  - The editor then reads the values from the item

  - Inserts these into the appropriate text boxes

  - We can then use it as below,

    ``` python
    item = StockItem.StockItem(
        "D001",
        price=120,
        tags="dress,colour:red,loc:shop window,pattern:swirly,size:12,evening,long",
    )

    item.add_stock(5)
    stock_frame.load_into_editor(item)
    ```

#### Code Analysis: The `load_into_editor` Method

*Work through the following questions about the* `load_into_editor`
*method*

1. *What is the purpose of this method?*

    - Used after the user has selected a `StockItem` to edit
    - Needs to load and display the values of the item for the user to
      then modify
      - Compared to our text-based interface which prompted the user to
        edit each attribute in turn for `Contact` objects

2. *Why are some of the items converted to a string before editing?*

    - Attributes internally are not strictly held as strings
    - E.g. the `price` is a number and tags are a `set`
    - `Entry` and `Text` expect strings though, so we have to convert
      back and forth

3. *What is the* `text_tags` *attribute of the a* `StockItem`

    - Good spot!

    - This is a small addition make to the `StockItem` to simply
      conversion of a tags set to a string and back

    - Allows the user to easily supply or receive a set of tags as a
      string of comma-seperated values

      ``` python
        @property
        def text_tags(self):
            """
            text_tags : str
                item tags as a comma separated string
            """
            tag_list = list(self.tags)
            tag_list.sort()
            return ",".join(tag_list)

        @text_tags.setter
        def text_tags(self, tag_string):
            self.tags = set(map(str.strip, str.split(str.lower(tag_string), sep=",")))
      ```

    - We’ve modified the `StockItem` implementation to simply support
      this

    - An alternative would be to provide a wrapper or adaptor

- Last method, is the reverse of the previous. To fetch a `StockItem`
  from the editor

  ``` python
    def get_from_editor(self, item):
        """
        Get an updated `StockItem` from the editor

        Parameters
        ----------
        item : StockItem
            stock reference to update

        Raises
        ------
        ValueError
            raised if the price entry cannot be converted to a number
        """
        item.set_price(self._price_entry.get())
        item.stock_ref = self._stock_ref_entry.get()
        item.text_tags = self._tags_text.get("1.0", tkinter.END)
  ```

  - We now want to link this to a button that the user will press

  ``` python
    def save_edit():
        stock_frame.get_from_editor(item)
        stock_frame.clear_editor()


    save_button = tkinter.Button(root, text="Save", command=save_edit)
    save_button.grid(row=1, column=0)
  ```

  - We can see this updates the item, then clears the editor

  - You might notice a new function on the `StockItem`, `set_price`

  - This simply validates that a given price is a number and then
    updates the price

    ``` python
      def set_price(self, new_price):
          """
          Set a new price on the stock item

          Parameters
          ----------
          new_price : int | float
              new price of the item

          Raises
          ------
          ValueError
              Raised if the price is outside of the valid range
          ValueError
              Raised if the price is not a number

          """
          if StockItem.show_instrumentation:
              print("** StockItem set_price called")
          try:
              new_price = int(new_price)
          except ValueError:
              new_price = float(new_price)
          if new_price < StockItem.min_price or new_price > StockItem.max_price:
              raise ValueError("Price out of range")
          self.__price = new_price
    ```

#### Code Analysis: The `get_from_editor` Method

*Answer the following questions about* `get_from_editor`

1. *What is the purpose of this method?*

    - Takes the edited `StockItem` values and puts them back into a
      `StockItem`
    - Equivalent of saving text in a text editor, your changes are
      written back to the original file

2. *Can this method fail?*

    - Yes
    - Invalid prices will cause the `set_price` method to raise a
      `ValueError`
      - This occurs if the value is not a number or if it’s outside the
        valid range
    - The caller is responsible for handling the exception

- We can write a simple script to check that the `StockItemEditor`
  widget works as expected

``` python
if __name__ == "__main__":
    item = StockItem.StockItem(
        "D001",
        price=120,
        tags="dress,colour:red,loc:shop window,pattern:swirly,size:12,evening,long",
    )

    item.add_stock(5)

    root = tkinter.Tk()
    stock_frame = StockItemEditor(root)
    stock_frame.frame.grid(row=0, column=0)
    stock_frame.load_into_editor(item)

    def save_edit():
        stock_frame.get_from_editor(item)
        stock_frame.clear_editor()

    save_button = tkinter.Button(root, text="Save", command=save_edit)
    save_button.grid(row=1, column=0)

    root.mainloop()
```

- For simplicity this has been written in the same file as the
  [StockItemEditor](./Examples/08_EditableStockItem/StockItemEditor.py)

- The final widget should look something like below

  ![The final `StockItemEditor`
  widget](./Examples/08_EditableStockItem/stockItemEditorFrame.png)

- You can also see the updated
  [`StockItem`](./Examples/08_EditableStockItem/StockItem.py)

#### Code Analysis: Editing Stock Items

*Would it not make sense to put the editing behaviour inside the*
`StockItem` *class?*

You can probably make an argument one way or another. The argument in
favour might be that all the functionality of a `StockItem` should be in
the `StockItem` and that by keeping the editing behaviour on the object
we can reduce coupling to another edit object that might need to read
the internals of the `StockItem` class.

The argument against might be that the `StockItem` is supposed to
represent a specific `StockItem` and its associated data. It would be an
additional responsibility for it to also be responsible for editing
itself, as that is effectively taking responsibility for creating
`StockItem` objects.

For this program we decide to go with the second approach, `StockItem`
simply acts as a datastore, and `StockItemEditor` implements the logic
for editing a `StockItem`

### Create a Listbox Selector

- We can now load and edit our stock items
- The thing we need is a way for the user to select a stock item
- We can’t just put a simple button in because the number of stock items
  is dynamic
- One approach would be to use an `Entry` widget to have the user type
  in the reference they want to edit
  - This has the difficulty that the user has to know the stock
    reference beforehand
- A more useful approach might to be have all the stock references
  displayed in a list that we can select from
  - `Listbox` is a widget that lets us do this

#### Make Something Happen: Investigating the `Listbox` Object

*Start by investigating the* `Listbox` *through the python interpreter.
Work through the following steps*

1. *Load tkinter and create a window*

    ``` python
     import tkinter
     root = tkinter.Tk()
    ```

2. *Create a* `Listbox` *and display it*

    ``` python
     lb = tkinter.Listbox(root)
     lb.grid(row=0, column=0)
    ```

    - This creates a `Listbox` assigns it to the variable `lb`
    - Then adds `lb` to the window
    - Screen should now have an empty white list box

3. *Add some items to the box*

    - We can add items using the `insert` method

      ``` python
        lb.insert(0, "hello")
      ```

    - First argument is the index to insert the item

    - Second argument is the text to insert

    - Add some more items,

      ``` python
        lb.insert(1, "goodbye")
        lb.insert(0, "top line")
        lb.insert(tkinter.END, "bottom line")
      ```

    - The final listbox should look like below,

    - We can see that `insert` doesn’t overwrite elements, if we insert
      before another element, everything is shifted down

    - We can use `tkinter.END` to append something to the end

      ![The `Listbox` after adding some items to
      it](./Examples/09_Listbox/listbox.png)

    - In our program, we’ll populate the `Listbox` with the stock
      references of our stock items

4. *Define a binding to select items from the* `Listbox`

    - Now we need to be able to select items in the box

    - This is an event to bind against

    - Start by defining the function to bind

      ``` python
        def on_select(event):
            """
            Get's the text associated with a selected Listbox item
            """
            lb = event.widget
            index = int(lb.curselection()[0])
            print(lb.get(index))
      ```

    - Runs when the user clicks on a `Listbox`

    - We first retrieve the widget that triggered the event with
      `event.widget()`

      - In this case it is the listbox

    - We then get the currently selected index in the list box

      - `curselection` returns a tuple of selected elements
      - Since we might have multiple selected
      - We’re not using this, so we only want the first one

    - Then pass this index to the `get` method of the list box

      - The list box `get` returns the text associated with a supplied
        index

    - Now we need to bind this to the listbox

    - The event we want is `"<<ListboxSelect>>"`

    - Enter the following

      ``` python
        lb.bind("<<ListboxSelect>>", on_select)
      ```

- A script version is available in
  [Listbox.py](./Examples/09_Listbox/Listbox.py)

#### Create a `StockItem` Selector

- Now let’s create a `StockItem` Selector component using a `Listbox`

- Our `StockItemSelector` needs to,

  1. Accept `StockItem` objects to define the selection list
  2. Tell the user when an item has been selected from the list

- First step is straightforward

- Second is more complicated

  - How do we make an object tell us something?
  - i.e. the reverse of binding where we do something when something
    else tells us something
  - This is called *message passing*, one part of a program sends a
    message to another
  - Here `StockItemSelector` wants to send a message to tell listeners
    that a `StockItem` has been selected

- Implementing message passing can be done using references

  - Sender takes in a reference to the receiver object
  - Message transmission is then implemented as calling a method on the
    receiver object
  - The receiver object is defined in the initialiser

``` python
class StockItemSelector:
    """
    Widget providing a list selection for StockItem objects
    """

    def __init__(self, root, receiver):
        """
        Create a new `StockItemSelector`

        Parameters
        ----------
        root
            The parent frame or window to attach this component to
        receiver
            Object to send a message to when the selection changes
        """
        self.receiver = receiver
        self.frame = tkinter.Frame()
        self.listbox = tkinter.Listbox(self.frame)
        self.listbox.grid(row=0, column=0)

        def on_select(event):
            """
            Find the selected text in the Listbox and send it to the
            receiving object

            Bound to the `ListboxSelect` event

            Parameters
            ----------
            event
                event that triggered the function

            Returns
            -------
            None
            """
            lb = event.widget
            index = int(lb.curselection()[0])
            receiver.got_selection(lb.get(index))

        self.listbox.bind("<<ListboxSelect>>", on_select)
```

##### Code Analysis: Selecting Stock Items

*Work through the following questions about the code*

1. *What is the following method doing?*

    - Creates an instance of the `StockItemSelector`
    - Designed to display a `Listbox` of `StockItem` objects
    - We want to inform a user-specified receiver object when the
      selection changes
    - `__init__` takes the root window, and the object that should be
      informed (the receiver)
    - `__init__` stores the receiver, creates the `Listbox` and properly
      configures an event handler

2. *What happens if the receiver doesn’t have a* `got_selection`
    *method?*

    - `StockItemSelector` calls the `got_selection` method on the
      receiving object when the selection changes

    - If there is no such method an exception will be thrown

    - We can test if the function exists using,

      ``` python
        assert hasattr(receiver, "got_selection")
      ```

    - `hasattr` accepts two arguments

      1. The object to check
      2. A string identifying the attribute

    - `hasattr` returns `True` if the attribute exists on the object,
      else `False`

    - We can use this to raise an exception in the `__init__` if the
      supplied object doesn’t have the appropriate method

    - This is the appropriate place to put this check (rather than
      making it implicit at the point we call the function)

- The second method to implement is the one that actually populates the
  `Listbox`

  - Should accept a list of `StockItem` objects and add their references
    to the display

  ``` python
      def populate_listbox(self, items):
        """
        Populate the Listbox with a list of StockItem's

        Parameters
        ----------
        items : list[StockItem]
            a list of stock items to add to the selection

        Returns
        -------
        None
        """
        self.listbox.delete(0, tkinter.END)
        for item in items:
            self.listbox.insert(tkinter.END, item.stock_ref)
  ```

- This method is pretty straightforward

- First clear any existing elements in the `Listbox`

- Then iterate over the list inserting the stock references for each
  item

- Finally we’ll add a simple demo script in
  [StockItemSelector.py](./Examples/10_StockItemSelector/StockItemSelector.py)

  ``` python

  if __name__ == "__main__":

    class MessageReceiver:
        def got_selection(self, stock_ref):
            print("stock item selected:", stock_ref)

    stock_list = []

    for i in range(1, 100):
        stock_ref = "D{0}".format(i)
        item = StockItem.StockItem(
            stock_ref,
            120 + (i * 10),
            "dress, colour:red, loc:shop window,pattern:swirly, size:12, evening, long",
        )
        stock_list.append(item)

    receiver = MessageReceiver()
    root = tkinter.Tk()
    stock_selector = StockItemSelector(root, receiver)
    stock_selector.populate_listbox(stock_list)
    stock_selector.frame.grid(row=0, column=0)
    root.mainloop()
  ```

- Which after running should look like,

  ![Demonstration of the
  `StockItemSelector`](./Examples/10_StockItemSelector/demoSelector.png)

### An Application with a Graphical User Interface

- Our goal now is to put all of the pieces of the previous section
  together to create a full graphical version of the fashion shop
  program

- The user should be able to,

  1. Select Stock Items
  2. Add or sell stock of a selected item
  3. Edit an item
  4. Create a new item
  5. Search for an item by tags

- The final version of the program should look something like this,

  ![The final implementation of a Graphical Fashion Shop
  Program](./Examples/11_FashionShopGUI/Docs/final_fashion_shop.png)

#### Setting up the File Structure and the Basic Graphical User Interface

- Let’s start by getting our basic set-up working and then add more
  functionality on top
- We want to make our program follow the interface of the shell-based
  fashion shop program, so that we can seamlessly switch between them
- We’ll start with the final implementation found in [Chapter
  12](../../02_AdvancedProgramming/12_PythonApplications/Chapter_12.qmd#exercise-complete-the-testing-of-stockitem)
  - We’ll start by modifying the folder structure, now rather than just
    having a `UI` package, we’ll split that into a `GUI` and a `ShellUI`
    subpackage
    - We move the shell implementation into the `ShellUI` subpackage and
      update / add `__init__.py` files as required
    - We create a new `GUI` subpackage which we’ll use to create our gui
      package
  - Let’s start by copying in the `StockItemEditor` and
    `StockItemSelector` components from the previous section
  - We can remove the demo code from these
- Now let’s create a `FashionShopGraphicalApplication` this will act
  like the old `FashionShopApplication` but support a GUI
- The start of the class, is below
  - We provide a simple static method for converting between a tag set
    and the text based tag implementation
  - Then define a basic `__init__`
  - To avoid cluttering the `__init__` we define a method
    `self._setup_UI` that contains the user interface setup code
- The rest of the class should look familiar
  - We attempt to load the database from a file
  - This time if we fail, we present the user with a *Warning* message
    box
- We also then set the currently selected item, and the current search
  tags to be empty

``` python
class FashionShopGraphicalApplication:
    """
    Provides a graphical interface for Fashion Shop inventory management
    """

    @staticmethod
    def tag_set_from_text(tag_text):
        """
        Create a set of tags from a comma-separated list

        Tags are normalised as lowercase with leading and
        trailing whitespace stripped

        Parameters
        ----------
        tag_text: str
            comma-separated list of tags

        Returns
        -------
        set
            set containing unique tags. Tags are lowercase with
            no leading or trailing whitespace
        """
        if tag_text == "":
            return set()
        tags = set(map(str.strip, str.split(str.lower(tag_text), sep=",")))
        return tags

    def __init__(self, filename, storage_class):
        """
        Creates a new `FashionShopApplication`

        Attempts to load a `FashionShop` from the provided file. Otherwise
        an empty instance is created

        Parameters
        ----------
        filename : str
            path to a file containing pickled `FashionShop` data
        storage_class : Data Manager
            class that supports the Fashion Shop Data Management API

        See Also
        --------
        FashionShop : Main class for handling inventory management
        """

        # load the storage class
        FashionShopGraphicalApplication.__filename = filename
        try:
            self.__shop = storage_class.load(filename)
        except:  # noqa: E722
            tkinter.messagebox.showwarning(
                title="Mary's Fashion Shop",
                message="Failed to load Fashion Shop\nCreating an empty Fashion Shop",
            )
            self.__shop = storage_class()

        # configure the starting state
        self._current_item = None
        self._search_tags = ""

        # configure the user interface
        self._setup_UI()
```

#### Adding Selection and Editing

- Now we can start setting up our `_setup_UI` method

- It looks like below,

  ``` python
    def _setup_UI(self):
        """
        Setup's and initialises the GUI elements

        Returns
        -------
        None
        """
        self._program_title = "Mary's Fashion Shop"
        self._root = tkinter.Tk()

        title_label = tkinter.Label(self._root, text=self._program_title)
        title_label.grid(
            sticky=tkinter.E + tkinter.W, row=0, column=0, columnspan=2, padx=5, pady=5
        )

        self._setup_editor()
        self._setup_selector()

        self._adjuster = StockItemStockAdjuster.StockItemStockAdjuster(self._root, self)
        self._adjuster.frame.grid(sticky=tkinter.E, row=4, column=1, padx=5, pady=5)
        self._adjuster.current_item = self._current_item
  ```

- We store the program title as a constant, which is then used for a top
  level label

- This `program_title` variable is used whenever we want to title a
  message box

- We then define two functions

  1. `self._setup_editor`
  2. `self._setup.selector`

- These functions set up the UI elements responsible for editing stock
  items and selecting them

- Again just designed to keep the functions small and sell contained so
  they are easy to understand

- The last bit about the `_adjuster` is used to set up the part of the
  UI that handles adjusting stock item inventory levels and we’ll look
  at it later

  - At it’s most basic it creates a `StockItemAdjuster` component
  - Then adds this to the main window in the bottom right corner

##### Adding Editing

- Editing functionality is handled by the `self._setup_editor` method

  ``` python
    def _setup_editor(self):
        """
        Setup and configure the editor component

        Returns
        -------
        None
        """

        # set up the editor
        self._editor = StockItemEditor.StockItemEditor(self._root)
        self._editor.frame.grid(sticky=tkinter.W, row=2, column=1, padx=5, pady=5)

        # set up the editor buttons

        edit_buttons_frame = tkinter.Frame(self._root)
        edit_buttons_frame.grid(sticky=tkinter.E, row=3, column=1, padx=5, pady=5)

        def create_new_stock_item():
            """
            Configure the UI to create a new `StockItem`

            Returns
            -------
            None
            """
            self._current_item = None
            self._adjuster.current_item = self._current_item
            self._editor.clear_editor()

        def save_item():
            """
            Save the details of the item currently under edit

            If there is an actively selected item, then the save overwrites it,
            otherwise a new `StockItem` is created

            Returns
            -------
            None
            """
            try:
                item = StockItem.StockItem("", StockItem.StockItem.min_price, "")
                self._editor.get_from_editor(item)
            except ValueError:
                tkinter.messagebox.showerror(title=self._program_title, message="Failed to create a new item\nPrice invalid")
                return
            if self._current_item is not None and self._current_item.stock_ref == item.stock_ref:
                # edited an item but kept the reference identical
                self.__shop.remove_old_stock_item(self._current_item.stock_ref)
                self.__shop.store_new_stock_item(item)
            else:
                # edited an item to different reference or new - need to check doesn't clash
                try:
                    self.__shop.store_new_stock_item(item)
                    if self._current_item is not None:
                        self.__shop.remove_old_stock_item(self._current_item.stock_ref)
                except KeyError as e:
                    tkinter.messagebox.showerror(title=self._program_title, message=str(e))

            self._filter_stock_items()
            create_new_stock_item()

        create_new_button = tkinter.Button(
            edit_buttons_frame,
            text="Create new item",
            command=create_new_stock_item,
        )
        create_new_button.grid(sticky=tkinter.W, row=0, column=0, padx=5, pady=5)

        save_button = tkinter.Button(edit_buttons_frame, text="Save", command=save_item)
        save_button.grid(sticky=tkinter.E, row=0, column=1, padx=5, pady=5)
  ```

  - We start by creating a new `StockItemEditor` component and placing
    it on the grid

  - You’ve seen this before

  - We premptively put it on row two, because the tags search bar will
    take up row one

  - We then create a frame to hold the edit buttons

  - We have two edit buttons,

    1. Create new item
        - Clears any currently selected item
        - Clears the editor
        - Used to be able to input a new item
    2. Save
        - Save the current state of the editor into an item
        - If there is a currently selected item, it is overwritten
        - Otherwise, a new item is created

  - We can now define the methods for our buttons

  - Since they only be used by the buttons defined here, we will define
    the functions local to the `_setup_editor` function

    - Makes the code cleaner since it avoids polluting the scope of the
      outer `FashionShopGraphicalApplication` class

  - The first function `create_new_stock_item` simply deselects the
    current item and clears the editor

  - The second, `save_item` is more sophisticated

    - There are two cases to consider, when we are adding a new item,
      and when we are editing an old item

    - Let’s refamiliarise ourselves with the code,

      ``` python
        def save_item():
            """
            Save the details of the item currently under edit

            If there is an actively selected item, then the save overwrites it,
            otherwise a new `StockItem` is created

            Returns
            -------
            None
            """
            try:
                item = StockItem.StockItem("", StockItem.StockItem.min_price, "")
                self._editor.get_from_editor(item)
            except ValueError:
                tkinter.messagebox.showerror(title=self._program_title, message="Failed to create a new item\nPrice invalid")
                return
            if self._current_item is not None and self._current_item.stock_ref == item.stock_ref:
                # edited an item but kept the reference identical
                self.__shop.remove_old_stock_item(self._current_item.stock_ref)
                self.__shop.store_new_stock_item(item)
            else:
                # edited an item to different reference or new - need to check doesn't clash
                try:
                    self.__shop.store_new_stock_item(item)
                    if self._current_item is not None:
                        self.__shop.remove_old_stock_item(self._current_item.stock_ref)
                except KeyError as e:
                    tkinter.messagebox.showerror(title=self._program_title, message=str(e))
                    return

            self._filter_stock_items()
            create_new_stock_item()
      ```

    - First we create a new dummy `StockItem` and then attempt to
      populate it with the values from the editor

    - If the editor has invalid data then we will report the error via
      message box and stop

    - Next we have to be careful,

    - The storage class stores items in a key-value store where the key
      is the stock reference

    - For a new item, we have to check that the the key isn’t already in
      use

      - We do this via the catching the `KeyError` from the
        `store_new_stock` method
      - In this case we just don’t add the new item

    - For an edited item, it’s a bit more complicated

      - If we haven’t changed the stock reference we could just get the
        old item and manually copy across the values
      - This is brittle though, and defeats the whole point of copying
        the data from the editor (i.e. the editor is responsible for
        making sure an item has the correct values)
      - We *could* call the `editor.get_from_editor` method again,
        passing in our old item object
        - But we’ve already got the information and done all the
          validation, we don’t want to repeat it
      - The other method would be to delete the old `StockItem` and then
        put the new one in
      - There’s a catch though - If we delete the old item, *then* find
        that the new stock reference is in use, we can’t rollback the
        change
      - We also can’t just add the new item, because if the stock
        reference hasn’t changed we’ll get an error because the key is
        in use by the old version of the item
      - So we have two cases,
        1. If the stock reference is unchanged
            - Delete the old stock item
            - Then add the new one
            - This is guaranteed to succeed because the key must exist
              (it was in use by the same object), and it can’t be in use
              once we delete it
        2. If the stock reference has changed
            - First check that we can add the new item (i.e. attempt to
              add it)
            - Then if that succeeds, delete the old one

    - Finally we have to be careful about what state we’re in

      - It’s possible that the user might now have a current item stored
        which doesn’t actually exist
      - So we reset the state
        - i.e. clear the editor
        - set the current item to `None`
        - handled by calling `create_new_stock_item`
        - We also want to update the displayed items, which is handled
          by `filter_stock_items`
          - We’ll look at this function in the next section

    - There is one downside to this approach

      - Since python dictionaries maintain their insertion order, every
        time an item is edited, it will move to the end of the list

  - Of course we have to add the a method to `FashionShop` to actually
    let us remove items,

    ``` python
      def remove_old_stock_item(self, stock_ref):
          """
          Remove an old item in the reference system

          The provided `item` can be indexed by it's `stock_ref` parameter

          Parameters
          ----------
          item : StockItem
              item to remove from the inventory system

          Returns
          -------
          None

          Raises
          ------
          KeyError
              Raised if the item's `stock_ref` is not registered as a key
          """
          self.__stock_dictionary.pop(stock_ref)
    ```

  - This is a simple wrapper around the dictionary method `pop`

##### Setup Selector

- Selection is handled similarly but is relatively straightforward in
  comparison

``` python
    def _setup_selector(self):
        """
        Configure and set-up the selector components, including
        searching on tags

        Returns
        -------
        None
        """
        self._selector = StockItemSelector.StockItemSelector(self._root, self)
        self._selector.frame.grid(
            sticky=tkinter.N + tkinter.S,
            row=2,
            column=0,
            rowspan=3,
            padx=5,
            pady=5,
        )

        def update_search_tags():
            """
            Updates the search tags and the corresponding list box display

            Returns
            -------
            None
            """
            self._search_tags = self._search_tags_entry.get()
            self._filter_stock_items()

        search_tags_button = tkinter.Button(
            self._root, text="Search tags:", command=update_search_tags
        )
        self._search_tags_entry = tkinter.Entry(self._root, width=40)

        search_tags_button.grid(sticky=tkinter.E, row=1, column=0, padx=5, pady=5)
        self._search_tags_entry.grid(
            sticky=tkinter.E + tkinter.W, row=1, column=1, padx=5, pady=5
        )

        update_search_tags()
```

- This is much more straightforward

- We create a new `StockItemSelector` component

- Add it the main window

- We then define a Button `search_tags_button` and an Entry element
  `search_tags_entry`

  - When `search_tags_button` is pressed it reads the tags from
    `search_tags_entry` and sets them as the search tags
    (`self._search_tags`)

- We then want to update the displayed items to match the tags

- This is handled by the method `self._filter_stock_items`

  - It is used both by the selection widget when the tags are updated
  - and by the editor when we edit items
  - Hence we store it at the object level since it needs to be used by
    multiple components

  ``` python
    def _filter_stock_items(self):
        """
        Populates the list box with item's matching the current search tags

        Returns
        -------
        None
        """
        self._selector.populate_listbox(
            self.__shop.find_matching_with_tags(
                FashionShopGraphicalApplication.tag_set_from_text(self._search_tags)
            )
        )
  ```

- Simply converts the current search tags (as a comma-seperated string)
  to a set of tags

- Then passes this to the `self.__shop` `find_matching_with_tags` method
  to get the subset of matching items

- Then updates the selector

- We *could* in theory cache the conversion to a set when the tags are
  updated, however we make the assumption that the need to filter will
  be infrequent

  - If this assumption is wrong, this is a potential source of
    performance gains

- The method in the `setup_selector` function, `update_search_tags`,
  simply updates the value of `self._search_tags` then calls
  `self._filter_stock_items`

  ``` python
    def update_search_tags():
        """
        Updates the search tags and the corresponding list box display

        Returns
        -------
        None
        """
        self._search_tags = self._search_tags_entry.get()
        self._filter_stock_items()
  ```

- We also have to implement the `got_selection` method that will be
  called by `StockItemSelector` when the selection is changed, it’s
  given below

  ``` python
    def got_selection(self, selection):
        """
        Method to be called when the program detects that the Stock Item selection has changed

        Parameters
        ----------
        selection : str
            The new selection
        """
        self._current_item = self.__shop.find_stock_item(selection)
        self._adjuster.current_item = self._current_item
        self._editor.load_into_editor(self._current_item)
  ```

- This sets the current item to what ever the new selection is and loads
  it into the editor

- It also passes this through to the `StockItemAdjuster` component we’ll
  look at next

##### Setting up a Stock Level Adjuster Component

- In the final product you can see that we have a pair of Button-Entry
  widgets for adding and removing stock

- Really these should be treated all together

- So we band them together as one component

- This will work similar to the selection component

  - It takes in the currently selected item and uses that to validate
    any proposed change in the stock level
  - When the stock level is changed, a receiver object is informed of
    the change so it can properly respond

- The implementation is below

  ``` python
    class StockItemStockAdjuster:
        """
        Graphical Component for adjusting a Stock Item

        Parameters
        ----------

        receiver
            Object to send a message to when the stock changes. Must
            support a method `stock_level_updated()`
        frame: tkinter.Frame
            the tkinter `Frame` this component is contained within

        Notes
        -----
        Implemented as a `tkinter` frame
        """

        def __init__(self, root, receiver):
            """
            Create a new `StockItemAdjuster`

            Parameters
            ----------
            root
                The parent frame or window to attach this component to
            receiver
                Object to send a message to when the stock changes. Must
                support a method `stock_level_updated()`

            Raises
            ------
            AttributeError
                raised if `receiver` does not support `stock_level_updated()`
            """
            if not hasattr(receiver, "stock_level_updated"):
                raise AttributeError(
                    "Supplied receiver does not support stock_level_updated"
                )
            self.receiver = receiver
            self._current_item = None
            self.frame = tkinter.Frame(root)

            self._add_stock_entry = tkinter.Entry(self.frame, width=10)
            self._remove_stock_entry = tkinter.Entry(self.frame, width=10)

            def add_stock():
                """
                binding function for adding stock when the button is pressed

                Returns
                -------
                None
                """
                # Entry box must not be empty
                try:
                    if self._current_item is None:
                        raise ValueError("No stock item currently selected")
                    self._current_item.add_stock(int(self._add_stock_entry.get()))
                    self.receiver.stock_level_updated()
                    self._add_stock_entry.delete(0, tkinter.END)
                except ValueError as e:
                    tkinter.messagebox.showerror(
                        title="Failed to Add Stock", message=str(e)
                    )

            def remove_stock():
                """
                binding function for removing stock when the button is pressed

                Returns
                -------
                None

                Raises
                ------
                ValueError
                    raised if no stock item is selected
                ValueError
                    raised if the value provided stock amount is not a positive
                    whole number, or larger than the maximum allowed to sell
                """
                # Entry box must not be empty
                try:
                    if self._current_item is None:
                        raise ValueError(
                            "Failed to remove stock:\nno stock item currently selected"
                        )
                    self._current_item.sell_stock(int(self._remove_stock_entry.get()))
                    self.receiver.stock_level_updated()
                    self._remove_stock_entry.delete(0, tkinter.END)
                except ValueError as e:
                    tkinter.messagebox.showerror(
                        title="Failed to Remove Stock", message=str(e)
                    )

            add_stock_button = tkinter.Button(
                self.frame, text="Add stock:", command=add_stock
            )
            remove_stock_button = tkinter.Button(
                self.frame, text="Remove stock:", command=remove_stock
            )

            add_stock_button.grid(row=0, column=0, sticky=tkinter.E, padx=5, pady=5)
            self._add_stock_entry.grid(row=0, column=1, sticky=tkinter.E, padx=5, pady=5)
            remove_stock_button.grid(row=1, column=0, sticky=tkinter.E, padx=5, pady=5)
            self._remove_stock_entry.grid(row=1, column=1, sticky=tkinter.E, padx=5, pady=5)

        @property
        def current_item(self):
            """
            current_item : StockItem | None
                The currently active `StockItem`

            Raises
            ------
            TypeError
                raised if `item` is not a `StockItem`
            """
            return self._current_item

        @current_item.setter
        def current_item(self, item):
            if not isinstance(item, StockItem.StockItem) and item is not None:
                raise TypeError("item must be of type StockItem or None")
            self._current_item = item
  ```

- The `__init__` should look very familiar to the `StockItemSelector`

  - Instead of a `got_selection` function, we have a
    `stock_level_changed` function to receive the change
    - This time, because the widget can adjust the stock level via the
      item directly
  - `__init__` will use `hasattr` to check that the passed `receiver`
    has the required `stock_level_changed` attribute

- We then create our buttons and entry widgets for adding and removing
  stock

- The `add_stock` and `delete_stock` widgets are bound to the respective
  buttons

- On being clicked they check that the state is valid, i.e.

  1. There is a currently selected item
  2. There is a value in the respective `Entry` label
  3. It is a positive number that is either less than the current stock
      level (selling stock) or less than the maximum we can add (adding
      stock)

- We then update the stock level as appropriate

- Clear the respective `Entry` label so the user doesn’t accidently
  press the button multiple times

- Call the `stock_level_changed` method on the receiver object

- Lastly changing the `current_item` is implemented via a property

  - Let’s us enforce that the current item is always a `StockItem`
    instance or `None`

- How do we implement this component in the application?

  - Well you already saw in `self._setup_UI` that we added this
    component to the bottom right corner

  - We’ve seen whenever we change the current item, we have to propagate
    that through to the adjuster component

  - Now need to implement the `stock_level_updated` method

  - All this needs to do is reload the current item to update the
    displayed stock level

    ``` python
      def stock_level_updated(self):
      """
      Method to be called when the program detects the the Stock Item's stock level has changed

      Returns
      -------
      None
      """
      self._editor.load_into_editor(self._current_item)  # reload the current item
    ```

    #### Running the Program

- The last step is to implement code to actually run the application

  - Previously we’ve called this `display`, but because we want to be
    consistent with the Shell-based UI, we instead use `main_menu`
  - This is just a wrapper around `root.mainloop` and then a call to
    save the state of the database when the program is closed

  ``` python
    def main_menu(self):
        """
        Run the program

        Notes
        -----
        The function is called `main_menu` to maintain legacy compatibility
        with the `ShellUI` interface for an application
        """
        self._root.mainloop()

        self.__shop.save(FashionShopGraphicalApplication.__filename)
  ```

- We then define our main program, `FashionShopGraphicalUI.py`

  ``` python
    if __name__ == "__main__":
        from Data import FashionShop
        from UI.GUI import FashionShopGraphicalApplication

        # load the UI implementation
        ui = FashionShopGraphicalApplication.FashionShopGraphicalApplication

        # load the data management implementation
        shop = FashionShop.FashionShop

        app = ui(filename="fashionshop.pickle", storage_class=shop)
        app.main_menu()
  ```

- This looks pretty much identical to the previous shell program

- Indeed the only changes are that we change the import to
  `from UI.GUI import FashionShopGraphicalApplication` and the setup of
  the `ui` as
  `ui = FashionShopGraphicalApplication.FashionShopGraphicalApplication`

- The code to then run the program is identical because we made the
  API’s match

- To emphasise this we have included `FashionShopShellUI.py` with some
  minor adjustments to the `FashionShopShellApplication` (to match the
  updated `StockItem` API for handling tags)

  - Both interfaces work on the same underlying data model with no
    issues
  - Use the same Data library code

- We’ve also generated updated documentation and updated the tests

- You might find it useful to look through the full setup

- The original answer provided in the samples code implements the
  solution in a slightly different way

  - There’s value in looking at both approaches
  - Though I would argue that my implementation has much better handling
    of state to avoid bugs

## Summary

## Questions and Answers
