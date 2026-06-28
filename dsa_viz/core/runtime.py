import os


DEFAULT_INPUT = [8, 3, 5, 1, 6]


def get_runtime_input():
    """
    Reads runtime input passed from run.py.

    Example:
        DSA_INPUT=8,3,5,1,6

    Returns:
        list[int]
    """

    raw = os.getenv("DSA_INPUT")

    if not raw:
        return DEFAULT_INPUT.copy()

    try:
        values = [int(x.strip()) for x in raw.split(",") if x.strip()]
    except ValueError:
        print("[Runtime] Invalid input. Using default values.")
        return DEFAULT_INPUT.copy()

    if not values:
        return DEFAULT_INPUT.copy()

    return values