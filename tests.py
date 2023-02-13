from autoredis import AutoRedis
import os

class obj():
    def __init__(self, val):
        self.value = val
        
        self.string = "object member"
        
    def __repr__(self) -> str:
        return f"{self.value}_{self.string}"

with AutoRedis(
        host='localhost',
        pwd=os.path.join(os.path.dirname(__file__)),
        port=6379) as r:
    
    r.set('foo', 'bar')
    value = r.get('foo')
    # for key in r.keys():
    #     print(r.get_obj(key))
    o = obj(9)
    r.set_obj('obj', o)
    print(r.keys())
    print(r.get_obj('obj'))
    r.delete("foo")
    r.delete("obj")