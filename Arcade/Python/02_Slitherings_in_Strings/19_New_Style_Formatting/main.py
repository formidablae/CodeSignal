import re


def solution(s):
    return re.sub(
        '{%}',
        '%',
        re.sub(
            '%[bcdefgosxX]',
            '{}',
            re.sub(
                '%%',
                '{%}',
                s
            )
        )
    )
