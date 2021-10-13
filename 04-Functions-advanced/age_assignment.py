def age_assignment(*args, **kwargs, ):
    # names_age = {}
    # for name in args:
    #     first_letter = name[0]
    #     names_age[name] = kwargs[first_letter]
    #
    # return names_age

    return {x: kwargs[x[0]] for x in args}


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))