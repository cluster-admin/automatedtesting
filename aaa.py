import pyttsx3 as p
e = p.init()
while True:
      e.say('	GET 产 生 一 个 TCP 数据（http  header 和 data），POST 先发送 http header返回100后发'
            'GET在浏览器回退时是无害的，而POST会再次提交请求。'
            'GET产生的URL地址可以被Bookmark，而POST不可以。'
            'GET请求会被浏览器主动cache，而POST不会，除非手动设置。'
            'GET请求只能进行url编码，而POST支持多种编码方式。'
            'GET请求参数会被完整保留在浏览器历史记录里，而POST中的参数不会被保留。'
            'GET请求在URL中传送的参数是有长度限制的，而POST么有。'
            'GET只接受ASCII字符，而POST没有限制。'
            'GET比POST更不安全，因为参数直接暴露在URL上，所以不能用来传递敏感信息。'
            'GET参数通过URL传递，POST放在Request body中')
      e.runAndWait()
      #

