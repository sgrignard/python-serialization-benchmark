from subjects import rf, serp, strain, col, hand, loli, k, lim, tmarsh, serpy
from data import ParentTestObject
import pprint

TARGET = {
    "foo": "bar",
    "bar": 5,
    "sub": {"w": 100, "y": "hello", "z": 10, "x": 30},
    "subs": [
        {"w": 100, "y": "hello", "z": 10, "x": 30},
        {"w": 1000, "y": "hello", "z": 10, "x": 30},
        {"w": 2000, "y": "hellohello", "z": 20, "x": 50},
        {"w": 3000, "y": "hellohellohello", "z": 30, "x": 70},
        {"w": 4000, "y": "hellohellohellohello", "z": 40, "x": 90},
        {"w": 5000, "y": "hellohellohellohellohello", "z": 50, "x": 110},
        {"w": 6000, "y": "hellohellohellohellohellohello", "z": 60, "x": 130},
        {"w": 7000, "y": "hellohellohellohellohellohellohello", "z": 70, "x": 150},
        {"w": 8000, "y": "hellohellohellohellohellohellohellohello", "z": 80, "x": 170},
        {
            "w": 9000,
            "y": "hellohellohellohellohellohellohellohellohello",
            "z": 90,
            "x": 190,
        },
    ],
}


def test_serializers():
    test_object = ParentTestObject()

    for subject in (rf, tmarsh, serp, strain, col, hand, loli, k, lim, serpy):
        print(subject.name)
        data = subject.serialization_func(test_object, False)
        pprint.pprint(data)
        assert str(data["foo"]) == str(TARGET["foo"])
        assert str(data["bar"]) == str(TARGET["bar"])
        assert str(data["sub"]["w"]) == str(TARGET["sub"]["w"])
        assert str(data["subs"][3]["y"]) == str(TARGET["subs"][3]["y"])
        assert str(data["subs"][3]["x"]) == str(TARGET["subs"][3]["x"])

        datas = subject.serialization_func([test_object, test_object], True)
        for data in datas:
            assert str(data["foo"]) == str(TARGET["foo"])
            assert str(data["sub"]["w"]) == str(TARGET["sub"]["w"])
            assert str(data["subs"][3]["y"]) == str(TARGET["subs"][3]["y"])
            assert str(data["subs"][3]["x"]) == str(TARGET["subs"][3]["x"])


if __name__ == "__main__":
    test_serializers()
