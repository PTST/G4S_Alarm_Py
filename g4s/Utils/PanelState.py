from Utils.Enums import ArmType
from Utils.StaticUtils import StaticUtils


class PanelState(object):
    def __init__(self, inputDict: dict):
        self.ArmType = ArmType(inputDict.get("ArmType"))
        self.ArmTypeChangedTime = StaticUtils.ParseDate(
            inputDict.get("ArmTypeChangedTime")
        )
        self.ArmForcedState = inputDict.get("ArmForcedState")
        self.ArmDelayedState = inputDict.get("ArmDelayedState")
        self.AlarmState = inputDict.get("AlarmState")
        self.AlarmStateTime = StaticUtils.ParseDate(inputDict.get("AlarmStateTime"))
        self.Partition = inputDict.get("Partition")
        self.DeviceName = inputDict.get("DeviceName")
        self.ExitDelayArmInProcess = inputDict.get("ExitDelayArmInProcess")
        self.EntryDelayArmInProcess = inputDict.get("EntryDelayArmInProcess")
        self.ReceptionLevel = inputDict.get("ReceptionLevel")
        self.ReceptionLevelChangedTime = StaticUtils.ParseDate(
            inputDict.get("ReceptionLevelChangedTime")
        )
        self.PanelBatteryLevel = inputDict.get("PanelBatteryLevel")
        self.IsPanelOffline = inputDict.get("IsPanelOffline")
        self.IsPanelOfflineChangedTime = StaticUtils.ParseDate(
            inputDict.get("IsPanelOfflineChangedTime")
        )
        self.IsZWaveEnabled = inputDict.get("IsZWaveEnabled")
        self.IsZWaveEnabledChangedTime = StaticUtils.ParseDate(
            inputDict.get("IsZWaveEnabledChangedTime")
        )
        self.IsMainPowerConnected = inputDict.get("IsMainPowerConnected")
        self.IsMainPowerConnectedChangedTime = StaticUtils.ParseDate(
            inputDict.get("IsMainPowerConnectedChangedTime")
        )
        self.IsSimCardReady = inputDict.get("IsSimCardReady")
        self.CommunicationLink = inputDict.get("CommunicationLink")
        self.BackupChannelStatus = inputDict.get("BackupChannelStatus")
        self.BackupChannelStatusDescription = inputDict.get(
            "BackupChannelStatusDescription"
        )
        self.HasLowBattery = inputDict.get("HasLowBattery")
        self.HasLowBatteryChangedTime = StaticUtils.ParseDate(
            inputDict.get("HasLowBatteryChangedTime")
        )
        self.SetupMode = inputDict.get("SetupMode")
        self.SirensVolumeLevel = inputDict.get("SirensVolumeLevel")
        self.SirensDuration = inputDict.get("SirensDuration")
        self.SirensVolumeLevelDurationChangedTime = StaticUtils.ParseDate(
            inputDict.get("SirensVolumeLevelDurationChangedTime")
        )
        self.IsInInstallationMode = inputDict.get("IsInInstallationMode")
        self.IsInInstallationModeChangedTime = StaticUtils.ParseDate(
            inputDict.get("IsInInstallationModeChangedTime")
        )
        self.IsInSignalStrengthTest = inputDict.get("IsInSignalStrengthTest")
        self.IsInSignalStrengthTestChangedTime = StaticUtils.ParseDate(
            inputDict.get("IsInSignalStrengthTestChangedTime")
        )
        self.PanelId = inputDict.get("PanelId")
        self.IsSynchronized = inputDict.get("IsSynchronized")
        self.SirensEntryExitDuration = inputDict.get("SirensEntryExitDuration")
        self.FrtState = inputDict.get("FrtState")
        self.FrtStateChangedTime = StaticUtils.ParseDate(
            inputDict.get("FrtStateChangedTime")
        )
