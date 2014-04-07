from pybloomfilter import BloomFilter
from pyccn import Key
from Crypto.Hash import SHA256
import random, sys, threading

count = 1000000
error_rate = 0.01
keyDigest_list = []
keyLen = 2048
# key digest length is 32 bytes

FILE = open('/home/enzo/CCNx/python_projects/bloomfilter/PublicKeyDigest', 'r')

for i in range(count):
	keyDigest_list.append(FILE.read(32))

FILE.close()

bf = BloomFilter.open('filter.bloom')
for i in range(len(keyDigest_list)):
	if keyDigest_list[i] in bf:
		continue
	else:
		print "keyDigest is not in bloom filter."
		break


