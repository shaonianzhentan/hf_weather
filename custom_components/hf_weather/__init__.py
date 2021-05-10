
import homeassistant
from .weather import async_setup_platform

def setup(hass, config):
    # 注册静态目录
    VERSION = '1.2.1'
    ROOT_PATH = '/hf_weather-local'
    hass.http.register_static_path(ROOT_PATH, hass.config.path('custom_components/hf_weather/local'), False)
    hass.components.frontend.add_extra_js_url(hass, ROOT_PATH + '/hf_weather-card/hf_weather-card.js?ver=' + VERSION)
    hass.components.frontend.add_extra_js_url(hass, ROOT_PATH + '/hf_weather-card/hf_weather-more-info.js?ver=' + VERSION)
    return True

async def async_setup_entry(hass, config_entry):
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(config_entry, "weather"))
    return True