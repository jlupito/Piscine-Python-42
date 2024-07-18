def all_thing_is_obj(object: any) -> int:
    if type(object) == str:
        print(f"{object} is in the kitchen: {repr(type(object))}")
    elif type(object) == list or type(object) == set or type(object) == tuple or type(object) == dict:
        print(f"{type(object).__name__.capitalize()} : {repr(type(object))}")
    else:
        print("Type not found")
    return 42