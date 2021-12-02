def parse_data(data, objects_format, separator=" "):
    """
    Takes a list of strings and a list of objects format and returns a list of objects formatted according to the objects format.
    Example:
        parse_data(['forward 10', 'left 90', 'right 90'], [{'key': 'command, 'format': str}, {'key': 'value', 'format': int}], " ") =>
        [{'command': 'forward', 'value': 10}, {'command': 'left', 'value': 90}, {'command': 'right', 'value': 90}]
    """
    result = []
    for line in data:
        line_result = {}
        for i, value in enumerate(line.split(separator)):
            line_result[objects_format[i]["key"]] = objects_format[i]["format"](value)
        result.append(line_result)
    return result
