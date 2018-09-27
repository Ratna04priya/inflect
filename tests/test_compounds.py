from nose.tools import eq_

import inflect

p = inflect.engine()


def test_compound_1():
    eq_(p.singular_noun('hello-out-there'), 'hello-out-there')


def test_compound_2():
    eq_(p.singular_noun('hello out there'), 'hello out there')


def test_compound_3():
    eq_(p.singular_noun('continue-to-operate'), 'continue-to-operate')


def test_compound_4():
    eq_(p.singular_noun('case of diapers'), 'case of diapers')


def test_unit_handling_degree():
    test_cases = {
        'degree celsius': 'degrees celsius',
        'degree fahrenheit': 'degrees fahrenheit',
        'degree rankine': 'degrees rankine'
    }
    for singular, plural in test_cases.items():
        eq_(p.plural(singular), plural)


def test_unit_handling_fractional():
    test_cases = {
        'pound per square inch': 'pounds per square inch',
        'pound-force per square inch': 'pound-forces per square inch',
        'metre per second': 'metres per second',
        'kilometre per hour': 'kilometres per hour',
        'foot per square second': 'feet per square second',
        'cubic metre per second': 'cubic metres per second',
        'dollar a year': 'dollars a year'
    }
    for singular, plural in test_cases.items():
        eq_(p.plural(singular), plural)
