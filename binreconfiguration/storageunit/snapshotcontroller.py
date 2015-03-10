"""Snapshot manager"""

class SnapshotController(object):

	SUSPENDED = 0
	RUNNING   = 1

	def __init__(self):
		self._snapshots = []
		self._state     = self.RUNNING

	def append(self, snapshot):
		"""Append a new storage unit snapshot."""
		if self._state == self.RUNNING:
			self._snapshots.append(snapshot)

	def add(self, snapshot):
		"""Alias"""
		self.append(snapshot)

	def snapshots(self):
		"""Return the list of all strorage unit snapshots."""
		return self._snapshots

	def suspend(self):
		"""Suspend the storage unit snapshot controller."""
		self._state = self.SUSPENDED

	def run(self):
		"""Restart the storage unit snapshot controller."""
		self._state = self.RUNNING

	def clean(self):
		"""Delete all controlled storage unit snapshots."""
		self._snapshots = []

	def last(self):
		"""Return the last controlled storage unit snapshot."""
		return self._snapshots[-1]

	def __len__(self):
		"""Return the the number controlled storage unit snapshots.""" 
		return len(self._snapshots)

	def __iter__(self):
		"""Iterate over storage unit snapshots."""
		return iter(self._snapshots)

	def state(self):
		return self._state
