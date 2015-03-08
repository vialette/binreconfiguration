"""Snapshot manager"""

class SnapshotController(object):

	SUSPENDED = 0
	RUNNING   = 1

	def __init__(self):
		self._snapshots = []
		self._state     = self.RUNNING

	def append(slef, snapshot):
		if self._state == self.RUNNING:
			self._snapshots.append(snapshot)

	def add(self, snapshot):
		self.append(snapshot)

	def snapshots(self):
		return self._snapshots

	def suspend(self):
		self._state = self.SUSPENDED

	def run(self):
		self._state = self.RUNNING

	def clean(self):
		self._snapshots = []

	def last(self):
		return self._snapshots[-1]

	def __len__(self):
		return len(self._snapshots)

	def state(self):
		return self._state
