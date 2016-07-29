"""Storage unit snapshot.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

from time import gmtime, strftime

class StorageUnitSnapshot(object):
    """Storage unit snapshot.

    """

    def __init__(self, storage_unit):
        """Initialize this strorage unit snapshot.

        """
        self._data = {}
        self._data["name"] = storage_unit.name
        self._data["time"] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        self._data["capacity"] = storage_unit.capacity
        self._data["count"] = storage_unit.count()
        self._data["size"] = storage_unit.size()
        self._data["load"] = storage_unit.load()


    def __str__(self):
        """Stringify this storage unit snapshot.

        """
        return "(" + \
               "name:" + self._data["name"]         + \
               "time:" + self._data["time"]         + \
               "capacity:" + self._data["capacity"] + \
               "count:" + self._data["count"]       + \
               "size:" + self._data["size"]         + \
               "load:" + self._data["load"]         + \
               ")"

    def __getitem__(self, key):
        """Return the value of a given key in this storage unit snapshot.

        :param key: The key.
        :type key: string.
        :raise: KeyError

        """
        return self._data[key.lower()]


    def storage_unit_name(self):
        """Return the name of the storage_unit of this storage unit.

        """
        return self._data['name']
