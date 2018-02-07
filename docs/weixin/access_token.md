###  获取署校联盟服务中心access_token

**请求地址**:
```
    GET     /api/weixin/service_center/access_token/
```

**请求参数**:
```
    {
        "app_id": str   选填
        "app_secret": str   选填
    }
```
    如果未传入app_id,app_secret则默认调用学生系统所在的微信公众号的access_token
```
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
        "access_token": "5_awQV99LSRYU3Mfz85AS6IgO-f_xE3FtaD1-P_zxsS0H9d_Y4NSYuPoUU0-Rnmxm16o2v_M51B0DBj41oL6VabyRZypzl3S6JhapQM3OmTf1FXh2J1l5LxiFj3w_pabigsnHT3RAG7aLIvVyfQFVfACAJYO"
    }
}
```

**失败返回**：
```

```