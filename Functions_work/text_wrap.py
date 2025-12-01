import textwrap
def wrap(s,width):
    wrapped_lines=textwrap.wrap(s,width)
    return "\n".join(wrapped_lines)

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4))