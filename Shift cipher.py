ch7 = 'L|k€y+*^*zo‚*€kvsno|*k€om*vo*zk}}*cyvksr '
for i in range(256):
    print('%i: %s' % (i, repr(''.join([chr((ord(c) + i) % 256) for c in ch7]))))
