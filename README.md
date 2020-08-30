# "起点月票榜爬虫"API 使用文档

本项目在 [GitHub](https://github.com/xiongyi24/QiDianSpider) 上开源

本项目可以通过指定API按书籍序号或者页码检索[起点月票榜](https://www.qidian.com/rank/yuepiao?style=1&page=1)书籍的信息

<br>

⚠ 如果本项目侵犯了您或您公司的权益，请您联系作者，作者将在第一时间删除项目，保护您的权益

联系方式：yi.xiong@cumt.edu.cn



## ① 验证身份

为了防止恶意攻击，使用本项目API需要验证身份

### 1. GET 方法

使用登陆方式，输入用户名密码即可

### 2. POST 方法

####  获取令牌

**POST 方法**

```url
https://www.xiongyi24.club/book/token
```

请求参数（json）：

```json
{
    username: "username",
    password: "password"
}
```

返回结果：

```json
{
    username - token: "token......"
}
```

令牌的有效期为30分钟

#### b. 使用令牌

每次请求在请求头中加一个 Authorization

```python
headers = {
    'Authorization':'Bearer ' + token
    }
```



## ② 按指定书籍序号检索

**GET 方法**

```url
https://www.xiongyi24.club/book/ranking/<int:ranking>
```

其中 `<int:ranking>` 为指定的书籍序号

**POST 方法**

```url
https://www.xiongyi24.club/book/ranking
```

请求参数：

```json
{
    ranking: num
}
```

注意在请求头中携带令牌



## ③ 按指定页码检索

**GET 方法**

```url
https://www.xiongyi24.club/book/page/<int:page>
```

其中 `<int:page>` 为指定的书籍序号

**POST 方法**

```url
https://www.xiongyi24.club/book/page
```

请求参数：

```json
{
    page: num
}
```

注意在请求头中携带令牌