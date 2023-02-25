import pickle
import unittest


class MyTestCase(unittest.TestCase):
    my_attribute = 1


class MyPickler(pickle.Pickler):
    def reducer_override(self, obj):
        """Custom reducer for MyClass."""
        if getattr(obj, "__name__", None) == "MyClass":
            return type, (obj.__name__, obj.__bases__,
                          {'my_attribute': obj.my_attribute})
        else:

            # For any other object, fallback to usual reduction
            return NotImplemented


f = pickle.APPENDS
f.capitalize()
f.title()

del f

unpickled_class = pickle.Pickler

assert isinstance(unpickled_class, type)
assert unpickled_class.__name__ == "MyClass"
assert unpickled_class.my_attribute == 1

if __name__ == '__main__':
    unittest.main()
