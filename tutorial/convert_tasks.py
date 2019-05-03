from typing import NamedTuple


class ConvertTask(NamedTuple):
    img_dir: str
    model: str
    convert_args: list


CONVERT_TASKS = {
    "marcpuels-for-trumpsample": ConvertTask("trumpsample",
                                             "trump-marcpuels",
                                             [])
}
