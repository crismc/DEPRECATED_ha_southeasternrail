"""Configuration page used for the initial HA integrations screen"""
import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_API_KEY,
    CONF_ARRIVAL,
    CONF_DESTINATIONS,
    CONF_TIME_OFFSET,
    CONF_TIME_WINDOW,
    DOMAIN,
)

from .station_codes import STATIONS

_LOGGER = logging.getLogger(__name__)


@config_entries.HANDLERS.register(DOMAIN)
class SoutheasternConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Southeastern config flow."""

    def __init__(self) -> None:
        """Initialize."""
        self.data_config: dict[str, Any] = {CONF_ARRIVAL: "", CONF_DESTINATIONS: []}

    async def async_step_user(self, user_input=None):
        """Primary configuration information"""
        if user_input is not None:
            self.data_config[CONF_API_KEY] = user_input[CONF_API_KEY]
            self.data_config[CONF_ARRIVAL] = user_input[CONF_ARRIVAL]
            self.data_config[CONF_TIME_OFFSET] = user_input[CONF_TIME_OFFSET]
            self.data_config[CONF_TIME_WINDOW] = user_input[CONF_TIME_WINDOW]
            return await self.async_step_destination()

        # Specify items in the order they are to be displayed in the UI
        data_schema = {
            vol.Required(CONF_API_KEY): str,
            vol.Required(CONF_ARRIVAL): vol.In(STATIONS),
            vol.Required(CONF_TIME_OFFSET, default="20"): str,
            vol.Required(CONF_TIME_WINDOW, default="120"): str,
        }

        return self.async_show_form(step_id="user", data_schema=vol.Schema(data_schema))

    async def async_step_destination(self, user_input=None):
        """Target destination station configuration information"""
        if user_input is not None:
            self.data_config[CONF_DESTINATIONS].append(user_input[CONF_DESTINATIONS])
            # If user ticked the box show this form again so they can add an additional station.
            if user_input.get("add_another", False):
                return await self.async_step_destination()

            return self.async_create_entry(
                title="Southeastern Rail", data=self.data_config
            )

        return self.async_show_form(
            step_id="destination",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_DESTINATIONS): vol.In(STATIONS),
                    vol.Optional("add_another", default=False): cv.boolean,
                }
            ),
        )
