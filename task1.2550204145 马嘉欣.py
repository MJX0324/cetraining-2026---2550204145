def is_balanced(s: str) -> bool:
    """
    判断字符串中的括号是否匹配。

    支持的括号类型：
    - 圆括号: ( )
    - 方括号: [ ]
    - 花括号: { }

    Args:
        s: 输入字符串

    Returns:
        True 如果所有括号正确匹配，否则 False

    Examples:
        >>> is_balanced("()")
        True
        >>> is_balanced("()[]{}")
        True
        >>> is_balanced("(]")
        False
        >>> is_balanced("([)]")
        False
        >>> is_balanced("{[]}")
        True
        >>> is_balanced("a(b[c]d)e")
        True
        >>> is_balanced("(")
        False
        >>> is_balanced("")
        True
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    # 测试用例
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("a(b[c]d)e", True),
        ("(", False),
        ("", True),
        ("(((())))", True),
        ("{[}]", False),
        ("[{()}]", True),
    ]

    all_passed = True
    for s, expected in test_cases:
        result = is_balanced(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"[{status}] is_balanced({s!r}) = {result}, 期望 {expected}")

    print(f"\n{'全部测试通过!' if all_passed else '存在未通过的测试'}")