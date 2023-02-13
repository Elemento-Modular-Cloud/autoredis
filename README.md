# redis_object
A smarter redis handler

# Modules
This package implements two modules

- `autoredis.ObjectRedis` adds two methods `get_obj` and `set_obj` to allow users to store serializable objects in a redis db.

- `autoredis.AutoRedis` automatically starts a docker container with redis installed and automatically connected to the pyhton handler.

# Example

```python
with AutoRedis(
        host='localhost',
        pwd=os.path.join(os.path.dirname(__file__)),
        port=6379) as r:
    
    r.set('foo', 'bar')
    
    o = complex_object()
    r.set_obj('obj', o)
```

# License
See [LICENSE](LICENSE)