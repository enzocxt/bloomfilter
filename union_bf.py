from pybloomfilter import BloomFilter
from pyccn import Key
from Crypto.Hash import SHA256
import random, sys, threading

count = 10000
error_rate = 0.01
keyDigest_list = []
keyLen = 2048
# key digest length is 32 bytes
HASH = SHA256.new()

for i in range(count):
	key = random.randint(2**2047, 2**2048-1)
	HASH.update(str(key))
	keyDigest = HASH.digest()
	keyDigest_list.append(keyDigest)

FILE = open('/home/enzo/CCNx/python_projects/bloomfilter/PublicKeyDigest01', 'w')
for i in range(count):
	FILE.write(keyDigest_list[i])
FILE.close()

bf_base = BloomFilter.open('filter.bloom')
bf = bf_base.copy_template('filter01.bloom')

for publicKeyID in keyDigest_list:
	bf.add(publicKeyID)

bf.union(bf_base)


