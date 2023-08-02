import logging
from enum import Enum
from dataclasses import dataclass
from typing import Any, List, Optional, TypeVar, Callable, Type, cast

_LOGGER = logging.getLogger(__name__)

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


class AccessModuleType(Enum):
    LOCAL_TRANSMITTER = "localTransmitter"
    MULTI_TRANSMITTER = "multiTransmitter"
    LOCAL_ZONE = "localZone"
    LOCAL_RELAY = "localRelay"
    LOCAL_SIREN = "localSiren"
    KEYPAD = "keypad"
    # Undocumented type
    INPUT_MAIN_ZONE = "inputMainZone"
    TRANSMITTER = "transmitter"


class DetectorType(Enum):
    ACTIVE_IR_DETECTOR = "activeInfraredDetector"
    CONTROL_SWITCH = "controlSwitch"
    DISPLACEMENT_DETECTOR = "displacementDetector"
    DOOR_CONTACT = "singleInfraredDetector"
    DOOR_MAGNETIC_CONTACT_DETECTOR = "magneticContact"
    DUAL_TECHNOLOGY_MOTION_DETECTOR = "dualTechnologyPirDetector"
    DYNAMIC_SWITCH = "dynamicSwitch"
    GAS_DETECTOR = "combustibleGasDetector"
    GLASS_BREAK_DETECTOR = "glassBreakDetector"
    HUMIDITY_DETECTOR = "humidityDetector"
    INDOOR_DUAL_TECHNOLOGY_DETECTOR = "indoorDualTechnologyDetector"
    IR_CURTAIN_DETECTOR = "curtainInfraredDetector"
    MAGNET_SHOCK_DETECTOR = "magnetShockDetector"
    PANIC_BUTTON = "panicButton"
    PIRCAM_DETECTOR = "pircam"
    PIR_DETECTOR = "passiveInfraredDetector"
    SHOCK_DETECTOR = "vibrationDetector"
    SLIM_MAGNETIC_CONTACT = "slimMagneticContact"
    SMART_LOCK = "smartLock"
    SMOKE_DETECTOR = "smokeDetector"
    TEMPERATURE_DETECTOR = "temperatureDetector"
    TRIPLE_TECHNOLOGY_DETECTOR = "tripleTechnologyPirDetector"
    WATER_DETECTOR = "waterDetector"
    WATER_LEAK_DETECTOR = "waterLeakDetector"
    WIRELESS_CODETECTOR = "wirelessCODetector"
    WIRELESS_DTAMCURTAIN_DETECTOR = "wirelessDTAMCurtainDetector"
    WIRELESS_EXTERNAL_MAGNET_DETECTOR = "wirelessExternalMagnetDetector"
    WIRELESS_GLASS_BREAK_DETECTOR = "wirelessGlassBreakDetector"
    WIRELESS_HEAT_DETECTOR = "wirelessHeatDetector"
    WIRELESS_PIRCEILING_DETECTOR = "wirelessPIRCeilingDetector"
    WIRELESS_PIRCURTAIN_DETECTOR = "wirelessPIRCurtainDetector"
    WIRELESS_SINGLE_INPUT_EXPANDER = "singleZoneModule"
    WIRELESS_SMOKE_DETECTOR = "wirelessSmokeDetector"
    WIRELESS_TEMPERATURE_HUMIDITY_DETECTOR = "wirelessTemperatureHumidityDetector"
    WIRELESS_TRI_TECH_DETECTOR = "wirelesTriTechDetector"
    OTHER = "other"


def detector_model_to_name(model_id: Optional[str]) -> str:
    if model_id == "0x00001":
        return "Passive Infrared Detector"
    if model_id == "0x00002":
        return "Wireless Dual-Tech Detector"
    if model_id == "0x00005":
        return "Slim Magnetic Contact"
    if model_id == "0x00006":
        return "Magnetic Contact"
    if model_id == "0x00012":
        return "Wireless PIR CAM Detector"
    if model_id == "0x00015":
        return "Wireless Smoke Detector"
    if model_id == "0x00017":
        return "Wireless Magnet Shock Detector"
    if model_id == "0x00018":
        return "Glass Break Detector"
    if model_id == "0x00026":
        return "Wireless Temperature Humidity Detector"
    if model_id == "0x00028":
        return "Wireless External Magnet Detector"
    if model_id == "0x00031":
        return "Wireless CO Detector"
    if model_id == "0x00032":
        return "Wireless PIR AM Curtain Detector"
    if model_id is not None:
        return str(model_id)
    return "Unknown"


