# hf_weather
一个不知道改了几手的和风天气最简单的配置版本


>实体配置

```yaml
weather:
  - platform: hf_weather
    name: 天气
    city: shanghai
    appkey: 06642046425c68a351817b5b020b591f
```
注意：请自行申请appkey: https://wx.jdcloud.com/market/datas/26/10610

> Lovelace配置

```yaml
type: 'custom:hf_weather-card'
entity: weather.tian_qi

# 不设置则同时显示
mode: hourly按小时天气预报、daily按天天气预报

# 不设置则使用entity的friendly_name
title: 卡片标题
```

> TTS语音提醒模板
```yaml
data:
  message: >-
    {% set state = state_attr('weather.tian_qi', 'forecast')[0]%}
    今天的天气是{{state.condition_cn}}，最高温度：{{state.temperature}}度，最低温度：{{state.templow}}度
service: ha_cloud_music.tts
```