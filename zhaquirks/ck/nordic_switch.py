
"""Device handler for CK remote control."""
from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Alarms,
    Basic,
    Groups,
    Scenes,
    Identify,
    LevelControl,
    OnOff,
    OnOffConfiguration,
    Ota,
    PollControl,
    PowerConfiguration,
)
from zigpy.zcl.clusters.homeautomation import Diagnostic
from zigpy.zcl.clusters.lightlink import LightLink

from zhaquirks.const import (
    CLUSTER_ID,
    COMMAND,
    COMMAND_HOLD,
    COMMAND_MOVE,
    COMMAND_MOVE_ON_OFF,
    COMMAND_PRESS,
    COMMAND_RELEASE,
    COMMAND_STEP,
    COMMAND_STEP_ON_OFF,
    COMMAND_TOGGLE,
    DEVICE_TYPE,
    DIM_DOWN,
    DIM_UP,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    LEFT,
    LONG_PRESS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PARAMS,
    PROFILE_ID,
    RIGHT,
    SHORT_PRESS,
    TURN_ON,
    BUTTON,
    BUTTON_1,
    BUTTON_2,
    BUTTON_3,
    BUTTON_4,
    BUTTON_5,
    BUTTON_6,
)
# from zhaquirks.ikea import (
#     IKEA,
#     LightLinkCluster,
#     PowerConfiguration1CRCluster,
#     ScenesCluster,
# )

# IKEA_CLUSTER_ID = 0xFC7C  # decimal = 64636 TODO figure out what this should be, might be in signature

NORDIC = "Nordic"

class CKButton(CustomDevice):
    """Custom device representing IKEA of Sweden TRADFRI remote control."""

    signature = {
        # <SimpleDescriptor endpoint=1 profile=260 device_type=2080
        # device_version=1
        # input_clusters=[0, 1, 3, 32, 4096, 64636]
        # output_clusters=[3, 4, 6, 8, 25, 4096]>
        MODELS_INFO: [(NORDIC, "Dimable_Light_v0.1")], # TODO: get actual name from code, also replace the IKEA string
        ENDPOINTS: {
            10: {
                 PROFILE_ID: zha.PROFILE_ID,
                 DEVICE_TYPE: zha.DeviceType.DIMMABLE_LIGHT, # TODO: wrong name, guessed. Check ZHA package on github maybe
                 INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                ],
                OUTPUT_CLUSTERS: []
            },
            12: {
                 PROFILE_ID: zha.PROFILE_ID,
                 DEVICE_TYPE: zha.DeviceType.ON_OFF_SWITCH, # TODO: wrong name, guessed
                 INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOffConfiguration.cluster_id,
                 ],
                 OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                 ]
            },
            13: {
                 PROFILE_ID: zha.PROFILE_ID,
                 DEVICE_TYPE: zha.DeviceType.ON_OFF_SWITCH, # TODO: wrong name, guessed
                 INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOffConfiguration.cluster_id,
                 ],
                 OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                 ]
            }
        },
    }

    replacement = {
        ENDPOINTS: { 
            10: {
                 PROFILE_ID: zha.PROFILE_ID,
                 DEVICE_TYPE: zha.DeviceType.DIMMABLE_LIGHT, 
                 INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                ],
                OUTPUT_CLUSTERS: []
            },
            12: {
                 PROFILE_ID: zha.PROFILE_ID,
                 DEVICE_TYPE: zha.DeviceType.ON_OFF_SWITCH, 
                 INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOffConfiguration.cluster_id,
                 ],
                 OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                 ]
            },
            13: {
                 PROFILE_ID: zha.PROFILE_ID,
                 DEVICE_TYPE: zha.DeviceType.ON_OFF_SWITCH, 
                 INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOffConfiguration.cluster_id,
                 ],
                 OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                 ]
            }
        }
    }

    device_automation_triggers = { # TODO: Replace these
        (SHORT_PRESS, BUTTON): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 12,
        },
        (SHORT_PRESS, BUTTON_1): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 13,
        },
    }
