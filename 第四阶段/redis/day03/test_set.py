import redis



r=redis.Redis(password='123456')

r.sadd('武将','张飞','周瑜','关羽')
r.sadd('文臣','周瑜','诸葛亮','司马懿')
for i in r.sinter('武将','文臣'):
    print(i.decode())

for i in r.sunion('武将','文臣'):
    print(i.decode())

for i in r.sdiff('武将','文臣'):
    print(i.decode())
    

for i in r.sdiff('文臣','武将'):
    print(i.decode())