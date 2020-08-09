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
    {% set state = state_attr('weather.tian_qi', 'forecast')%}
    今天的天气是{{state[0].condition_cn}}，最高温度：{{state[0].temperature}}度，最低温度：{{state[0].templow}}度，
    明天的天气是{{state[1].condition_cn}}，最高温度：{{state[1].temperature}}度，最低温度：{{state[1].templow}}度，
    后天的天气是{{state[2].condition_cn}}，最高温度：{{state[2].temperature}}度，最低温度：{{state[2].templow}}度
service: ha_cloud_music.tts
```

```yaml
data:
  message: >-
    {% set state = state_attr('weather.tian_qi', 'hourly_forecast')%}
    {{state[0].datetime | regex_replace(now().strftime('%Y-%m-%d'), '')}}
    的天气是{{state[0].condition_cn}}，温度是{{state[0].temperature}}度，
    {{state[1].datetime | regex_replace(now().strftime('%Y-%m-%d'), '')}}
    的天气是{{state[1].condition_cn}}，温度是{{state[1].temperature}}度，
    {{state[2].datetime | regex_replace(now().strftime('%Y-%m-%d'), '')}}
    的天气是{{state[2].condition_cn}}，温度是{{state[2].temperature}}度
service: ha_cloud_music.tts
```