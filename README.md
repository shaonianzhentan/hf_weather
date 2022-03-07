# hf_weather
一个不知道改了几手的和风天气最简单的配置版本

[![hacs_badge](https://img.shields.io/badge/Home-Assistant-%23049cdb)](https://www.home-assistant.io/)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
![visit](https://visitor-badge.laobi.icu/badge?page_id=shaonianzhentan.hf_weather&left_text=visit)

## 使用方式

安装完成重启HA，刷新一下页面，在集成里搜索`和风天气`即可

[![Add Integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=hf_weather)

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

## 如果这个项目对你有帮助，请我喝杯<del style="font-size: 14px;">咖啡</del>奶茶吧😘
|支付宝|微信|
|---|---|
<img src="https://github.com/shaonianzhentan/ha-docs/raw/master/docs/img/alipay.png" align="left" height="160" width="160" alt="支付宝" title="支付宝">  |  <img src="https://github.com/shaonianzhentan/ha-docs/raw/master/docs/img/wechat.png" align="left" height="160" width="160" alt="微信支付" title="微信">


## 关注我的微信订阅号，了解更多HomeAssistant相关知识
<img src="https://github.com/shaonianzhentan/ha-docs/raw/master/docs/img/wechat-channel.png" height="160" alt="HomeAssistant家庭助理" title="HomeAssistant家庭助理"> 

---
**在使用的过程之中，如果遇到无法解决的问题，付费咨询请加Q`635147515`**