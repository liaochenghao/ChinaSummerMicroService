### 验证ticket有效性

**请求地址**:
```
    GET     /api/stu_system/auth/authorize/
```

**请求参数**:
```
{
    "ticket": str   必填
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
        "valid_ticket":   boolean  是否有效
        "user_id":        int    用户id或者None
        "err_msg": null   str    错误信息
    }
}
```

**失败返回**：
```

```