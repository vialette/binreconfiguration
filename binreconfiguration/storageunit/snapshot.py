"""Storage unit snapshot"""

class Snapshot(object):
  def __init__(self, storage_unit):
    self._bin_snapshots = dict([(bin.name(), bin.snapshot()) for bin in storage_unit])

  def __str__(self):
    return '(' + self._str_aux() + ')'

  def _str_aux(self):
    return ','.join(["{}={}".format(bin_name, str(self._bin_snapshots[bin_name]))
                     for bin_name in sorted(self._bin_snapshots)])

  def __getitem__(self, bin_name):
    return self._bin_snapshots[bin_name]

  def __iter__(self):
    return oter(self._bin_snapshots)
