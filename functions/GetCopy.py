def GetCopy(instance):
    assert isinstance(instance, list), \
        f"Expected List, got {type(instance)}"

    instance.sort()

    copies = []
    prev = None
    
    for i in instance:
        if i == prev:
            copies.append(i)
        else:
            prev = i

    return copies