@dataclass
class InputList:
    id: int
    enabled: bool
    mode: str

    @staticmethod
    def from_dict(obj: Any) -> 'InputList':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        enabled = from_bool(obj.get("enabled"))
        mode = from_str(obj.get("mode"))
        return InputList(id, enabled, mode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["enabled"] = from_bool(self.enabled)
        result["mode"] = from_str(self.mode)
        return result


class Status(Enum):
    ONLINE = "online"
    TRIGGER = "trigger"
    OFFLINE = "offline"
    BREAK_DOWN = "breakDown"
    HEART_BEAT_ABNORMAL = "heartbeatAbnormal"
    NOT_RELATED = "notRelated"


class ZoneAttrib(Enum):
    WIRED = "wired"
    WIRELESS = "wireless"


class ZoneType(Enum):
    """ delay zone """
    DELAY = "Delay"
    """ panic zone """
    EMERGENCY = "Emergency"
    """ fire zone """
    FIRE = "Fire"
    """ follow zone """
    FOLLOW = "Follow"
    """ gas zone """
    GAS = "Gas"
    """ key """
    KEY = "Key"
    """ medical zone """
    MEDICAL = "Medical"
    """ disabled zone """
    NON_ALARM = "Non-Alarm"
    """ 24 - hour silent zone """
    NO_SOUND_24 = "24hNoSound"
    """ perimeter zone """
    PERIMETER = "Perimeter"
    """ timeout zone """
    TIMEOUT = "Timeout"
    """ instant zone """
    INSTANT = "Instant"


@dataclass
class Zone:
    id: int
    name: str
    status: Optional[Status]
    tamper_evident: Optional[bool]
    shielded: Optional[bool]
    bypassed: Optional[bool]
    armed: bool
    is_arming: Optional[bool]
    alarm: Optional[bool]
    sub_system_no: Optional[int]
    linkage_sub_system: Optional[list[int]]
    detector_type: Optional[DetectorType]
    stay_away: Optional[bool]
    zone_type: Optional[ZoneType]
    zone_attrib: Optional[ZoneAttrib]
    device_no: Optional[int]
    abnormal_or_not: Optional[bool] = None
    charge: Optional[str] = None
    charge_value: Optional[int] = None
    signal: Optional[int] = None
    temperature: Optional[int] = None
    humidity: Optional[int] = None
    model: Optional[str] = None
    is_via_repeater: Optional[bool] = None
    version: Optional[str] = None
    magnet_open_status: Optional[bool] = None
    input_list: Optional[list[InputList]] = None
    is_support_add_type: Optional[bool] = None
    access_module_type: Optional[AccessModuleType] = None
    module_channel: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Zone':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        if obj.get("name") is None:
            name = f"Zone ID {id}"
        else:
            name = from_str(obj.get("name"))
        tamper_evident = from_union([from_bool, from_none], obj.get("tamperEvident"))
        shielded = from_union([from_bool, from_none], obj.get("shielded"))
        bypassed = from_union([from_bool, from_none], obj.get("bypassed"))
        armed = from_bool(obj.get("armed"))
        is_arming = from_union([from_bool, from_none], obj.get("isArming"))
        alarm = from_union([from_bool, from_none], obj.get("alarm"))
        sub_system_no = from_union([from_int, from_none], obj.get("subSystemNo"))

        try:
            linkage_sub_system = from_union([lambda x: from_list(from_int, x), from_none], obj.get("linkageSubSystem"))
        except:
            _LOGGER.warning("Invalid zone linkage_sub_system %s", obj.get("linkage_sub_system"))
            _LOGGER.warning("Zone info: %s", obj)
            linkage_sub_system = None

        stay_away = from_union([from_bool, from_none], obj.get("stayAway"))
        device_no = from_union([from_int, from_none], obj.get("deviceNo"))
        abnormal_or_not = from_union([from_bool, from_none], obj.get("abnormalOrNot"))
        charge = from_union([from_str, from_none], obj.get("charge"))
        charge_value = from_union([from_int, from_none], obj.get("chargeValue"))
        signal = from_union([from_int, from_none], obj.get("signal"))
        temperature = from_union([from_int, from_none], obj.get("temperature"))
        humidity = from_union([from_int, from_none], obj.get("humidity"))
        model = from_union([from_str, from_none], obj.get("model"))
        is_via_repeater = from_union([from_bool, from_none], obj.get("isViaRepeater"))
        version = from_union([from_str, from_none], obj.get("version"))
        magnet_open_status = from_union([from_bool, from_none], obj.get("magnetOpenStatus"))
        input_list = from_union([lambda x: from_list(InputList.from_dict, x), from_none], obj.get("InputList"))
        is_support_add_type = from_union([from_bool, from_none], obj.get("isSupportAddType"))
        module_channel = from_union([from_int, from_none], obj.get("moduleChannel"))

        try:
            status = Status(obj.get("status"))
        except:
            _LOGGER.warning("Invalid status %s", obj.get("status"))
            _LOGGER.warning("Detector info: %s", obj)
            status = None
        try:
            detector_type = from_union([DetectorType, from_none], obj.get("detectorType"))
        except:
            _LOGGER.warning("Invalid detector type %s", obj.get("detectorType"))
            _LOGGER.warning("Detector info: %s", obj)
            detector_type = None
        try:
            zone_type = from_union([ZoneType, from_none], obj.get("zoneType"))
        except:
            _LOGGER.warning("Invalid zone type %s", obj.get("zoneType"))
            _LOGGER.warning("Detector info: %s", obj)
            zone_type = None
        try:
            zone_attrib = from_union([ZoneAttrib, from_none], obj.get("zoneAttrib"))
        except:
            _LOGGER.warning("Invalid zone attrib %s", obj.get("zoneAttrib"))
            _LOGGER.warning("Detector info: %s", obj)
            zone_attrib = None
        try:
            access_module_type = from_union([AccessModuleType, from_none], obj.get("accessModuleType"))
        except:
            _LOGGER.warning("Invalid accessModuleType %s", obj.get("accessModuleType"))
            _LOGGER.warning("Detector info: %s", obj)
            access_module_type = None
        return Zone(id, name, status, tamper_evident, shielded, bypassed, armed, is_arming, alarm, sub_system_no,
                    linkage_sub_system, detector_type, stay_away, zone_type, zone_attrib, device_no, abnormal_or_not,
                    charge, charge_value, signal, temperature, humidity, model, is_via_repeater, version,
                    magnet_open_status, input_list, is_support_add_type, access_module_type, module_channel)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["status"] = to_enum(Status, self.status)
        result["tamperEvident"] = from_bool(self.tamper_evident)
        result["shielded"] = from_bool(self.shielded)
        result["bypassed"] = from_bool(self.bypassed)
        result["armed"] = from_bool(self.armed)
        result["isArming"] = from_bool(self.is_arming)
        result["alarm"] = from_bool(self.alarm)
        result["subSystemNo"] = from_int(self.sub_system_no)
        result["linkageSubSystem"] = from_list(from_int, self.linkage_sub_system)
        result["detectorType"] = to_enum(DetectorType, self.detector_type)
        result["stayAway"] = from_bool(self.stay_away)
        if self.zone_type is not None:
            result["zoneType"] = to_enum(ZoneType, self.zone_type)
        result["zoneAttrib"] = to_enum(ZoneAttrib, self.zone_attrib)
        result["deviceNo"] = from_int(self.device_no)
        result["abnormalOrNot"] = from_union([from_bool, from_none], self.abnormal_or_not)
        result["charge"] = from_union([from_str, from_none], self.charge)
        result["chargeValue"] = from_union([from_int, from_none], self.charge_value)
        result["signal"] = from_union([from_int, from_none], self.signal)
        result["temperature"] = from_union([from_int, from_none], self.temperature)
        result["humidity"] = from_union([from_int, from_none], self.humidity)
        result["model"] = from_union([from_str, from_none], self.model)
        result["isViaRepeater"] = from_union([from_bool, from_none], self.is_via_repeater)
        result["version"] = from_union([from_str, from_none], self.version)
        result["magnetOpenStatus"] = from_union([from_bool, from_none], self.magnet_open_status)
        result["InputList"] = from_union([lambda x: from_list(lambda x: to_class(InputList, x), x), from_none],
                                         self.input_list)
        result["isSupportAddType"] = from_union([from_bool, from_none], self.is_support_add_type)
        result["accessModuleType"] = from_union([lambda x: to_enum(AccessModuleType, x), from_none],
                                                self.access_module_type)
        result["moduleChannel"] = from_union([from_int, from_none], self.module_channel)
        return result


@dataclass
class ZoneList:
    zone: Zone

    @staticmethod
    def from_dict(obj: Any) -> 'ZoneList':
        assert isinstance(obj, dict)
        zone = Zone.from_dict(obj.get("Zone"))
        return ZoneList(zone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Zone"] = to_class(Zone, self.zone)
        return result


@dataclass
class ZonesResponse:
    zone_list: List[ZoneList]

    @staticmethod
    def from_dict(obj: Any) -> 'ZonesResponse':
        assert isinstance(obj, dict)
        zone_list = from_list(ZoneList.from_dict, obj.get("ZoneList"))
        return ZonesResponse(zone_list)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ZoneList"] = from_list(lambda x: to_class(ZoneList, x), self.zone_list)
        return result


class Arming(Enum):
    AWAY = "away"
    STAY = "stay"
    VACATION = "vacation"
    DISARM = "disarm"
    ARMING = "arming"


@dataclass
class SubSys:
    id: int
    arming: Arming
    alarm: bool
    enabled: bool
    name: str
    delay_time: int

    @staticmethod
    def from_dict(obj: Any) -> 'SubSys':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        try:
            arming = Arming(obj.get("arming"))
        except:
            _LOGGER.warning("Invalid subsys attr arming %s", obj.get("arming"))
            _LOGGER.warning("Subsys: %s", obj)
            arming = None
        alarm = from_bool(obj.get("alarm"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        if enabled is None:
            enabled = True
        name = from_union([from_str, from_none], obj.get("name"))
        delay_time = from_union([from_int, from_none], obj.get("delayTime"))
        return SubSys(id, arming, alarm, enabled, name, delay_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["arming"] = to_enum(Arming, self.arming)
        result["alarm"] = from_bool(self.alarm)
        result["enabled"] = from_bool(self.enabled)
        result["name"] = from_str(self.name)
        result["delayTime"] = from_int(self.delay_time)
        return result


@dataclass
class SubSysList:
    sub_sys: SubSys

    @staticmethod
    def from_dict(obj: Any) -> 'SubSysList':
        assert isinstance(obj, dict)
        sub_sys = SubSys.from_dict(obj.get("SubSys"))
        return SubSysList(sub_sys)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SubSys"] = to_class(SubSys, self.sub_sys)
        return result


@dataclass
class SubSystemResponse:
    sub_sys_list: List[SubSysList]

    @staticmethod
    def from_dict(obj: Any) -> 'SubSystemResponse':
        assert isinstance(obj, dict)
        sub_sys_list = from_list(SubSysList.from_dict, obj.get("SubSysList"))
        return SubSystemResponse(sub_sys_list)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SubSysList"] = from_list(lambda x: to_class(SubSysList, x), self.sub_sys_list)
        return result


class AMMode(Enum):
    ARM = "arm"


class ArmModeConf(Enum):
    AND = "and"
    OR = "or"


class ArmMode(Enum):
    WIRELESS = "wireless"
    WIRED = "wired"


class ChimeWarningType(Enum):
    SINGLE = "single"
    CONTINUOUS = "continuous"


@dataclass
class CrossZoneCFG:
    is_associated: bool
    support_associated_zone: List[int]
    already_associated_zone: List[Any]
    support_linkage_channel_id: List[Any]
    already_linkage_channel_id: List[Any]
    associate_time: int

    @staticmethod
    def from_dict(obj: Any) -> 'CrossZoneCFG':
        assert isinstance(obj, dict)
        is_associated = from_bool(obj.get("isAssociated"))
        support_associated_zone = from_list(from_int, obj.get("supportAssociatedZone"))
        already_associated_zone = from_list(lambda x: x, obj.get("alreadyAssociatedZone"))
        support_linkage_channel_id = from_list(lambda x: x, obj.get("supportLinkageChannelID"))
        already_linkage_channel_id = from_list(lambda x: x, obj.get("alreadyLinkageChannelID"))
        associate_time = from_int(obj.get("associateTime"))
        return CrossZoneCFG(is_associated, support_associated_zone, already_associated_zone, support_linkage_channel_id,
                            already_linkage_channel_id, associate_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["isAssociated"] = from_bool(self.is_associated)
        result["supportAssociatedZone"] = from_list(from_int, self.support_associated_zone)
        result["alreadyAssociatedZone"] = from_list(lambda x: x, self.already_associated_zone)
        result["supportLinkageChannelID"] = from_list(lambda x: x, self.support_linkage_channel_id)
        result["alreadyLinkageChannelID"] = from_list(lambda x: x, self.already_linkage_channel_id)
        result["associateTime"] = from_int(self.associate_time)
        return result


class DetectorAccessMode(Enum):
    NO = "NO"
    NC = "NC"


class DetectorWiringMode(Enum):
    SEOL = "SEOL"


class NewKeyZoneTriggerTypeCFG(Enum):
    ZONE_STATUS = "zoneStatus"


class Relator(Enum):
    APP = "app"
    HOST = "host"


@dataclass
class RelatedChan:
    camera_seq: str
    related_chan: int
    linkage_camera_name: Optional[str] = None
    relator: Optional[Relator] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelatedChan':
        assert isinstance(obj, dict)
        camera_seq = from_str(obj.get("cameraSeq"))
        related_chan = from_int(obj.get("relatedChan"))
        linkage_camera_name = from_union([from_str, from_none], obj.get("linkageCameraName"))
        try:
            relator = from_union([Relator, from_none], obj.get("relator"))
        except:
            _LOGGER.warning("Invalid relator type %s", obj.get("relator"))
            _LOGGER.warning("relator info: %s", obj)
            relator = None
        return RelatedChan(camera_seq, related_chan, linkage_camera_name, relator)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cameraSeq"] = from_str(self.camera_seq)
        result["relatedChan"] = from_int(self.related_chan)
        if self.linkage_camera_name is not None:
            result["linkageCameraName"] = from_union([from_str, from_none], self.linkage_camera_name)
        if self.relator is not None:
            result["relator"] = from_union([lambda x: to_enum(Relator, x), from_none], self.relator)
        return result


@dataclass
class RelatedChanList:
    related_chan: RelatedChan

    @staticmethod
    def from_dict(obj: Any) -> 'RelatedChanList':
        assert isinstance(obj, dict)
        related_chan = RelatedChan.from_dict(obj.get("RelatedChan"))
        return RelatedChanList(related_chan)

    def to_dict(self) -> dict:
        result: dict = {}
        result["RelatedChan"] = to_class(RelatedChan, self.related_chan)
        return result


@dataclass
class RelatedPIRCAM:
    support_linkage_zones: List[Any]
    linkage_zone: List[Any]
    linkage_pircam_name: str

    @staticmethod
    def from_dict(obj: Any) -> 'RelatedPIRCAM':
        assert isinstance(obj, dict)
        support_linkage_zones = from_list(lambda x: x, obj.get("supportLinkageZones"))
        linkage_zone = from_list(lambda x: x, obj.get("linkageZone"))
        linkage_pircam_name = from_str(obj.get("linkagePIRCAMName"))
        return RelatedPIRCAM(support_linkage_zones, linkage_zone, linkage_pircam_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["supportLinkageZones"] = from_list(lambda x: x, self.support_linkage_zones)
        result["linkageZone"] = from_list(lambda x: x, self.linkage_zone)
        result["linkagePIRCAMName"] = from_str(self.linkage_pircam_name)
        return result


class TimeoutType(Enum):
    RECOVER = "recover"
    TIGGER = "tigger"


class ZoneStatusCFG(Enum):
    TRIGGER_ARM = "triggerArm"


@dataclass
class ZoneConfig:
    id: int
    zone_name: str
    detector_type: DetectorType
    stay_away_enabled: bool
    chime_enabled: bool
    silent_enabled: bool
    timeout_type: TimeoutType
    timeout: int
    related_chan_list: List[RelatedChanList]
    new_key_zone_trigger_type_cfg: NewKeyZoneTriggerTypeCFG
    zone_status_cfg: ZoneStatusCFG
    double_knock_enabled: Optional[bool] = None
    double_knock_time: Optional[int] = None
    zone_type: Optional[ZoneType] = None
    chime_warning_type: Optional[ChimeWarningType] = None
    relate_detector: Optional[bool] = None
    sub_system_no: Optional[int] = None
    linkage_sub_system: Optional[List[int]] = None
    support_linkage_sub_system_list: Optional[List[int]] = None
    enter_delay: Optional[int] = None
    exit_delay: Optional[int] = None
    stay_arm_delay_time: Optional[int] = None
    siren_delay_time: Optional[int] = None
    detector_seq: Optional[str] = None
    cross_zone_cfg: Optional[CrossZoneCFG] = None
    arm_no_bypass_enabled: Optional[bool] = None
    related_pircam: Optional[RelatedPIRCAM] = None
    arm_mode: Optional[ArmModeConf] = None
    zone_attrib: Optional[ZoneAttrib] = None
    final_door_exit_enabled: Optional[bool] = None
    time_restart_enabled: Optional[bool] = None
    swinger_limit_activation: Optional[int] = None
    detector_wiring_mode: Optional[DetectorWiringMode] = None
    detector_access_mode: Optional[DetectorAccessMode] = None
    anti_masking_enabled: Optional[bool] = None
    am_mode: Optional[AMMode] = None
    am_delay_time: Optional[int] = None
    pulse_sensitivity: Optional[int] = None
    alarm_resistence: Optional[float] = None
    tamper_resistence: Optional[float] = None
    module_channel: Optional[int] = None
    double_zone_cfg_enable: Optional[bool] = None
    access_module_type: Optional[AccessModuleType] = None
    delay_time: Optional[int] = None
    timeout_limit: Optional[bool] = None
    check_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ZoneConfig':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        zone_name = from_str(obj.get("zoneName"))
        detector_type = DetectorType(obj.get("detectorType"))
        try:
            zone_type = from_union([ZoneType, from_none], obj.get("zoneType"))
        except:
            _LOGGER.warning("Invalid zone type %s", obj.get("zoneType"))
            _LOGGER.warning("Detector info: %s", obj)
            zone_type = None
        stay_away_enabled = from_bool(obj.get("stayAwayEnabled"))
        chime_enabled = from_bool(obj.get("chimeEnabled"))
        silent_enabled = from_bool(obj.get("silentEnabled"))
        chime_warning_type = from_union([ChimeWarningType, from_none], obj.get("chimeWarningType"))
        timeout_type = TimeoutType(obj.get("timeoutType"))
        timeout = from_int(obj.get("timeout"))
        relate_detector = from_union([from_bool, from_none], obj.get("relateDetector"))
        related_chan_list = from_list(RelatedChanList.from_dict, obj.get("RelatedChanList"))
        double_knock_enabled = from_union([from_bool, from_none], obj.get("doubleKnockEnabled"))
        double_knock_time = from_union([from_int, from_none], obj.get("doubleKnockTime"))
        new_key_zone_trigger_type_cfg = NewKeyZoneTriggerTypeCFG(obj.get("newKeyZoneTriggerTypeCfg"))
        zone_status_cfg = ZoneStatusCFG(obj.get("zoneStatusCfg"))
        sub_system_no = from_union([from_int, from_none], obj.get("subSystemNo"))
        linkage_sub_system = from_union([lambda x: from_list(from_int, x), from_none], obj.get("linkageSubSystem"))
        support_linkage_sub_system_list = from_union([lambda x: from_list(from_int, x), from_none],
                                                     obj.get("supportLinkageSubSystemList"))
        enter_delay = from_union([from_int, from_none], obj.get("enterDelay"))
        exit_delay = from_union([from_int, from_none], obj.get("exitDelay"))
        stay_arm_delay_time = from_union([from_int, from_none], obj.get("stayArmDelayTime"))
        siren_delay_time = from_union([from_int, from_none], obj.get("sirenDelayTime"))
        detector_seq = from_union([from_str, from_none], obj.get("detectorSeq"))
        cross_zone_cfg = from_union([CrossZoneCFG.from_dict, from_none], obj.get("CrossZoneCfg"))
        arm_no_bypass_enabled = from_union([from_bool, from_none], obj.get("armNoBypassEnabled"))
        related_pircam = from_union([RelatedPIRCAM.from_dict, from_none], obj.get("RelatedPIRCAM"))
        arm_mode = from_union([ArmModeConf, from_none], obj.get("armMode"))
        zone_attrib = from_union([ZoneAttrib, from_none], obj.get("zoneAttrib"))
        final_door_exit_enabled = from_union([from_bool, from_none], obj.get("finalDoorExitEnabled"))
        time_restart_enabled = from_union([from_bool, from_none], obj.get("timeRestartEnabled"))
        swinger_limit_activation = from_union([from_int, from_none], obj.get("swingerLimitActivation"))
        try:
            detector_wiring_mode = from_union([DetectorWiringMode, from_none], obj.get("detectorWiringMode"))
        except:
            _LOGGER.warning("Invalid detector_wiring_mode %s", obj.get("detectorWiringMode"))
            _LOGGER.warning("Detector info: %s", obj)
            detector_wiring_mode = None
        try:
            detector_access_mode = from_union([DetectorAccessMode, from_none], obj.get("detectorAccessMode"))
        except:
            _LOGGER.warning("Invalid detector_access_mode %s", obj.get("detectorAccessMode"))
            _LOGGER.warning("Detector info: %s", obj)
            detector_access_mode = None
        anti_masking_enabled = from_union([from_bool, from_none], obj.get("antiMaskingEnabled"))
        am_mode = from_union([AMMode, from_none], obj.get("AMMode"))
        am_delay_time = from_union([from_int, from_none], obj.get("AMDelayTime"))
        pulse_sensitivity = from_union([from_int, from_none], obj.get("pulseSensitivity"))
        alarm_resistence = from_union([from_float, from_none], obj.get("alarmResistence"))
        tamper_resistence = from_union([from_float, from_none], obj.get("tamperResistence"))
        module_channel = from_union([from_int, from_none], obj.get("moduleChannel"))
        double_zone_cfg_enable = from_union([from_bool, from_none], obj.get("doubleZoneCfgEnable"))
        try:
            access_module_type = from_union([AccessModuleType, from_none], obj.get("accessModuleType"))
        except:
            _LOGGER.warning("Invalid accessModuleType %s", obj.get("accessModuleType"))
            _LOGGER.warning("Zone config: %s", obj)
            access_module_type = None
        delay_time = from_union([from_int, from_none], obj.get("delayTime"))
        timeout_limit = from_union([from_bool, from_none], obj.get("timeoutLimit"))
        check_time = from_union([from_int, from_none], obj.get("checkTime"))
        return ZoneConfig(
            id,
            zone_name,
            detector_type,
            stay_away_enabled,
            chime_enabled,
            silent_enabled,
            timeout_type,
            timeout,
            related_chan_list,
            new_key_zone_trigger_type_cfg,
            zone_status_cfg,
            double_knock_enabled,
            double_knock_time,
            zone_type,
            chime_warning_type,
            relate_detector,
            sub_system_no,
            linkage_sub_system,
            support_linkage_sub_system_list,
            enter_delay,
            exit_delay,
            stay_arm_delay_time,
            siren_delay_time,
            detector_seq,
            cross_zone_cfg,
            arm_no_bypass_enabled,
            related_pircam,
            arm_mode,
            zone_attrib,
            final_door_exit_enabled,
            time_restart_enabled,
            swinger_limit_activation,
            detector_wiring_mode,
            detector_access_mode,
            anti_masking_enabled,
            am_mode,
            am_delay_time,
            pulse_sensitivity,
            alarm_resistence,
            tamper_resistence,
            module_channel,
            double_zone_cfg_enable,
            access_module_type,
            delay_time,
            timeout_limit,
            check_time,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["zoneName"] = from_str(self.zone_name)
        result["detectorType"] = to_enum(DetectorType, self.detector_type)
        if self.zone_type is not None:
            result["zoneType"] = to_enum(ZoneType, self.zone_type)
        result["stayAwayEnabled"] = from_bool(self.stay_away_enabled)
        result["chimeEnabled"] = from_bool(self.chime_enabled)
        result["silentEnabled"] = from_bool(self.silent_enabled)
        if self.chime_warning_type is not None:
            result["chimeWarningType"] = to_enum(ChimeWarningType, self.chime_warning_type)
        result["timeoutType"] = to_enum(TimeoutType, self.timeout_type)
        result["timeout"] = from_int(self.timeout)
        if self.relate_detector is not None:
            result["relateDetector"] = from_bool(self.relate_detector)
        result["RelatedChanList"] = from_list(lambda x: to_class(RelatedChanList, x), self.related_chan_list)
        if self.double_knock_enabled is not None:
            result["doubleKnockEnabled"] = from_bool(self.double_knock_enabled)
        if self.double_knock_time is not None:
            result["doubleKnockTime"] = from_int(self.double_knock_time)
        result["newKeyZoneTriggerTypeCfg"] = to_enum(NewKeyZoneTriggerTypeCFG, self.new_key_zone_trigger_type_cfg)
        result["zoneStatusCfg"] = to_enum(ZoneStatusCFG, self.zone_status_cfg)
        if self.sub_system_no is not None:
            result["subSystemNo"] = from_union([from_int, from_none], self.sub_system_no)
        if self.linkage_sub_system is not None:
            result["linkageSubSystem"] = from_union([lambda x: from_list(from_int, x), from_none],
                                                    self.linkage_sub_system)
        if self.support_linkage_sub_system_list is not None:
            result["supportLinkageSubSystemList"] = from_union([lambda x: from_list(from_int, x), from_none],
                                                               self.support_linkage_sub_system_list)
        if self.enter_delay is not None:
            result["enterDelay"] = from_union([from_int, from_none], self.enter_delay)
        if self.exit_delay is not None:
            result["exitDelay"] = from_union([from_int, from_none], self.exit_delay)
        if self.stay_arm_delay_time is not None:
            result["stayArmDelayTime"] = from_union([from_int, from_none], self.stay_arm_delay_time)
        if self.siren_delay_time is not None:
            result["sirenDelayTime"] = from_union([from_int, from_none], self.siren_delay_time)
        if self.detector_seq is not None:
            result["detectorSeq"] = from_union([from_str, from_none], self.detector_seq)
        if self.cross_zone_cfg is not None:
            result["CrossZoneCfg"] = from_union([lambda x: to_class(CrossZoneCFG, x), from_none], self.cross_zone_cfg)
        if self.arm_no_bypass_enabled is not None:
            result["armNoBypassEnabled"] = from_union([from_bool, from_none], self.arm_no_bypass_enabled)
        if self.related_pircam is not None:
            result["RelatedPIRCAM"] = from_union([lambda x: to_class(RelatedPIRCAM, x), from_none], self.related_pircam)
        if self.arm_mode is not None:
            result["armMode"] = from_union([lambda x: to_enum(ArmModeConf, x), from_none], self.arm_mode)
        if self.zone_attrib is not None:
            result["zoneAttrib"] = from_union([lambda x: to_enum(ZoneAttrib, x), from_none], self.zone_attrib)
        if self.final_door_exit_enabled is not None:
            result["finalDoorExitEnabled"] = from_union([from_bool, from_none], self.final_door_exit_enabled)
        if self.time_restart_enabled is not None:
            result["timeRestartEnabled"] = from_union([from_bool, from_none], self.time_restart_enabled)
        if self.swinger_limit_activation is not None:
            result["swingerLimitActivation"] = from_union([from_int, from_none], self.swinger_limit_activation)
        if self.detector_wiring_mode is not None:
            result["detectorWiringMode"] = from_union([lambda x: to_enum(DetectorWiringMode, x), from_none],
                                                      self.detector_wiring_mode)
        if self.detector_access_mode is not None:
            result["detectorAccessMode"] = from_union([lambda x: to_enum(DetectorAccessMode, x), from_none],
                                                      self.detector_access_mode)
        if self.anti_masking_enabled is not None:
            result["antiMaskingEnabled"] = from_union([from_bool, from_none], self.anti_masking_enabled)
        if self.am_mode is not None:
            result["AMMode"] = from_union([lambda x: to_enum(AMMode, x), from_none], self.am_mode)
        if self.am_delay_time is not None:
            result["AMDelayTime"] = from_union([from_int, from_none], self.am_delay_time)
        if self.pulse_sensitivity is not None:
            result["pulseSensitivity"] = from_union([from_int, from_none], self.pulse_sensitivity)
        if self.alarm_resistence is not None:
            result["alarmResistence"] = from_union([to_float, from_none], self.alarm_resistence)
        if self.tamper_resistence is not None:
            result["tamperResistence"] = from_union([to_float, from_none], self.tamper_resistence)
        if self.module_channel is not None:
            result["moduleChannel"] = from_union([from_int, from_none], self.module_channel)
        if self.double_zone_cfg_enable is not None:
            result["doubleZoneCfgEnable"] = from_union([from_bool, from_none], self.double_zone_cfg_enable)
        if self.access_module_type is not None:
            result["accessModuleType"] = from_union([lambda x: to_enum(AccessModuleType, x), from_none],
                                                    self.access_module_type)
        if self.delay_time is not None:
            result["delayTime"] = from_union([from_int, from_none], self.delay_time)
        if self.timeout_limit is not None:
            result["timeoutLimit"] = from_union([from_bool, from_none], self.timeout_limit)
        if self.check_time is not None:
            result["checkTime"] = from_union([from_int, from_none], self.check_time)
        return result


@dataclass
class ZoneConfListWrap:
    zone: ZoneConfig

    @staticmethod
    def from_dict(obj: Any) -> 'ZoneConfListWrap':
        assert isinstance(obj, dict)
        zone = ZoneConfig.from_dict(obj.get("Zone"))
        return ZoneConfListWrap(zone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Zone"] = to_class(ZoneConfig, self.zone)
        return result


@dataclass
class ZonesConf:
    list: List[ZoneConfListWrap]

    @staticmethod
    def from_dict(obj: Any) -> 'ZonesConf':
        assert isinstance(obj, dict)
        list = from_list(ZoneConfListWrap.from_dict, obj.get("List"))
        return ZonesConf(list)

    def to_dict(self) -> dict:
        result: dict = {}
        result["List"] = from_list(lambda x: to_class(ZoneConfListWrap, x), self.list)
        return result


@dataclass
class AlarmCFG:
    alarm_type: Optional[List[Any]] = None
    support_associated_zone: Optional[List[int]] = None
    associate_zone_cfg: Optional[List[Any]] = None
    support_disarm_linkage_zone: Optional[List[Any]] = None
    disarm_linkage_zone: Optional[List[Any]] = None
    support_linkage_channel_id: Optional[List[Any]] = None
    linkage_channel_id: Optional[List[Any]] = None
    alarm_logic: Optional[str] = None
    relay_mode: Optional[str] = None
    pulse_duration: Optional[int] = None
    contact_status: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AlarmCFG':
        assert isinstance(obj, dict)
        alarm_type = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("alarmType"))
        support_associated_zone = from_union([lambda x: from_list(from_int, x), from_none], obj.get("supportAssociatedZone"))
        associate_zone_cfg = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("associateZoneCfg"))
        support_disarm_linkage_zone = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("supportDisarmLinkageZone"))
        disarm_linkage_zone = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("disarmLinkageZone"))
        support_linkage_channel_id = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("supportLinkageChannelID"))
        linkage_channel_id = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("linkageChannelID"))
        alarm_logic = from_union([from_str, from_none], obj.get("alarmLogic"))
        relay_mode = from_union([from_str, from_none], obj.get("relayMode"))
        pulse_duration = from_union([from_int, from_none], obj.get("pulseDuration"))
        contact_status = from_union([from_str, from_none], obj.get("contactStatus"))
        return AlarmCFG(alarm_type, support_associated_zone, associate_zone_cfg, support_disarm_linkage_zone, disarm_linkage_zone, support_linkage_channel_id, linkage_channel_id, alarm_logic, relay_mode, pulse_duration, contact_status)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.alarm_type is not None:
            result["alarmType"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.alarm_type)
        if self.support_associated_zone is not None:
            result["supportAssociatedZone"] = from_union([lambda x: from_list(from_int, x), from_none], self.support_associated_zone)
        if self.associate_zone_cfg is not None:
            result["associateZoneCfg"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.associate_zone_cfg)
        if self.support_disarm_linkage_zone is not None:
            result["supportDisarmLinkageZone"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.support_disarm_linkage_zone)
        if self.disarm_linkage_zone is not None:
            result["disarmLinkageZone"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.disarm_linkage_zone)
        if self.support_linkage_channel_id is not None:
            result["supportLinkageChannelID"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.support_linkage_channel_id)
        if self.linkage_channel_id is not None:
            result["linkageChannelID"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.linkage_channel_id)
        if self.alarm_logic is not None:
            result["alarmLogic"] = from_union([from_str, from_none], self.alarm_logic)
        if self.relay_mode is not None:
            result["relayMode"] = from_union([from_str, from_none], self.relay_mode)
        if self.pulse_duration is not None:
            result["pulseDuration"] = from_union([from_int, from_none], self.pulse_duration)
        if self.contact_status is not None:
            result["contactStatus"] = from_union([from_str, from_none], self.contact_status)
        return result


@dataclass
class CFG:
    arm_type: Optional[List[Any]] = None
    relay_mode: Optional[str] = None
    pulse_duration: Optional[int] = None
    contact_status: Optional[str] = None
    fault_type: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CFG':
        assert isinstance(obj, dict)
        arm_type = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("armType"))
        relay_mode = from_union([from_str, from_none], obj.get("relayMode"))
        pulse_duration = from_union([from_int, from_none], obj.get("pulseDuration"))
        contact_status = from_union([from_str, from_none], obj.get("contactStatus"))
        fault_type = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("faultType"))
        return CFG(arm_type, relay_mode, pulse_duration, contact_status, fault_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.arm_type is not None:
            result["armType"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.arm_type)
        if self.relay_mode is not None:
            result["relayMode"] = from_union([from_str, from_none], self.relay_mode)
        if self.pulse_duration is not None:
            result["pulseDuration"] = from_union([from_int, from_none], self.pulse_duration)
        if self.contact_status is not None:
            result["contactStatus"] = from_union([from_str, from_none], self.contact_status)
        if self.fault_type is not None:
            result["faultType"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.fault_type)
        return result


@dataclass
class ManualCFG:
    relay_mode: Optional[str] = None
    pulse_duration: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ManualCFG':
        assert isinstance(obj, dict)
        relay_mode = from_union([from_str, from_none], obj.get("relayMode"))
        pulse_duration = from_union([from_int, from_none], obj.get("pulseDuration"))
        return ManualCFG(relay_mode, pulse_duration)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.relay_mode is not None:
            result["relayMode"] = from_union([from_str, from_none], self.relay_mode)
        if self.pulse_duration is not None:
            result["pulseDuration"] = from_union([from_int, from_none], self.pulse_duration)
        return result


@dataclass
class TimeSegment:
    id: Optional[int] = None
    enabled: Optional[bool] = None
    contact_status: Optional[str] = None
    begin_time: Optional[str] = None
    end_time: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TimeSegment':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        contact_status = from_union([from_str, from_none], obj.get("contactStatus"))
        begin_time = from_union([from_str, from_none], obj.get("beginTime"))
        end_time = from_union([from_str, from_none], obj.get("endTime"))
        return TimeSegment(id, enabled, contact_status, begin_time, end_time)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.enabled is not None:
            result["enabled"] = from_union([from_bool, from_none], self.enabled)
        if self.contact_status is not None:
            result["contactStatus"] = from_union([from_str, from_none], self.contact_status)
        if self.begin_time is not None:
            result["beginTime"] = from_union([from_str, from_none], self.begin_time)
        if self.end_time is not None:
            result["endTime"] = from_union([from_str, from_none], self.end_time)
        return result


@dataclass
class ScheduleCFG:
    time_segment: Optional[TimeSegment] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ScheduleCFG':
        assert isinstance(obj, dict)
        time_segment = from_union([TimeSegment.from_dict, from_none], obj.get("timeSegment"))
        return ScheduleCFG(time_segment)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.time_segment is not None:
            result["timeSegment"] = from_union([lambda x: to_class(TimeSegment, x), from_none], self.time_segment)
        return result


@dataclass
class RelaySwitchConf:
    id: Optional[int] = None
    name: Optional[str] = None
    related: Optional[bool] = None
    access_module_type: Optional[str] = None
    module_channel: Optional[int] = None
    sub_system: Optional[List[int]] = None
    scenario_type: Optional[List[str]] = None
    alarm_cfg: Optional[AlarmCFG] = None
    schedule_cfg: Optional[List[ScheduleCFG]] = None
    arm_cfg: Optional[CFG] = None
    disarm_cfg: Optional[CFG] = None
    clear_alarm_cfg: Optional[CFG] = None
    fault_cfg: Optional[CFG] = None
    manual_cfg: Optional[ManualCFG] = None
    original_status: Optional[str] = None
    support_linkage_sub_system_list: Optional[List[int]] = None
    relay_attrib: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelaySwitchConf':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        related = from_union([from_bool, from_none], obj.get("related"))
        access_module_type = from_union([from_str, from_none], obj.get("accessModuleType"))
        module_channel = from_union([from_int, from_none], obj.get("moduleChannel"))
        sub_system = from_union([lambda x: from_list(from_int, x), from_none], obj.get("subSystem"))
        scenario_type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scenarioType"))
        try:
            alarm_cfg = from_union([AlarmCFG.from_dict, from_none], obj.get("alarmCfg"))
        except:
            alarm_cfg = None
        try:
            schedule_cfg = from_union([lambda x: from_list(ScheduleCFG.from_dict, x), from_none], obj.get("scheduleCfg"))
        except:
            schedule_cfg = None
        try:
            arm_cfg = from_union([CFG.from_dict, from_none], obj.get("armCfg"))
        except:
            arm_cfg = None
        try:
            disarm_cfg = from_union([CFG.from_dict, from_none], obj.get("disarmCfg"))
        except:
            disarm_cfg = None
        try:
            clear_alarm_cfg = from_union([CFG.from_dict, from_none], obj.get("clearAlarmCfg"))
        except:
            clear_alarm_cfg = None
        try:
            fault_cfg = from_union([CFG.from_dict, from_none], obj.get("faultCfg"))
        except:
            fault_cfg = None
        try:
            manual_cfg = from_union([ManualCFG.from_dict, from_none], obj.get("manualCfg"))
        except:
            manual_cfg = None
        original_status = from_union([from_str, from_none], obj.get("OriginalStatus"))
        support_linkage_sub_system_list = from_union([lambda x: from_list(from_int, x), from_none], obj.get("supportLinkageSubSystemList"))
        relay_attrib = from_union([from_str, from_none], obj.get("relayAttrib"))
        return RelaySwitchConf(id, name, related, access_module_type, module_channel, sub_system, scenario_type, alarm_cfg, schedule_cfg, arm_cfg, disarm_cfg, clear_alarm_cfg, fault_cfg, manual_cfg, original_status, support_linkage_sub_system_list, relay_attrib)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.related is not None:
            result["related"] = from_union([from_bool, from_none], self.related)
        if self.access_module_type is not None:
            result["accessModuleType"] = from_union([from_str, from_none], self.access_module_type)
        if self.module_channel is not None:
            result["moduleChannel"] = from_union([from_int, from_none], self.module_channel)
        if self.sub_system is not None:
            result["subSystem"] = from_union([lambda x: from_list(from_int, x), from_none], self.sub_system)
        if self.scenario_type is not None:
            result["scenarioType"] = from_union([lambda x: from_list(from_str, x), from_none], self.scenario_type)
        if self.alarm_cfg is not None:
            result["alarmCfg"] = from_union([lambda x: to_class(AlarmCFG, x), from_none], self.alarm_cfg)
        if self.schedule_cfg is not None:
            result["scheduleCfg"] = from_union([lambda x: from_list(lambda x: to_class(ScheduleCFG, x), x), from_none], self.schedule_cfg)
        if self.arm_cfg is not None:
            result["armCfg"] = from_union([lambda x: to_class(CFG, x), from_none], self.arm_cfg)
        if self.disarm_cfg is not None:
            result["disarmCfg"] = from_union([lambda x: to_class(CFG, x), from_none], self.disarm_cfg)
        if self.clear_alarm_cfg is not None:
            result["clearAlarmCfg"] = from_union([lambda x: to_class(CFG, x), from_none], self.clear_alarm_cfg)
        if self.fault_cfg is not None:
            result["faultCfg"] = from_union([lambda x: to_class(CFG, x), from_none], self.fault_cfg)
        if self.manual_cfg is not None:
            result["manualCfg"] = from_union([lambda x: to_class(ManualCFG, x), from_none], self.manual_cfg)
        if self.original_status is not None:
            result["OriginalStatus"] = from_union([from_str, from_none], self.original_status)
        if self.support_linkage_sub_system_list is not None:
            result["supportLinkageSubSystemList"] = from_union([lambda x: from_list(from_int, x), from_none], self.support_linkage_sub_system_list)
        if self.relay_attrib is not None:
            result["relayAttrib"] = from_union([from_str, from_none], self.relay_attrib)
        return result


@dataclass
class OutputConfListWrap:
    output: Optional[RelaySwitchConf] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OutputConfListWrap':
        assert isinstance(obj, dict)
        output = from_union([RelaySwitchConf.from_dict, from_none], obj.get("Output"))
        return OutputConfListWrap(output)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.output is not None:
            result["Output"] = from_union([lambda x: to_class(RelaySwitchConf, x), from_none], self.output)
        return result


@dataclass
class OutputConfList:
    list: Optional[List[OutputConfListWrap]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OutputConfList':
        assert isinstance(obj, dict)
        list = from_union([lambda x: from_list(OutputConfListWrap.from_dict, x), from_none], obj.get("List"))
        return OutputConfList(list)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.list is not None:
            result["List"] = from_union([lambda x: from_list(lambda x: to_class(OutputConfListWrap, x), x), from_none], self.list)
        return result



class RelayAttrib(Enum):
    WIRED = "wired"


class RelayStatusEnum(Enum):
    NOT_RELATED = "notRelated"
    OFF = "off"
    ON = "on"


@dataclass
class RelayStatus:
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[RelayStatusEnum] = None
    access_module_type: Optional[str] = None
    module_channel: Optional[int] = None
    sub_system_list: Optional[List[int]] = None
    scenario_type: Optional[List[str]] = None
    relay_attrib: Optional[RelayAttrib] = None
    device_no: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelayStatus':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        try:
            status = from_union([RelayStatusEnum, from_none], obj.get("status"))
        except:
            status = None
        access_module_type = from_union([from_str, from_none], obj.get("accessModuleType"))
        module_channel = from_union([from_int, from_none], obj.get("moduleChannel"))
        sub_system_list = from_union([lambda x: from_list(from_int, x), from_none], obj.get("subSystemList"))
        scenario_type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scenarioType"))
        try:
            relay_attrib = from_union([RelayAttrib, from_none], obj.get("relayAttrib"))
        except:
            relay_attrib = None
        device_no = from_union([from_int, from_none], obj.get("deviceNo"))
        return RelayStatus(id, name, status, access_module_type, module_channel, sub_system_list, scenario_type, relay_attrib, device_no)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        if self.access_module_type is not None:
            result["accessModuleType"] = from_union([from_str, from_none], self.access_module_type)
        if self.module_channel is not None:
            result["moduleChannel"] = from_union([from_int, from_none], self.module_channel)
        if self.sub_system_list is not None:
            result["subSystemList"] = from_union([lambda x: from_list(from_int, x), from_none], self.sub_system_list)
        if self.scenario_type is not None:
            result["scenarioType"] = from_union([lambda x: from_list(from_str, x), from_none], self.scenario_type)
        if self.relay_attrib is not None:
            result["relayAttrib"] = from_union([lambda x: to_enum(RelayAttrib, x), from_none], self.relay_attrib)
        if self.device_no is not None:
            result["deviceNo"] = from_union([from_int, from_none], self.device_no)
        return result


@dataclass
class RelayStatusList:
    output: Optional[RelayStatus] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelayStatusList':
        assert isinstance(obj, dict)
        output = from_union([RelayStatus.from_dict, from_none], obj.get("Output"))
        return RelayStatusList(output)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.output is not None:
            result["Output"] = from_union([lambda x: to_class(RelayStatus, x), from_none], self.output)
        return result


@dataclass
class RelayStatusSearch:
    search_id: Optional[str] = None
    response_status_strg: Optional[str] = None
    num_of_matches: Optional[int] = None
    total_matches: Optional[int] = None
    output_list: Optional[List[RelayStatusList]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelayStatusSearch':
        assert isinstance(obj, dict)
        search_id = from_union([from_str, from_none], obj.get("searchID"))
        response_status_strg = from_union([from_str, from_none], obj.get("responseStatusStrg"))
        num_of_matches = from_union([from_int, from_none], obj.get("numOfMatches"))
        total_matches = from_union([from_int, from_none], obj.get("totalMatches"))
        output_list = from_union([lambda x: from_list(RelayStatusList.from_dict, x), from_none], obj.get("OutputList"))
        return RelayStatusSearch(search_id, response_status_strg, num_of_matches, total_matches, output_list)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.search_id is not None:
            result["searchID"] = from_union([from_str, from_none], self.search_id)
        if self.response_status_strg is not None:
            result["responseStatusStrg"] = from_union([from_str, from_none], self.response_status_strg)
        if self.num_of_matches is not None:
            result["numOfMatches"] = from_union([from_int, from_none], self.num_of_matches)
        if self.total_matches is not None:
            result["totalMatches"] = from_union([from_int, from_none], self.total_matches)
        if self.output_list is not None:
            result["OutputList"] = from_union([lambda x: from_list(lambda x: to_class(RelayStatusList, x), x), from_none], self.output_list)
        return result


@dataclass
class RelayStatusSearchResponse:
    output_search: Optional[RelayStatusSearch] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RelayStatusSearchResponse':
        assert isinstance(obj, dict)
        output_search = from_union([RelayStatusSearch.from_dict, from_none], obj.get("OutputSearch"))
        return RelayStatusSearchResponse(output_search)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.output_search is not None:
            result["OutputSearch"] = from_union([lambda x: to_class(RelayStatusSearch, x), from_none], self.output_search)
        return result


@dataclass
class JSONResponseStatus:
    request_url: Optional[str] = None
    status_code: Optional[int] = None
    status_string: Optional[str] = None
    sub_status_code: Optional[str] = None
    error_code: Optional[int] = None
    error_msg: Optional[str] = None
    m_err_code: Optional[str] = None
    m_err_dev_self_ex: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'JSONResponseStatus':
        assert isinstance(obj, dict)
        request_url = from_union([from_str, from_none], obj.get("requestURL"))
        status_code = from_union([from_int, from_none], obj.get("statusCode"))
        status_string = from_union([from_str, from_none], obj.get("statusString"))
        sub_status_code = from_union([from_str, from_none], obj.get("subStatusCode"))
        error_code = from_union([from_int, from_none], obj.get("errorCode"))
        error_msg = from_union([from_str, from_none], obj.get("errorMsg"))
        m_err_code = from_union([from_str, from_none], obj.get("MErrCode"))
        m_err_dev_self_ex = from_union([from_str, from_none], obj.get("MErrDevSelfEx"))
        return JSONResponseStatus(request_url, status_code, status_string, sub_status_code, error_code, error_msg, m_err_code, m_err_dev_self_ex)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.request_url is not None:
            result["requestURL"] = from_union([from_str, from_none], self.request_url)
        if self.status_code is not None:
            result["statusCode"] = from_union([from_int, from_none], self.status_code)
        if self.status_string is not None:
            result["statusString"] = from_union([from_str, from_none], self.status_string)
        if self.sub_status_code is not None:
            result["subStatusCode"] = from_union([from_str, from_none], self.sub_status_code)
        if self.error_code is not None:
            result["errorCode"] = from_union([from_int, from_none], self.error_code)
        if self.error_msg is not None:
            result["errorMsg"] = from_union([from_str, from_none], self.error_msg)
        if self.m_err_code is not None:
            result["MErrCode"] = from_union([from_str, from_none], self.m_err_code)
        if self.m_err_dev_self_ex is not None:
            result["MErrDevSelfEx"] = from_union([from_str, from_none], self.m_err_dev_self_ex)
        return result

