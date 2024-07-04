def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given the initial set of keys.

    Parameters:
    boxes (list of lists): Each index i contains a list of keys for boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)  # Total number of boxes
    opened = [False] * n  # Track whether each box has been opened
    opened[0] = True  # The first box (index 0) is initially open

    keys = [0]  # Start with the key to the first box

    while keys:
        current_key = keys.pop()  # Get a key to use
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True  # Mark the box as opened
                keys.append(key)

    return all(opened)  # Return True if all boxes have been opened, else False
