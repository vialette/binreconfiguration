# coding=utf-8

"""Storage system snapshot

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""


class StorageSystemSnapshot(object):
    """Storage system snapshot class.

    """

    def __init__(self, environment, storage_system):
        """Initialize this storage system snapshot.

        :param storage_system: The associated storage system.
        :type storage_system: ultrastorage.storagesystem.StorageSystem

        """
        self._timestamp = environment.now
        self._storage_unit_snapshots = [storage_unit.snapshot()
                                        for storage_unit in storage_system]

    @property
    def timestamp(self):
        """Return the timestamp of this storage system snapshot.
        """
        return self._timestamp

    @property
    def storage_unit_snapshots(self):
        """Return the storage unit snapshots of this storage system snapshot.

        """
        return self._storage_unit_snapshots

    def __len__(self):
        """Return the number of storage units in this storage system snapshot.

        """
        return len(self.storage_unit_snapshots)

    def __str__(self):
        """Stringify this storage system snapshot.

        """
        return "(timestamp={},".format(self.timestamp) + \
               "(" + \
               ",".join([str(storage_unit_snapshot) for storage_unit_snapshot in self]) + \
               "))"

    def __getitem__(self, storage_unit_snapshot_index):
        """Access the storage unit snapshot by index.

        """
        return self.storage_unit_snapshots[storage_unit_snapshot_index]

    def storage_unit_snapshot_by_index(self, storage_unit_snapshot_index):
        """Access the storage unit snapshot by index.
        """
        return self[storage_unit_snapshot_index]

    def storage_unit_snapshot_by_name(self, storage_unit_name):
        """Access the storage unit snapshot by storage_unit_snapshot_by_name.

        """
        return next(storage_unit_snapshot
                    for storage_unit_snapshot in self.storage_unit_snapshots
                    if storage_unit_snapshot.storage_unit_name() == storage_unit_name)

    def __iter__(self):
        """Iterate over all storage unit snapshots of this storage system snapshot.
        """
        return iter(self.storage_unit_snapshots)
