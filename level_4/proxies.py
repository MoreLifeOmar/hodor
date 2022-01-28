#!/usr/bin/python3
"""module containing class for proxy_lists
"""

import requests

class Proxy_List:
    """proxy list class for use in generating custom lists of proxies
        currently only works with provided url, using non default produces
        unknown behavior
    """

    default_url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"

    def __init__(self, p_list=None, url=None):
        if url is None:
            self.url = self.default_url
        else:
            self.url = url
        self.__proxy_i = 400
        if p_list is None:
            self.p_list = self.get_proxy_list()
            print("{} proxies created".format(len(self.p_list)))
        else:
            self.p_list = p_list

    @property
    def proxy_i(self):
        return self.__proxy_i

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise TypeError("Proxy_List url must be of str type")
        self.__url = value

    @property
    def p_list(self):
        return self.__list

    @p_list.setter
    def p_list(self, value):
        if not isinstance(value, list):
            raise TypeError("Proxy_List list must be a list type")
        self.__list = value

    def get_proxy(self):
        """gets the proxy from current instance with index
            and advances index
        """
        proxy = self.p_list[self.proxy_i]
        self.__proxy_i += 1
        return proxy

    def get_proxy_list(self):
        """gets the proxy list from current instance's url
        """
        url = self.url
        r = requests.get(url)
        content = r.content
        builder = ""
        proxies = []
        for c in r.content:
            if chr(c) == '\n':
                builder = builder.replace("null", "None")
                proxy_eval = eval(builder)
                if not isinstance(proxy_eval, dict):
                    print("error converting proxy line")
                else:
                    host = str(proxy_eval.get("host"))
                    port = str(proxy_eval.get("port"))
                    proxies.append(":".join([host, port]))
                builder = ""
            builder += chr(c)
        return proxies
