import dataclasses
import typing

import serpyco

from data import ParentTestObject

name = "Serpyco"


def get_x(obj):
    return obj.x + 10


@dataclasses.dataclass
class SubM(object):
    w: int
    x: int = serpyco.field(getter=get_x)
    y: str
    z: int


@dataclasses.dataclass
class ComplexM(object):
    bar: int = serpyco.field(getter=ParentTestObject.bar)
    foo: str
    sub: SubM
    subs: typing.List[SubM]


serializer = serpyco.Serializer(ComplexM)
many_serializer = serpyco.Serializer(ComplexM, many=True)


def serialization_func(obj, many):
    if many:
        return many_serializer.dump(obj)
    return serializer.dump(obj)
