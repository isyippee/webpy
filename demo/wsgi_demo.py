# coding: utf8
HELLO_WORLD = b"Hello world!\n"


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [HELLO_WORLD]


def run(application):
    # 接受到客户端的请求，设置environ
    environ = {}

    # server 处理request的方法，整理response
    def start_response(status, response_headers, exc_info=None):
        print 'status is %s' % status
        print 'response_headers is %s' % response_headers

    # 将environ和start_response传给app，执行app获得结果
    result = application(environ, start_response)

    # 模拟回写给客户端
    def write(data):
        print data

    # 处理得到的結果
    for data in result:
        write(data)


def refmain():
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, simple_app)
    print "Serving on port 8000..."
    httpd.serve_forever()


def testmain():
    run(simple_app)


if __name__ == '__main__':
    testmain()
