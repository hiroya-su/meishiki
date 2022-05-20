from dataclasses import dataclass
from datetime import datetime

@dataclass(slots = True)
class Meishiki:

    birthday: datetime
    sex: int


def build_meishiki(birthday, sex):
    pass


