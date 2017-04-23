import re

def parseProxies():
    with open('fetched_proxies.txt') as old_file:
        with open('proxies.txt', 'w') as new_file:
            pattern_with_china = re.compile('^.+china.+$')
            patter_with_pound = re.compile('^(.+)#.+$')
            for line in old_file:
                line = re.sub(pattern_with_china, '', line)
                line = re.sub(patter_with_pound, r'\1', line)
                if re.match(r'.+', line):
                    new_file.write(line)

    with open('proxies.txt', 'r') as f:
        proxyList = [line[:-1] for line in f]
        return proxyList


if __name__ == '__main__':
    parseProxies()
