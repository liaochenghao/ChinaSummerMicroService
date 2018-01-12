###  发送文本消息

**请求地址**:
```
    POST    /api/weixin/service_center/send_template_message/
```

**请求参数**:
```
{
    "openid": str   用户openid  必填
    "template_id": str  发送模板id  必填
    "access_token":  access_token  选填  若access_token为空，则默认以署校联盟服务中心发送给用户,
    "url":  str 模板消息的url 选填
    "send_data": dict 必填  模板消息的内容
}
```

```
备注： send_data需填写模板消息内容，例如：
"send_data": {
        "first": "您的课程顾问为您选择了课程",
        "keyword1": "高等数学",
        "keyword2": "2018-01-12 18:00:00",
        "remark": "上课地点: 武汉理工大学\n\n请尽快确认所选课程，若所选课程有误，请立即与您的专属课程顾问联系，更改课程！"
    }
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
        "errcode": 0,       errcode 为0表示成功
        "errmsg": "ok",
        "msgid": 101927280581820416
    }
}
```

**失败返回**：
```

```