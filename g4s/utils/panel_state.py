from datetime import datetime
from typing import Optional
from g4s.utils.time_zone import TimeZone
from g4s.utils.enums import ArmType


class PanelState:
    def __init__(self, input_dict: dict[str, any], time_zone: TimeZone) -> None:
        self.arm_type: ArmType = ArmType(input_dict.get("ArmType"))
        self.arm_type_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("ArmTypeChangedTime")
        )
        self.arm_forced_state: int = input_dict.get("ArmForcedState")
        self.arm_delayed_state: int = input_dict.get("ArmDelayedState")
        self.alarm_state:int = input_dict.get("AlarmState")
        self.alarm_state_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("AlarmStateTime")
        )
        self.partition: int = input_dict.get("Partition")
        self.device_name: any = input_dict.get("DeviceName")
        self.exit_delay_arm_in_process: bool = input_dict.get("ExitDelayArmInProcess")
        self.entry_delay_arm_in_process: bool = input_dict.get("EntryDelayArmInProcess")
        self.reception_level: int = input_dict.get("ReceptionLevel")
        self.reception_level_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("ReceptionLevelChangedTime")
        )
        self.panel_battery_level: int = input_dict.get("PanelBatteryLevel")
        self.is_panel_offline: bool = input_dict.get("IsPanelOffline")
        self.is_panel_offline_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("IsPanelOfflineChangedTime")
        )
        self.is_z_wave_enabled: bool = input_dict.get("IsZWaveEnabled")
        self.is_z_wave_enabled_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("IsZWaveEnabledChangedTime")
        )
        self.is_main_power_connected: bool = input_dict.get("IsMainPowerConnected")
        self.is_main_power_connected_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("IsMainPowerConnectedChangedTime")
        )
        self.is_sim_card_ready: bool = input_dict.get("IsSimCardReady")
        self.communication_link: int = input_dict.get("CommunicationLink")
        self.backup_channel_status: int = input_dict.get("BackupChannelStatus")
        self.backup_channel_status_description: int = input_dict.get(
            "BackupChannelStatusDescription"
        )
        self.has_low_battery: bool = input_dict.get("HasLowBattery")
        self.has_low_battery_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("HasLowBatteryChangedTime")
        )
        self.setup_mode: bool = input_dict.get("SetupMode")
        self.sirens_volume_level: int = input_dict.get("SirensVolumeLevel")
        self.sirens_duration: int = input_dict.get("SirensDuration")
        self.sirens_volume_level_duration_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("SirensVolumeLevelDurationChangedTime")
        )
        self.is_in_installation_mode: bool = input_dict.get("IsInInstallationMode")
        self.is_in_installation_mode_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("IsInInstallationModeChangedTime")
        )
        self.is_in_signal_strength_test: bool = input_dict.get("IsInSignalStrengthTest")
        self.is_in_signal_strength_test_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("IsInSignalStrengthTestChangedTime")
        )
        self.panel_id: int = input_dict.get("PanelId")
        self.is_synchronized: bool = input_dict.get("IsSynchronized")
        self.sirens_entry_exit_duration: int = input_dict.get("SirensEntryExitDuration")
        self.frt_state: int = input_dict.get("FrtState")
        self.frt_state_changed_time: Optional[datetime] = time_zone.date_time_as_utc(
            input_dict.get("FrtStateChangedTime")
        )
