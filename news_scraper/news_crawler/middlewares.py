import logging

class MyMiddleware(object):
    def process_request(self, request, spider):
        spider.logger.info('User agent: %s' % request.headers['User-Agent'])
        return None

    def proccess_response(self, response, spider):
        spider.logger.info('Proxy: %s' % response.meta.get("proxy"))
        return response
