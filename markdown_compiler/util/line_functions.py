def compile_headers(line):
    for i in range(6, 0, -1):
        prefix = "#" * i + " "
        if line.startswith(prefix):
            return "<h" + str(i) + ">" + line[i:] + "</h" + str(i) + ">"
    return line


def compile_italic_star(line):
    result = ""
    i = 0

    while i < len(line):
        if line[i:i + 1] == "*" and line.find("*", i + 1) != -1:
            end = line.find("*", i + 1)
            result += "<i>" + line[i + 1:end] + "</i>"
            i = end + 1
        else:
            result += line[i]
            i += 1

    return result


def compile_italic_underscore(line):
    result = ""
    i = 0

    while i < len(line):
        if line[i:i + 1] == "_" and line.find("_", i + 1) != -1:
            end = line.find("_", i + 1)
            result += "<i>" + line[i + 1:end] + "</i>"
            i = end + 1
        else:
            result += line[i]
            i += 1

    return result


def compile_strikethrough(line):
    result = ""
    i = 0

    while i < len(line):
        if line[i:i + 2] == "~~" and line.find("~~", i + 2) != -1:
            end = line.find("~~", i + 2)
            result += "<ins>" + line[i + 2:end] + "</ins>"
            i = end + 2
        else:
            result += line[i]
            i += 1

    return result


def compile_bold_stars(line):
    result = ""
    i = 0

    while i < len(line):
        if line[i:i + 2] == "**" and line.find("**", i + 2) != -1:
            end = line.find("**", i + 2)
            result += "<b>" + line[i + 2:end] + "</b>"
            i = end + 2
        else:
            result += line[i]
            i += 1

    return result


def compile_bold_underscore(line):
    result = ""
    i = 0

    while i < len(line):
        if line[i:i + 2] == "__" and line.find("__", i + 2) != -1:
            end = line.find("__", i + 2)
            result += "<b>" + line[i + 2:end] + "</b>"
            i = end + 2
        else:
            result += line[i]
            i += 1

    return result


def compile_code_inline(line):
    if line.startswith("```"):
        return line

    result = ""
    i = 0

    while i < len(line):
        if line[i] == "`":
            end = line.find("`", i + 1)

            if end == -1:
                result += line[i]
                i += 1
            else:
                code = line[i + 1:end]
                code = code.replace("&", "&amp;")
                code = code.replace("<", "&lt;")
                code = code.replace(">", "&gt;")

                result += "<code>" + code + "</code>"
                i = end + 1
        else:
            result += line[i]
            i += 1

    return result


def compile_links(line):
    result = ""
    i = 0

    while i < len(line):
        if line[i] == "[":
            close_b = line.find("]", i + 1)

            if close_b == -1:
                result += line[i:]
                break

            if close_b + 1 < len(line) and line[close_b + 1] == "(":
                close_p = line.find(")", close_b + 2)

                if close_p == -1:
                    result += line[i:]
                    break

                text = line[i + 1:close_b]
                url = line[close_b + 2:close_p]

                result += f'<a href="{url}">{text}</a>'
                i = close_p + 1
            else:
                result += line[i]
                i += 1
        else:
            result += line[i]
            i += 1

    return result


def compile_images(line):
    result = ""
    i = 0

    while i < len(line):
        if i + 1 < len(line) and line[i] == "!" and line[i + 1] == "[":
            close_b = line.find("]", i + 2)

            if close_b == -1:
                result += line[i:]
                break

            if close_b + 1 < len(line) and line[close_b + 1] == "(":
                close_p = line.find(")", close_b + 2)

                if close_p == -1:
                    result += line[i:]
                    break

                text = line[i + 2:close_b]
                url = line[close_b + 2:close_p]

                result += f'<img src="{url}" alt="{text}" />'
                i = close_p + 1
            else:
                result += line[i]
                i += 1
        else:
            result += line[i]
            i += 1

    return result
