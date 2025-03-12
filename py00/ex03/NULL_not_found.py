def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing: None <class 'NoneType'>")
    elif object != object:
        print("Cheese: nan <class 'float'>") 
    elif object == "":
        print("Empty: <class 'str'>")
    elif object is False:
        print("Fake: False <class 'bool'>")
    elif object == 0 and object is not False:
        print("Zero: 0 <class 'int'>")
    else:
        print("Type not Found")
        return 1

    return 0


