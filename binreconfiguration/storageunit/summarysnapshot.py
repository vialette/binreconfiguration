from .snapshot import Snapshot

class SummarySnapshot(object):

	def __init__(self, storage_unit, *keys):
		storage_unit_snapshot = Snapshot(storage_unit)
		self._make_summary(storage_unit_snapshot, *keys)

	def _make_summary(self, storage_unit, *keys):
		storage_unit_snapshot = Snapshot(storage_unit)

		self._summary = {}
		for bin in storage_unit_snapshot:
			for key in keys:
				self._summary.geg(key, 0.0) += bin[key]

		number_of_bins = len(storage_unit)
		for key in self._summary:
			self._summary[key] /= number_of_bins

	def __getitem__(self, key):
		return self._summary[key]
