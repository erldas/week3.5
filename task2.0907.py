def metod():
    dict_ = {'name': 'John', 'lastname': 'Jones', 23: 'age'}
    for x in dict_.keys():
        try:
            x + 'abc'
        except TypeError:
            str(x)+'abc'
    print(dict_)
metod()

