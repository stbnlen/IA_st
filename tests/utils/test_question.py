from collections import Counter
from utils.question import questions


def test_questions_with_default_values():
    df = [
        "aspect1, aspect2, aspect3",
        "aspect2, aspect4",
        "aspect1, aspect5",
        "aspect3",
    ]
    aspectos = ["aspect1", "aspect2", "aspect3", "aspect4", "aspect5"]
    expected_result = Counter(
        {"aspect1": 2, "aspect2": 2, "aspect3": 2, "aspect4": 1, "aspect5": 1}
    )
    assert questions(df, aspectos) == expected_result


def test_questions_with_one_default_value():
    df = [
        "aspect1, aspect2, aspect3",
        "aspect2, aspect4",
        "aspect1, aspect5",
        "aspect3",
    ]
    aspectos = ["aspect1", "aspect2", "aspect3", "aspect4", "aspect5"]
    default_one = "aspect6"
    expected_result = Counter(
        {
            "aspect1": 2,
            "aspect2": 2,
            "aspect3": 2,
            "aspect4": 1,
            "aspect5": 1,
            "aspect6": 1,
        }
    )
    assert questions(df, aspectos, default_one=default_one) == expected_result


def test_questions_with_two_default_values():
    df = [
        "aspect1, aspect2, aspect3",
        "aspect2, aspect4",
        "aspect1, aspect5",
        "aspect3",
    ]
    aspectos = ["aspect1", "aspect2", "aspect3", "aspect4", "aspect5"]
    default_one = "aspect6"
    default_two = "aspect7"
    expected_result = Counter(
        {
            "aspect1": 2,
            "aspect2": 2,
            "aspect3": 2,
            "aspect4": 1,
            "aspect5": 1,
            "aspect6": 1,
            "aspect7": 1,
        }
    )
    assert (
        questions(df, aspectos, default_one=default_one, default_two=default_two)
        == expected_result
    )
