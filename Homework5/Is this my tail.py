def correct_tail(body, tail):
    return (body[len(body) - 1: ] == tail)
    if body == tail:
        return True
    else:
        return False