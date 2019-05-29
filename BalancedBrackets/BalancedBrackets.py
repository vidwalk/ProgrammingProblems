from __future__ import print_function, division


def balance(s):
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            # Check character is not unmatched
            if not stack:
                return False

            # Char is a closing bracket, check top of stack if it matches
            if (char == ")" and stack[-1] != "(") or \
               (char == "]" and stack[-1] != "[") or \
               (char == "}" and stack[-1] != "{"):
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    assert balance('([])[]({})')
    assert balance('([)]') == False
