def parseProxies():
    with open('proxies.txt', 'r') as f:
        proxyList = [line[:-1] for line in f]
        return proxyList


if __name__ == '__main__':
    print(parseProxies())