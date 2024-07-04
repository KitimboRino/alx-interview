def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given the initial set of keys.

    Parameters:
    boxes (list of lists): Each index i contains a list of keys for boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
