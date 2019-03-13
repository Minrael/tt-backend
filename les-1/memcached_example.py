from werkzeug.contrib.cache import MemcachedCache



#def get_my_item():
#	rv = cache.get('my-item')
#	print(rv)
#	if rv is None:
#		rv = calculate_value()
#		cache.set('my-item', rv, timeout=5*60)
#	return rv


if __name__ == "__main__":
    cache = MemcachedCache(['127.0.0.0:11211'])
    rv = cache.get('key')
    if rv is None:
        cache.set('key', 'value')
        print(cache)
        rv = cache.get('key')
    print( rv )
