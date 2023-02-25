"""Spook - Not your homey."""
from __future__ import annotations

import voluptuous as vol

from homeassistant.components.homeassistant import DOMAIN
from homeassistant.core import ServiceCall
from homeassistant.helpers import config_validation as cv, device_registry as dr

from ..models import AbstractSpookService


class SpookService(AbstractSpookService):
    """Home Assistant Core integration service to disable a device."""

    domain = DOMAIN
    service = "disable_device"
    schema = vol.Schema(
        {
            vol.Required("device_id"): cv.string,
        }
    )

    async def async_handle_service(self, call: ServiceCall) -> None:
        """Handle the service call."""
        device_registry = dr.async_get(self.hass)
        device_registry.async_update_device(
            device_id=call.data["device_id"],
            disabled_by=dr.DeviceEntryDisabler.USER,
        )