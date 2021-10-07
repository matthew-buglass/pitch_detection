#   Copyright (c) Matthew Buglass
#   Author: Matthew Buglass
#   Maintainer: Matthew Buglass
#   Website: matthewbuglass.com
#   Date: 2021/10/6

# implementation of an Fourier-transform to perform pitch detection of live audio

import scipy
import cmath


def natural_exponential(rotational_frequency):
    """
    Returns a function representing the natural exponential portion of the
    Fourier transform integration. Contains an irrational number in the exponent.
    :param rotational_frequency: The frequency that we are testing for
    :return: a function with 1 parameter, which will be the time for the integration
    """
    e = cmath.exp(1)
    non_variate_expo = 2 * cmath.pi * complex(0, 1) * rotational_frequency

    return lambda x: e ** (non_variate_expo * x)


def custom_sin(frequency):
    """
    Returns a custom sin function with the given frequency in Hz
    :param frequency: the desired frequency of the sin wave
    :return: A sin function with the given frequency
    """
    return lambda x: cmath.sin((x*cmath.pi) * frequency)


def custom_cos(frequency):
    """
    Returns a custom cos function with the given frequency in Hz
    :param frequency: the desired frequency of the cos wave
    :return: A cos function with the given frequency
    """
    return lambda x: cmath.cos((x*cmath.pi) * frequency)


def multiply_single_variate_functions(func_1, func_2):
    """
    Combines two single variate functions and returns a new function that is
    both original functions multiplied together.
    :param func_1: First function to multiply.
    :param func_2: Second function to multiply.
    :return: A new function that is the product of the 2 given functions.
    """
    return lambda x: func_1(x) * func_2(x)

