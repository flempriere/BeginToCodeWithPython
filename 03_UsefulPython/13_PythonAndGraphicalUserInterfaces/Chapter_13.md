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

## Summary

## Questions and Answers
