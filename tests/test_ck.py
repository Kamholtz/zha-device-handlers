"""Tests for CK quirks."""

import asyncio
import datetime
from unittest import mock

import pytest
from zigpy.profiles import zha
from zigpy.quirks import CustomDevice, get_device
import zigpy.types as t
from zigpy.zcl import foundation

import zhaquirks
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OFF,
    ON,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
    ZONE_STATE,
)
from zhaquirks.tuya import Data, TuyaManufClusterAttributes
import zhaquirks.tuya.ts0042

from tests.common import ClusterListener

zhaquirks.setup()

def test_ck_signature(assert_signature_matches_quirk):
    """Test Nordic Dimmable Lightbulb remote signature is matched to its quirk."""
    signature = {
      "node_descriptor": "NodeDescriptor(logical_type=<LogicalType.EndDevice: 2>, complex_descriptor_available=0, user_descriptor_available=0, reserved=0, aps_flags=0, frequency_band=<FrequencyBand.Freq2400MHz: 8>, mac_capability_flags=<MACCapabilityFlags.AllocateAddress|RxOnWhenIdle|MainsPowered: 140>, manufacturer_code=4660, maximum_buffer_size=108, maximum_incoming_transfer_size=1617, server_mask=11264, maximum_outgoing_transfer_size=1617, descriptor_capability_field=<DescriptorCapability.NONE: 0>, *allocate_address=True, *is_alternate_pan_coordinator=False, *is_coordinator=False, *is_end_device=True, *is_full_function_device=False, *is_mains_powered=True, *is_receiver_on_when_idle=True, *is_router=False, *is_security_capable=False)",
      "endpoints": {
        "10": {
          "profile_id": 260,
          "device_type": "0x0101",
          "in_clusters": [
            "0x0000",
            "0x0003",
            "0x0004",
            "0x0005",
            "0x0006",
            "0x0008"
          ],
          "out_clusters": []
        },
        "12": {
          "profile_id": 260,
          "device_type": "0x0000",
          "in_clusters": [
            "0x0000",
            "0x0003",
            "0x0007"
          ],
          "out_clusters": [
            "0x0003",
            "0x0004",
            "0x0005",
            "0x0006"
          ]
        },
        "13": {
          "profile_id": 260,
          "device_type": "0x0000",
          "in_clusters": [
            "0x0000",
            "0x0003",
            "0x0007"
          ],
          "out_clusters": [
            "0x0003",
            "0x0004",
            "0x0005",
            "0x0006"
          ]
        },
        "14": {
          "profile_id": 260,
          "device_type": "0x0000",
          "in_clusters": [
            "0x0000",
            "0x0003",
            "0x0007"
          ],
          "out_clusters": [
            "0x0003",
            "0x0004",
            "0x0005",
            "0x0006"
          ]
        },
        "15": {
          "profile_id": 260,
          "device_type": "0x0000",
          "in_clusters": [
            "0x0000",
            "0x0003",
            "0x0007"
          ],
          "out_clusters": [
            "0x0003",
            "0x0004",
            "0x0005",
            "0x0006"
          ]
        }
      },
      "manufacturer": "Nordic",
      "model": "Dimable_Light_v0.1",
      "class": "zigpy.device.Device"
    }
    assert_signature_matches_quirk(zhaquirks.ck.nordic_switch.CKButton, signature)

