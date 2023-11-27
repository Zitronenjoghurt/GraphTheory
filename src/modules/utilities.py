def get_safe(lst: list, index: int, default = None):
    if not isinstance(lst, list):
        return default

    try:
        return lst[index]
    except IndexError:
        return default