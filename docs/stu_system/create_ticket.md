###  根据用户创建ticket

**请求地址**:
```
    POST     /api/stu_system/auth/authorize/
```

**请求参数**:
```
{
    "user_id": int  必填
}
```

**成功返回**：
```
{
    "code": 0,
    "msg": "success",
    "data": {
        "ticket": "TK-c4iyDFgaNu6TpnGr3o8B"
    }
}
```

**失败返回**：
```

```