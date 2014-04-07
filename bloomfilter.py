from pybloomfilter import BloomFilter
import random, sys
from Crypto.Hash import SHA256

keyDigest_list = []
count = 1500000
count_base = 1000000
error_rate = 0.005
keyLen = 2048
keyDigestLen = 32
#HASH = SHA256.new()
keyDigestFile = '/home/enzo/CCNx/python_projects/PublicKeyDigest'

# write key digest to file
def write_keyDigest(keyDigestFile):
	HASH = SHA256.new()
	for i in range(count_base):
		key = random.randint(2**2047, 2**2048-1)
		HASH.update(str(key))
		keyDigest = HASH.digest()
		keyDigest_list.append(keyDigest)
		if i%10000 == 0: print i
	
	FILE = open(keyDigestFile, 'w')

	for i in range(len(keyDigest_list)):
		FILE.write(keyDigest_list[i])

	FILE.close()

# create a bloom filter
def create_bf():
	bf = BloomFilter(count, error_rate, 'filter_base.bloom')
	keyDigest_list = []
	FILE = open(keyDigestFile, 'r')
	
	for i in range(count):
		keyDigest = FILE.read(keyDigestLen)
		keyDigest_list.append(keyDigest)
		
	FILE.close()
	
	for publicKeyID in keyDigest_list:
		bf.add(publicKeyID)

def check_bf():
	bf = BloomFilter.open('filter_base.bloom')
	FILE = open(keyDigestFile, 'r')
	keyDigestAll = FILE.read()
	for i in range(count_base/100):
		index = random.randint(0, count_base-1)
		publicKeyID = keyDigestAll[index*keyDigestLen:(index+1)*keyDigestLen]
		if publicKeyID in bf:
#			print "i keyDigest in bf"
			continue
		else: 
			print "keyDigest not in bf"
			break
	

if __name__ == '__main__':
#	write_keyDigest(keyDigestFile)
#	create_bf()
	check_bf()





