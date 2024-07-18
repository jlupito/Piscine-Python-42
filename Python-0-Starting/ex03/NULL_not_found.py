def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Empty: {object} {repr(type(object))}")
    elif object != object:
        print(f"Cheese: {object} {repr(type(object))}")
    elif object == "":
        print(f"Nothing: {object} {repr(type(object))}")
    elif object == 0:
        print(f"Zero: {object} {repr(type(object))}")
    elif object == False:
        print(f"Fake: {object} {repr(type(object))}")
    else:
        print("Type not found")
        return 1
    return 0