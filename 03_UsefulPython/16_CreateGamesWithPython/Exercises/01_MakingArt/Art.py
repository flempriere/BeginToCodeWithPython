"""
Exercise 16.1 Making Art

This program creates an artwork that updates every hour. The colour gets
mellow as the day progresses, and shifts the level of blue and red is response
to the temperature
"""

import random
import time

import pygame
import WeatherData


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
        shift = scale_factor * (offset - hour)  # shift range: (0 - 120)
    elif 18 <= hour or hour < 6:
        # want evening to decrease the range
        shift = -(scale_factor * abs(offset - hour))  # shift range (0 - 120)
    else:
        shift = 0

    return (shift, shift, shift)


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
        time.sleep(60 * 30)  # update every 30 minutes


update_artwork_mainloop()
