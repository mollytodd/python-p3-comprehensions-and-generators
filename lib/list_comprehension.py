#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def make_exclamation(sentence_list):
    exclimation_list = [word +"!" for word in sentence_list]
    return exclimation_list