import sys
import os
import random
from multiprocessing import Pool
from netaddr import *

def rasterize(ip):
    print "scanning %s..." % ip
    os.system("phantomjs rasterize.js http://%s/ images/%s.png" % (ip, ip))

if __name__ == '__main__':
    p = Pool(4)
    for iprange in sys.argv[1:]:
        hosts = list(IPNetwork(iprange).iter_hosts())
        random.shuffle(hosts)
        p.map(rasterize, hosts)

