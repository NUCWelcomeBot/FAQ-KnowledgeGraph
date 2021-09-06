from enum import Enum


class Type(Enum):
    # 为序列值指定value值
    INT = 1
    TEXT = 2
    VIDEO = 3
    PIC = 4
    MessageChain = 5  # 消息链，图文并茂形式
