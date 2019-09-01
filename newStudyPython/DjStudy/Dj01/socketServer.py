import socket
import time
# 生成socket
sk = socket.socket()
# 绑定ip和端口
sk.bind(("127.0.0.1",8001))
# 监听数量
sk.listen(3)

def hi(url):
    with open("hi.html","r",encoding="utf-8") as r1:
        ret = r1.read()
    ret2 = ret.replace('@@xx@@',str(time.time()))
    return bytes(ret2, encoding='utf-8')
    #return bytes('hello {}'.format(url),encoding='utf-8')

def hello(url):
    with open("hello.html","r") as r1:
        return r1.read()
    #return bytes('hello {}'.format(url),encoding='utf-8')

def error(url):
    with open("error.html","r") as r1:
        return r1.read()
    #return bytes('error {}'.format(url),encoding='utf-8')

url_func = [
    ("/hi/",hi),
    ("/hello/",hello),
]

# 等待客户连接。写一个死循环
while 1:
    # 获取客户端连接
    # 把没用变量用_保存
    conn, _ = sk.accept()
    # 接收客户发来的消息
    data = conn.recv(8096)
    # 把收据的byte类型转成str
    data_str = str(data,encoding="utf-8")
    # /r/n分割字符串,获取域名后的url
    # 给客户端回复消息
    li = data_str.split('\r\n')
    # 在按照空格切割字符串
    li = li[0].split()
    # 获取第二个
    url = li[1]
    conn.send(b'http/1.1 200 OK \r\ncontent-type:text/html;charset=utf-8\r\n\r\n')   #浏览器返回协议
    # 浏览器返回内容
    for i in url_func:
        if i[0] == url:
            response = i[1](url)
            break
    else:
        response = error(url)
    # 关闭
    conn.send(response)
    conn.close()
    #sk.close()


# 总结
    #了解下jinja2
    #了解下wsgiref