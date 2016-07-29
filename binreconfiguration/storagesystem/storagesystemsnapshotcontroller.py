# coding=utf-8

"""Storage system snapshot controller

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

class SuspendedStorageSystemSnapshotController(object):

    def __init__(self, storage_system):
        self._storage_system = storage_system

    def __enter__(self):
        """Suspend the storage system snapshot controller.
        """
        self._storage_system.snapshot_controller.suspend()
        return self._storage_system

    def __exit__(self, type, value, traceback):
        """Restart the storage system snapshot controller.
        """
        self._storage_system.snapshot_controller.run()


class StorageSystemSnapshotController(object):
    """Storage system snapshot controller.

    """

    SUSPENDED = 0 # do not store storage system snapshot
    RUNNING   = 1 # do store storage system snapshot

    def __init__(self):
        """Initialize a storage system snapshot controller.
        """
        self._storage_system_snapshots = []
        self._state = self.__class__.RUNNING

    @property
    def storage_system_snapshots(self):
        """Return the list of the storage system snapshots.
        """
        return self._storage_system_snapshots

    @property
    def state(self):
        """Return the current state of this storage system snapshot controller.
        """
        return self._state

    def append(self, storage_system_snapshot):
        """Append a new storage system snapshot.

        :param snapshot: Thestorage system snapshot.
        :type snapshot: ultrastorage.storagesystem.Snapshot.

        """
        if self.state == self.__class__.RUNNING:
            self._storage_system_snapshots.append(storage_system_snapshot)

    def add(self, snapshot):
        """Alias for append.
        """
        self.append(snapshot)

    def snapshots(self):
        """Return a copy of all strorage system snapshots.
        """
        return self.storage_system_snapshots[:]

    def suspend(self):
        """Suspend the storage system snapshot controller.
        """
        self._state = self.__class__.SUSPENDED

    def run(self):
        """Restart the storage unit snapshot controller.
        """
        self._state = self.__class__.RUNNING

    def clean(self):
        """Delete all controlled storage system snapshots.
        """
        self._storage_system_snapshots = []

    def last(self):
        """Return the last controlled storage system snapshot.
        """
        return self.storage_system_snapshots[-1]

    def __len__(self):
        """Return the the number controlled storage system snapshots.
        """
        return len(self.storage_system_snapshots)

    def __iter__(self):
        """Iterate over storage system snapshots.
        """
        return iter(self.storage_system_snapshots)


