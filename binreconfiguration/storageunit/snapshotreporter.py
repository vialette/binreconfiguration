"""Storage unit snapshots easy reporter"""

class SnapshotReporter(object):

	class RowReporter(object):

		def __init__(self, storage_unit_snapshot):
			self._report = {}
			for bin_snapshot in storage_unit_snapshot:
				for key in bin_snapshot:
					if key != 'name' and key != 'capacity':
						if key not in self._report:
							self._report[key] = {}
						if 'values' not in self._report[key]:
							self._report[key]['values'] = []
						self._report[key]['values'].append(bin_snapshot[key])

			for key in self._report:
				n = len(self._report[key]['values'])
				self._report[key]['min'] = min(self._report[key]['values'])
				self._report[key]['average'] = float(sum(self._report[key]['values'])) / float(n)
				self._report[key]['max'] = max(self._report[key]['values'])

		def __getitem__(self, key):
			return self._report[key]

		def values(self, key):
			return self[key]['values']

		def min(self, key):
			return self[key]['min']

		def average(self, key):
			return self[key]['average']

		def max(self, key):
			return self[key]['max']

	def __init__(self, storage_unit_snapshots):
		self._rows = [SnapshotReporter.RowReporter(storage_unit_snapshot) 
					  for storage_unit_snapshot in storage_unit_snapshots]

	def values(self, key):
		return [row.values(key) for row in self._rows]

	def min(self, key):
		return [row.min(key) for row in self._rows]

	def average(self, key):
		return [row.average(key) for row in self._rows]

	def max(self, key):
		return [row.max(key) for row in self._rows]

	def last(self):
		return self._rows[-1]

	def last_values(self, key):
		return self._rows[-1].values(key)

	def last_min(self, key):
		return self._rows[-1].min(key)

	def last_average(self, key):
		return self._rows[-1].average(key)

	def last_max(self, key):
		return self._rows[-1].max(key)
