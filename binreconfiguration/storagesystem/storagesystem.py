# coding=utf-8

"""Storage system.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

from ultrastorage.bin import Bin
from .storagesystemsnapshot import StorageSystemSnapshot
from .storagesystemsnapshotcontroller import StorageSystemSnapshotController
from .storagesystemexception import StorageSystemException

class StorageSystem(object):
    """Storage system unit.

    """

    def __init__(self, bin_capacities):
        """Initialize this storage system.

        :param snapshot_controller: The snapshot controller.
        :type snapshot_controller: ultrastorage.storagesystem.SnapshotController.
        :param name: The name of this bin.
        :type name: string.

        """
        # associate a storage system snapshot controller to this storage system
        self._snapshot_controller = StorageSystemSnapshotController()

        # give this storage system a name
        self._name = name
        if self._name is None:
            # give this storage system unit a generic name
            self._name = "{}-{}".format(self.__class__.__name__, id(self))

        # bins
        self._bins = [Bin(capacity) for capacity in bin_capacities]

    def __iter__(self):
        return iter(self._bins)

    @property
    def bins(self):
        """
        """
        return self._bins

    @property
    def snapshot_controller(self):
        return self._bins()

    def __len__(self):
        """Return the number of bins in this storage system unit.
        """
        return len(self._bins)

    def count(self):
        """Return the number of items stored in the bins of this storage system.
        """
        return sum(bin.count() for bin in self._bins)

    """alias.
    """
    number_of_items = count

    def size(self):
        """Return the total size of the items stored in the bins of
        this storage system.
        """
        return sum(bin.size() for bin in self._bins)

    def filtered_items(self, predicate):
        """Return the  of the bins monitored by this storage system
        that satisfy a given predicate:

        :param predicate: The predicate function.
        :type predicate: Function:

        """
        return ((bin, item)
                for bin in self._bins
                for item in bin
                if predicate(item))

    def items(self):
        """Return the list of all items stored in the bins monitored by
        this storage system.

        """
        return filtered_items(lambda item: True)

    def small_items(self, maximum_size):
        """Return the list of all small enough items.

        :param maximum_size: The maximum size of an item.
        :type maximum_size: Numeric

        """
        return filtered_items(lambda item: item.size <= maximum_size)

    def large_items(self, minimum_size):
        """Return the list of all large enough items.

        :param minimum_size: The minimum size of an item.
        :type minimum_size: Numeric

        """
        return filtered_items(lambda item: item.size >= minimum_size)

    def filtered_bins(self, predicate):
        """Filter the list of bins.

        :param predicate: The function predicate to filter the StorageSystem units.
        :type predicate: function.

        """
        return (bin for bin in self._bins if predicate(bin))

    def free_space_bins(self, free_space):
        """Return the list of bins with large enough free space.

        :param requested_free_space: The needed free space.
        :type requested_free_space: Numeric.

        """
        return self.filter(lambda bin: bin.free_space() >= free_space)

    def small_load_bins(self, maximum_load):
        """Return the list of the bins monitored by this storage system
        with small enough load.

        :param maximum_load: The maximum allowed load of a bin.
        :type maximum_load: Numeric.

        """
        return self.filter(lambda bin: bin.load() >= maximum_load)

    def large_load_bins(self, minimum_load):
        """Return the list of the bins monitored by this storage system
        with large enough load.

        :param minimum_load: The inimum allowed load of a bin.
        :type minimum_load: Numeric.

        """
        return self.filter(lambda bin: bin.load() >= minimum_load)

    def _bins_by_ascending_key(self, key):
        """Return the list of the bins monitored by this storage system
        sorted by ascending key.

        :param key: The bin key the sort operates on.
        :type key: String.

        """
        return sorted(self._bins, key=operator.attrgetter(key))

    def _bins_by_descending_key(self, key):
        """Return the list of the bins monitored by this storage system
        sorted by descending key.

        :param key: The bin key the sort operates on.
        :type key: String.

        """
        return sorted(self._bins, key=operator.attrgetter(key), reverse=True)

    def bins_by_ascending_capacity(self):
        """Return the list of the bins monitored by this storage system
        sorted by ascending capacity.
        """
        return self._bins_by_ascending_key('capacity')

    def bins_by_decending_capacity(self):
        """Return the list of the bins monitored by this storage system
        sorted by descending capacity.
        """
        return self._bins_by_descending_key('capacity')

    def bins_by_ascending_load(self):
        """Return the list of the bins monitored by this storage system
        sorted by ascending load.
        """
        return self._bins_by_ascending_key('load')

    def bins_by_descending_load(self):
        """Return the list of the bins monitored by this storage system
        sorted by descending load.
        """
        return self._bins_by_ascending_key('load')

    def bins_by_ascending_size(self):
        """Return the list of the bins monitored by this storage system
        sorted by ascending size.
        """
        return self._bins_by_ascending_key('size')

    def bins_by_descending_size(self):
        """Return the list of the bins monitored by this storage system
        sorted by descending size.
        """
        return self._bins_by_ascending_key('size')

    def bins_by_ascending_count(self):
        """Return the list of the bins monitored by this storage system
        sorted by ascending count.
        """
        return self._bins_by_ascending_key('count')

    def bins_by_descending_count(self):
        """Return the list of the bins monitored by this storage system
        sorted by descending count.
        """
        return self._bins_by_ascending_key('count')

    def random_bin(self):
        """Return a bin choosed at random.

        :raises: IndexError

        """
        return random.choice(self._bins)

    def random_nonempty_bin(self):
        """Return a non-empty bin choosed at random.

        :raises: IndexError

        """
        return random.choice(self.non_empty_bins())

    def random_free_space_bin(self, free_space):
        """Return a StorageSystem unit of this storage system choosed at random with large enough free space.

        :raises: IndexError

        """
        return random.choice(self.free_space_bins(free_space))

    def random_item(self):
        """Return an item stored in this storage system choosed at random.


        :raises: IndexError

        """
        return random.choice(self.items())

    def random_item2(self):
        """Return an item stored in this storage system choosed at random.


        :raises: IndexError

        """
        bin = self.random_nonempty_bin()
        return (bin, random.choice(bin.items()))

    def random_small_item(self, maximum_size):
        """Return a small enough item stored in this storage system choosed at random.

        :param minimum_size: The maximum size of a choosen item.
        :type minimum_size: Numeric.
        :raises: IndexError

        """
        return random.choice(self.small_items(maximum_size))

    def random_large_item(self, minimum_size):
        """Return a large enough item stored in this storage system choosed at random.

        :param minimum_size: The minimum size of a choosen item.
        :type minimum_size: Numeric.
        :raises: IndexError

        """
        return random.choice(self.large_items(minimum_size))

    def _bin_index_from_bin_name(self, bin_name):
        """Return the index in this storage system of a bin
        (given by its name).

        :param bin_name: The name of the bin.
        :type bin_name: string.
        :raises: KeyError

        """
        try:
            indexed_bins = enumerate(self._bins)
            return next(index
                        for (index, bin) in indexed_bins
                        if bin.name == bin_name)
        except StopIteration:
            raise KeyError("no such bin name '{}'".format(bin_name))

    def __contains__(self, bin_name):
        """Return True iff this storage system contains a bin
        with a given name.

        :param bin_name: The name of the bin.
        :type bin_name: string.
        :raises: KeyError

        """
        if bin_name is None:
            return False

        try:
            self._bin_index_from_bin_name(bin_name)
            return True
        except KeyError:
            return False

    def __getitem__(self, bin_name):
        """Access to bin *bin_index*.

        :param bin_name: The name of the bin.
        :type bin_name: string.
        :raises: KeyError

        """
        try:
            indexed_bins = enumerate(self._bins)
            index = next(index
                         for (index, bin) in indexed_bins
                         if bin.name == bin_name)
            return self._bins[index]
        except StopIteration:
            raise KeyError("no such bin name '{}'".format(bin_name))

    def __str__(self):
        """Return a string representation of this storage system.
        """
        return "(name={},".format(self.name) + \
               "number of bins={},".format(len(self._bins)) + \
               "type={},".format(self.__class__.TYPE) + \
               "transfer time manager={},".format(self.transfer_time_manager) + \
               "bins=(" + \
               ",".join([str(bin) for bin in self._bins]) + \
               "))"

    def add_item(self, environment, bin_name, item):
        """Add an item to this storage system unit.

        :param bin_name: The name of the bin that should accomodate the item.
        :type bin_name: string.
        :param item: The item to add.
        :type item: ultrastorage.item.Item.
        :raises: KeyError.

        """
        # let the item event controller know about this item to be added
        item_event = ItemEvent(ItemEvent.REQUEST_ADD_ITEM, environment.now, item)
        self._item_event_controller.add(item_event)

        # get a reference to the bin
        bin = self[bin_name]

        # reserve the memory needed to add the item
        bin.reserve_memory(item.size)

        # request a bin cpu
        with bin.request() as request:

            # get the cpu
            yield request

            # let the item event controller know about this item to be added
            item_event = ItemEvent(ItemEvent.START_ADD_ITEM, environment.now, item)
            self._item_event_controller.add(item_event)

            # item transfer time
            yield environment.timeout(self.transfer_time_manager.transfer_time(item.size))

            # add the item
            bin.restore_memory(item.size)
            bin.add_item(item)

            # let the item event controller know about this item to be added
            item_event = ItemEvent(ItemEvent.END_ADD_ITEM, environment.now, item)
            self._item_event_controller.add(item_event)

        # let the storage system snapshot controller know about this item.
        if self.snapshot_controller is not None:
            self.snapshot_controller.add(self.snapshot(environment))

    def clean_snapshot_controller(self):
        """Remove all stored snapshots of this strorage unit.
        """
        if self.snapshot_controller is not None:
            self.snapshot_controller.clean()

    def snapshot(self, environment):
        """Return the snapshot of this storage system.
        """
        return StorageSystemSnapshot(environment, self)

    def _snapshot(self, environment):
        """Take and record a snapshot of this storage system.
        """
        if self.snapshot_controller is not None:
            self.snapshot_controller.add(self.snapshot(environment))

    def force_snapshot(self, environment):
        self._snapshot(environment)

    def add_bin(self, environment, capacity, cpu, name=None):
        """Add a bin to this storage system.

        :param capacity: The capacity of the new bin.
        :type capacity: Numeric.
        :param cpu: The numbers of cpu of the new bin.
        :type cpu: int.
        :param name: The name of the new bin.
        :type name: string.

        """
        if name in self:
            raise StorageSystemException("bin '{}' exists".format(name))

        # create a new bin and add it to this storage system
        bin = StorageUnit(environment, capacity, cpu, name)
        self._bins.append(bin)

        # let the snapshot controller know about this new bin
        self._snapshot(environment)

        # let the caller know about the name of this new bin
        return bin.name

    def remove_bin(self, bin_name):
        """Remove an existing bin from this storage system.

        :param bin_name: The name of the bin to be removed.
        :type bin_name: string.

        """
        bin_index = self._bin_index_from_bin_name(bin_name)

        del self._bins[bin_index]

        if self.snapshot_controller is not None:
            self.snapshot_controller.add(self.snapshot())


def storage_system_builder(capacities, name=None, bin_names=None):
    """Convenient function to construct a storage system from the capacity
    and cpu lists of the bins.


    """
    #
    storage_system = StorageSystem(transfer_time_manager, name=name)

    # suspend the storage system snapshot controller
    storage_system.snapshot_controller.suspend()

    # the capacity and the cpu of each bin must be given.
    if len(capacities) != len(cpus):
        raise StorageSystemException("bad bad bad")
    n = len(capacities)

    # deal with bin names.
    if bin_names is None:
        bin_names = [None for _ in range(n)]
    elif len(bin_names) < n:
        bin_names = bin_names + [None for _ in range(n - len(bin_names))]

    # add the bins.
    for (capacity, cpu, bin_name) in zip(capacities, cpus, bin_names):
        storage_system.add_bin(environment, capacity, cpu, bin_name)

    # reactivate the storage system snapshot controller
    storage_system.snapshot_controller.run()

    # let the snapshot controller know about these bins
    if storage_system.snapshot_controller is not None:
        storage_system.snapshot_controller.add(storage_system.snapshot())

    # done, return the ready to go storage system.
    return storage_system
