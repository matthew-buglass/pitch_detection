#   Copyright (c) Matthew Buglass
#   Author: Matthew Buglass
#   Maintainer: Matthew Buglass
#   Website: matthewbuglass.com
#   Date: 2021/10/6

# implementation of an Fourier-transform to perform pitch detection of live audio

import scipy
from scipy import integrate
import cmath


def natural_exponential(rotational_frequency):
    """
    Returns a function representing the natural exponential portion of the
        Fourier transform integration. Contains an irrational number in the exponent.
    :param rotational_frequency: The frequency that we are testing for.
    :return: a function with 1 parameter, which will be the time for the integration.
    """
    non_variate_expo = 2 * cmath.pi * complex(0, 1) * rotational_frequency

    return lambda x: scipy.e ** (non_variate_expo * x)


def custom_sin(frequency):
    """
    Returns a custom sin function with the given frequency in Hz.
    :param frequency: the desired frequency of the sin wave.
    :return: A sin function with the given frequency.
    """
    return lambda x: cmath.sin((x*cmath.pi) * frequency)


def custom_cos(frequency):
    """
    Returns a custom cos function with the given frequency in Hz.
    :param frequency: the desired frequency of the cos wave.
    :return: A cos function with the given frequency.
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


def fourier_transform(function, test_freq: list, integrate_low, integrate_high):
    """
    Returns a list of peak frequencies present in the oscillating
    wave of the provided function.
    :param function: A single variate oscillating function that the
        fourier transform is to be applied on.
    :param test_freq: A list of frequencies that are to be looked for in the
        provided function.
    :param integrate_low: The lower bound on the integration
    :param integrate_high: The upper bound on the integration
    :return: A list of floating point numbers that are the the resulting centers
        of mass of the fourier transform (ie. underlying frequencies).
    """
    coms = []    # a list of centers of mass for the tested frequencies

    for f in test_freq:
        natural_component = natural_exponential(f)
        transform_equation = multiply_single_variate_functions(function, natural_component)
        com = integrate.quad(transform_equation, integrate_low, integrate_high)
        coms.append(com)

    peak_com = 0
    results = []
    for c in coms:
        if c > peak_com:
            results = []
