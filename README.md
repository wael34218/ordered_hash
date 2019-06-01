# Python Ordered Hash

## Installation

```
pip install git+git://github.com/wael34218/ordered_hash
```

## Usage

```
from ordered_hash.ordered_hash import OrderedHash

myhash = OrderedHash([("Element", 4), (4, 2), ("key", "value")])

myhash.insert("key1", "value1")
print(myhash)
print(len(myhash)
myhash.delete("key1")
```
