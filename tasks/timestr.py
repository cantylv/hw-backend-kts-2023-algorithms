__all__ = (
    'seconds_to_str',
)


"""
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
"""

def seconds_to_str(seconds: int) -> str:

    if seconds == 0:
        return "00s"

    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    time_string = ""
    xx_format = False
    if days > 0:
        time_string += f"{days:02}d"
        xx_format = True
    if hours > 0 or xx_format:
        time_string += f"{hours:02}h"
        xx_format = True
    if minutes > 0 or xx_format:
        time_string += f"{minutes:02}m"
        xx_format = True
    if seconds > 0 or xx_format:
        time_string += f"{seconds:02}s"

    return time_string




