# hf_weather
一个不知道改了几手的和风天气最简单的配置版本


实体配置
```yaml
weather:
  - platform: hf_weather
    name: 天气
    city: shanghai
    appkey: 06642046425c68a351817b5b020b591f
```

注意：请自行申请appkey: https://wx.jdcloud.com/market/datas/26/10610

Lovelace配置
```yaml
type: 'custom:hf_weather-card'
entity: weather.tian_qi
```
