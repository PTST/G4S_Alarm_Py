from enum import Enum


class ArmType(Enum):
    FULL_ARM = 0
    NIGHT_ARM = 1
    UNKNOWN = 2
    DISARMED = 3

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return str(self)


class DeviceType(Enum):
    Unknown = -1
    Hub = 1
    DoorWindowSensor = 2
    Panel = 14
    Smokealarm = 16
    Siren = 24
    Camera = 38
    ZWaveController = 116
    AccessChip = 201

    @classmethod
    def _missing_(cls, value):
        return DeviceType.Unknown

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return str(self)


class EventType(Enum):
    Unknown = -1
    Arm = 39
    Disarm = 40
    NightArm = 57

    @classmethod
    def _missing_(cls, value):
        return EventType.Unknown

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return str(self)
