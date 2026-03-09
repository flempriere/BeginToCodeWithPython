# Create Games with PyGame

- [Notes](#notes)
  - [Getting Started with PyGame](#getting-started-with-pygame)
    - [Make Something Happen: Start PyGame and Draw Some
      Lines](#make-something-happen-start-pygame-and-draw-some-lines)
    - [Make Something Happen: Making
      Art](#make-something-happen-making-art)
- [Questions and Answers](#questions-and-answers)

## Notes

### Getting Started with PyGame

- PyGame is a module for creating games
- This means that it includes support for graphics, sound, shapes etc.
- We’ve already seen this, pygame powered the [snaps
  module](../../01_ProgrammingFundamentals/03_PythonProgramStructure/Chapter_03.qmd#adding-some-snaps)
- pygame uses tuples to create items that contain colours and
  coordinates
  - Make sure you’re familiar with tuples (see [Chapter
    8](../../01_ProgrammingFundamentals/08_StoringCollectionsOfData/Chapter_08.qmd#tuples))

#### Make Something Happen: Start PyGame and Draw Some Lines

*The best way to learn is to dive right in. Open up the python
interpreter and work through the following steps*

1. *load* `pygame`

    - This is done through the usual import

      ``` python
        import pygame
      ```

    - We can now use pygame’s functions and classes

2. *Initialise pygame*

    - The pygame framework needs to be initialised

    - This handles setting everything up

    - do so as follows

      ``` python
        pygame.init()
      ```

    - This sets up the pygame elements for handling various tasks

    - This includes,

      1. Reading user input
      2. Making sounds
      3. and more…

    - `init` returns a tuple indicating how many elements have
      initialised and how many have failed

    - If an element fails to initialise it can indicate that pygame
      hasn’t installed correctly

      1. The first element of the tuple is the number of successfully
          initialised elements
      2. The second element of the tuple is the number of failed
          elements

3. *Create a drawing surface*

    - To draw objects we first need to define a drawing surface

    - Drawing surface has a fixed size

      - Set at the time of creation
      - Size is specified in pixels
      - More pixels give a better quality display

      ``` python
        size = (800, 600)
      ```

    - We can then use this size tuple to create our display

      ``` python
        surface = pygame.display.set_mode(size)
      ```

    - This creates a drawing surface, references it with the variable
      `surface`

    - The result is then displayed

4. *Set the title*

    - Like with `tkinter` these windows have methods for changing how
      they display

    - We can change the title

    - Do so as follows,

      ``` python
        pygame.display.set_caption("An awesome game")
      ```

5. *Draw something on the canvas*

    - Now we can draw on the canvas

    - For example we can draw a line

    - This takes four arguments

      1. The surface to draw on
      2. The drawing colour
      3. The start position of the line
      4. The end position of the line

    - We already have our surface

    - Next define a colour

      - This is a 3-tuple containing red, green, blue values from $0$ to
        $255$
        - The lowest level is $0$
        - The highest level is $255$

        ``` python
          red = (255, 0, 0)
        ```

    - Now we need to define the start and end coordinates

    - Like with tkinter

      - $x$ coordinate measures from the left of the screen to the right
      - $y$ coordinate measures from the top of the screen to the bottom

    - We then represent a coordinate with a tuple `(x, y)`

    - Define our coordinates as below

      ``` python
        start = (0,0)
        end = (500, 300)
      ```

    - Now we just have to issue our actual drawing command

      ``` python
        pygame.draw.line(surface, red, start, end)
      ```

          <rect(0, 0, 501, 301)>

    - This returns a rectangle object enclosing the line

    - You can ignore this

6. *Render the line*

    - Looking at the window we can see that no line has appeared

    - Draw operations end up on the *back buffer*

      - Managed by pygame

    - We don’t draw directly on the screen for every draw command

      - In the context of a video game we don’t want to do every draw
        immediately
      - This is quite slow
      - We also might want to only show the final result rather than the
        immediate states

    - Instead all operations are drawn to the back buffer

      - When drawing is done this copy can be drawn over the display
        memory to replace it
      - The memory then used to display becomes the new back buffer
      - We then repeat

    - The `flip` function is used to swap the display and back buffer
      memory

    - Call it now

      ``` python
        pygame.display.flip()
      ```

7. *Change the background*

    - Currently the background is black

    - We can use the `fill` function to change the background colour

    - The below creates a tuple with the colour white, paints the
      background, then applies this

      ``` python
        white = (255, 255, 255)
        surface.fill(white)
        pygame.display.flip()
      ```

    - You’ll notice this has erased the red line

- We can use these functions to create some images
- We’ll create a function to draw $100$ randomly coloured and positioned
  lines and dots

``` python
"""
Example 16.2 Pygame Drawing Functions

Demonstrates the use of pygame's drawing functionality to create
some artwork
"""

import random

import pygame


class DrawDemo:
    """
    Draws an image of randomly coloured and positioned lines and dots
    """

    @staticmethod
    def do_draw_demo():
        """
        Create a demonstration display
        """
        init_result = pygame.init()
        if init_result[1] != 0:
            print("Failed to initialise all elements, check pygame installation")

        width = 800
        height = 600
        size = (width, height)

        def get_random_coordinates():
            """
            Generates a random (X,Y) coordinate tuple

            Returns
            -------
            tuple[int, int]
                X,Y coordinates
            """
            X = random.randint(0, width - 1)
            Y = random.randint(0, height - 1)

            return (X, Y)

        def get_random_colour():
            """
            Generate a random (R,G,B) colour tuple

            Returns
            -------
            tuple[int, int, int]
                R,G,B colour tuple
            """
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            return (red, green, blue)

        surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Drawing Example")

        red = (255, 0, 0)  # noqa: F841
        green = (0, 255, 0)  # noqa: F841
        blue = (0, 0, 255)  # noqa: F841
        black = (0, 0, 0)  # noqa: F841
        yellow = (255, 255, 0)  # noqa: F841
        magenta = (255, 0, 255)  # noqa: F841
        cyan = (0, 255, 255)  # noqa: F841
        white = (255, 255, 255)
        gray = (128, 128, 128)  # noqa: F841

        surface.fill(white)

        for count in range(100):
            start = get_random_coordinates()
            stop = get_random_coordinates()
            colour = get_random_colour()
            pygame.draw.line(surface, colour, start, stop)

        for count in range(100):
            pos = get_random_coordinates()
            colour = get_random_colour()
            radius = random.randint(5, 50)
            pygame.draw.circle(surface, colour, pos, radius)

        pygame.display.flip()


DrawDemo.do_draw_demo()
```

- The output should look similar (but slightly different) to the below

  ![Image generated using
  pygame](./Examples/02_PygameDraw/drawing_program.png)

- As a personal aside, since we’re implemented `do_draw_demo` as a
  static method there isn’t really a need for there to be a class here

- We could really just write `do_draw_demo` as a standalone function

#### Make Something Happen: Making Art

*Create a program that varies a displayed pattern. Use the time of day
and the weather to adjust the colours. Use bright primary colours in the
morning and more mellow dark colours in the evening. If the weather is
warm, the colours could have a red tinge, and if it’s colder, you could
create colours with more blues. Remember that you can create any colour
you like for you graphics by modifying the amount of red, green and
blue*

This one is quite a fun little program. We’ll use the core
implementation from [the previous
example](#make-something-happen-start-pygame-and-draw-some-lines). The
basic idea is to wrap the drawing code in a loop that will periodically
redraw the image. The second step is to add code that will adjust the
weighting of the generated colour in response to the time of day and the
current weather.

Lets plan out how we generate out colours first. Before we generated a
colour by randomly generating red, green, blue colour values from $0$ to
$255$ using a uniform distribution. This means that each colour value is
equally likely. We could tune the uniform distribution, e.g. by limiting
it to a subrange of a colour value, then shifting this up and down the
spectrum, but we’ll instead use another distribution, the *gaussian*. A
guassian distribution also called the normal distribution, lets us
define a mean point, then the standard deviation (or spread) for our
colour value. We can then clip the values to ensure they remain in the
$0$ to $255$ range. The advantage of this is that we can then easily
shift the mean to weight towards specific colours, but we still have a
chance of generating any possible colour.

The code implementing this is given below

``` python
    def get_random_colour(means):
        """
        Generate a random (R,G,B) colour tuple

        Parameters
        ----------
        means : tuple[int, int, int]
            Tuple containing the mean values in RGB space for the generated
            colours

        Returns
        -------
        tuple[int, int, int]
            R,G,B colour tuple
        """

        def random_single_colour_channel(mean, sigma):
            """
            Generate a random single colour value from 0 to 255

            Number is generated using a clipped gaussian

            Parameters
            ----------
            mean : int | float
                mean generated colour value
            sigma : int | float
                standard deviation in generated colour

            Returns
            -------
            int
                colour channel value between 0 and 255 inclusive
            """
            return int(max(0, min(255, random.gauss(mean, sigma))))

        sigma = 20
        red = random_single_colour_channel(means[0], sigma)
        green = random_single_colour_channel(means[1], sigma)
        blue = random_single_colour_channel(means[2], sigma)

        return (red, green, blue)
```

- We set our standard deviation to $20$

  - This was chosen through trial and error, to give a decent spread of
    colours

- `random_single_colour_channel` takes a mean and sigma (standard
  deviation), then generates a colour value using a Gaussian
  distribution

  - We then clip the value to the range $0$ to $255$

- `get_random_colour` wraps the above function

  - It defines the standard deviation
  - Then generates colour values for red, green and blue
  - It accepts a tuple of means corresponding to the mean red, green and
    blue component
    - This lets us shift the mean amount of each individual colour
      individually

- We then want to add code to shift these means based on the temperature
  and time of day

- For temperature, we want to increase the amount of red when it is hot,
  and increase the amount of blue when it is cold

- We first need to get the temperature data, which we do by using the
  Weather Data program from [Chapter
  14](../14_PythonProgramsAsNetworkClients/Chapter_14.qmd#make-something-happen-work-with-weather-data)
  as a module

- We then want to convert the temperature to celsius (because I
  intuitively understand those values)

  - We then use a basic formula for shifting the mean, we use the
    formula,

    $$
      \left(R, G, B\right) = \text{scale} \times \left(\text{temperature} - \text{offset}\right)
    $$

  - The idea is we define a *hot* threshold, and then increase the red
    the more the temperature is above this threshold

  - We then scale this by a scale factor to ensure the appropriate
    impact on the mean

  - We define a similar setup for a *cold* threshold to increase the
    blue

  - We want to return the final result as a tuple of R,G,B shift,
    because this will be easier to work with and means we don’t need to
    denote which colour value we are adjusted

  ``` python
    def fahrenheit_to_celsius(temperature):
        """
        Convert fahrenheit to celsius

        Parameters
        ----------
        temperature : int | float
            the temperature in fahrenheit

        Returns
        -------
        int | float
            temperature in celsius
        """
        return (temperature - 32.0) * (5 / 9)


    def convert_temperature_to_colour_shift(temperature):
        """
        Convert the given temperature into an RGB colour shift

        Low temperatures give a blue shift, high temperatures give a red shift

        Parameters
        ----------
        temperature : int | float
            the current temperature

        Returns
        -------
        tuple[int, int, int]
            tuple giving the colour shift in RGB
        """
        scale_factor = 10
        # if hot increase the amount of red (more heat = more red)
        if temperature > 25:
            return (scale_factor * (int(temperature) - 25), 0, 0)
        # if cold increase the amount of blue (lower temp = more blue)
        elif temperature < 10:
            return (0, 0, -scale_factor * (temperature - 10))  # i.e. 10 -> 0, -10 -> 20
        else:
            return (0, 0, 0)
  ```

- We then want to use the same idea for the time. However in this case
  we want higher saturation colours early in the morning, and low
  saturation colours late in the day

  - A high saturation colour has high values across $(R,G,B)$
  - A low saturation colour has low values across $(R,G,B)$
    - So we want to adjust the mean across all three colours

  ``` python
    def convert_hour_to_colour_shift(hour):
        """
        Convert the given time into an RGB colour shift

        Night times give a shift towards smaller RGB values, morning times
        give a shift towards larger RGB values

        Parameters
        ----------
        hour : int
            the current hour

        Returns
        -------
        tuple[int, int, int]
            RGB colour tuple giving the colour shift in RGB space
        """

        scale_factor = 20
        offset = 12

        if 6 <= hour <= 12:
            # want morning to increase the average
            shift = scale_factor * (offset - hour) # shift range: (0 - 120)
        elif 18 <= hour or hour < 6:
            # want evening to decrease the range
            shift = -(scale_factor * abs(offset - hour)) # shift range (0 - 120)
        else:
            shift = 0

        return (shift, shift, shift)
  ```

- We use the same kind of formula as before, however this time we shift
  the mean for all three colours

- We have two cases

  - Morning, in which case we can use the simple formula before (We
    define morning as between $6$ and $12$)
  - Evening, here we want to get more mellow as we get close to
    midnight, then progressively less mellow
  - So we can use the same idea as before but we want to use `abs` or
    absolute value to effectively measure the distance of the current
    hour to midnight

- The drawing code is then given as

  ``` python
    def draw_art(surface, width, height, hour, temperature):
        """
        Draw an artwork with time and temperature dependent colouring

        Parameters
        ----------
        surface : surface
            pygame surface to draw on
        width : int
            width of the image in pixels
        height : int
            height of the image in pixels
        hour : int
            The current hour
        temperature : int | float
            The current temperature
        """

        def get_random_coordinates():
            """
            Generates a random (X,Y) coordinate tuple

            Returns
            -------
            tuple[int, int]
                X,Y coordinates
            """
            X = random.randint(0, width - 1)
            Y = random.randint(0, height - 1)

            return (X, Y)

        def get_random_colour(means):
            """
            Generate a random (R,G,B) colour tuple

            Parameters
            ----------
            means : tuple[int, int, int]
                Tuple containing the mean values in RGB space for the generated
                colours

            Returns
            -------
            tuple[int, int, int]
                R,G,B colour tuple
            """

            def random_single_colour_channel(mean, sigma):
                """
                Generate a random single colour value from 0 to 255

                Number is generated using a clipped gaussian

                Parameters
                ----------
                mean : int | float
                    mean generated colour value
                sigma : int | float
                    standard deviation in generated colour

                Returns
                -------
                int
                    colour channel value between 0 and 255 inclusive
                """
                return int(max(0, min(255, random.gauss(mean, sigma))))

            sigma = 20
            red = random_single_colour_channel(means[0], sigma)
            green = random_single_colour_channel(means[1], sigma)
            blue = random_single_colour_channel(means[2], sigma)

            return (red, green, blue)

        white = (255, 255, 255)
        surface.fill(white)

        mean = 128
        means = (mean, mean, mean)
        hour_shift = convert_hour_to_colour_shift(hour)
        temperature_shift = convert_temperature_to_colour_shift(temperature)

        new_means = []
        for i in range(len(means)):
            new_means.append(means[i] + hour_shift[i] + temperature_shift[i])
        means = tuple(new_means)

        for count in range(100):
            start = get_random_coordinates()
            stop = get_random_coordinates()
            colour = get_random_colour(means)
            pygame.draw.line(surface, colour, start, stop)

        for count in range(100):
            pos = get_random_coordinates()
            colour = get_random_colour(means)
            radius = random.randint(5, 50)
            pygame.draw.circle(surface, colour, pos, radius)

        pygame.display.flip()


    def update_artwork_mainloop():
        """
        Create an art work that updates hourly
        """
        init_result = pygame.init()
        if init_result[1] != 0:
            print("Failed to initialise all elements, check pygame installation")

        width = 800
        height = 600
        size = (width, height)

        surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Drawing Example")

        while True:
            hour = time.localtime().tm_hour
            latitude = 47.61
            longitude = -122.33

            _, _, temperature, _ = WeatherData.get_weather_temp(
                latitude=latitude, longitude=longitude
            )
            temperature = fahrenheit_to_celsius(temperature)
            print(
                "Updating artwork, it is {0} and the temperature is {1}C".format(
                    hour, temperature
                )
            )
            draw_art(surface, width, height, hour, temperature)
            time.sleep(60 * 30) # update every 30 minutes


    update_artwork_mainloop()
  ```

- This program will redraw the artwork every half an hour

- When it does it pulls the current time and temperature (We’re sticking
  with Seattle here)

- Then redraws the image

- Two example images are shown below

  ![Art generated at late
  night](./Exercises/01_MakingArt/late_night.png) ![Art generated in the
  morning](./Exercises/01_MakingArt/cold_morning.png)

- ## Summary

## Questions and Answers
