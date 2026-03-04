def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    result = ""
    i = 0
    while i < len(line):
        if line[i:i + 1] == "*" and line.find("*", i + 1) != -1:
            end = line.find("*", i + 1)
            if end != -1:
                result += "<i>" + line[i + 1: end] + "</i>"
                i = end + 1
            else:
                result += line[i]
                i += 1
        else:
            result += line[i]
            i += 1

    return result
    