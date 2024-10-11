from collections import deque

def convert(ratios, from_unit, to_unit, value):
    """
    Converts a value from one unit to another using the provided ratios.

    Args:
        ratios (dict): Dictionary of conversion ratios.
        from_unit (str): Unit of the input value.
        to_unit (str): Desired unit of the output value.
        value (float): Value to be converted.

    Returns:
        float or None: Converted value or None if conversion is impossible.
    """

    # Create a conversion graph
    graph = {}
    for (unit1, unit2), ratio in ratios.items():
        graph.setdefault(unit1, {})[unit2] = ratio
        graph.setdefault(unit2, {})[unit1] = 1 / ratio

    # Find conversion path using Breadth-First Search
    queue = deque([(from_unit, value)])
    visited = set()

    while queue:
        unit, current_value = queue.popleft()
        visited.add(unit)

        if unit == to_unit:
            return current_value

        for next_unit, ratio in graph[unit].items():
            if next_unit not in visited:
                queue.append((next_unit, current_value * ratio))

    return None

