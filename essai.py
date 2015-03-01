# from binreconfiguration.bin import UnitBin
# from binreconfiguration.storageunit import StorageUnit
from binreconfiguration.simulator.nonreconfigurable import Overflow
from binreconfiguration.strategy import RandomFit
from binreconfiguration.strategy import FirstFit
from binreconfiguration.strategy import BestLoadFit
from binreconfiguration.strategy import WorstLoadFit
from binreconfiguration.strategy import BestCountFit
from binreconfiguration.strategy import WorstCountFit
from binreconfiguration.strategy import BestFreeSpaceFit
from binreconfiguration.strategy import WorstFreeSpaceFit
from binreconfiguration.strategy import BestAverageItemSizeFit
from binreconfiguration.strategy import WorstAverageItemSizeFit
from binreconfiguration.storageunit import SnapshotReporter

# item size generator
def items():
	import random
	while True:
		yield random.random()

# overflow simulator
s = Overflow(100, 1)

# run the simulator till overflow
snapshots = s.run(WorstLoadFit, items)

# display the snapshots
# for (index, snapshot) in enumerate(snapshots):
# 	print("{} {}\n".format(index+1, str(snapshot)))

snapshot_reporter = SnapshotReporter(snapshots)
print("average load = {}".format(snapshot_reporter.average('load')[-1]))
print("average size = {}".format(snapshot_reporter.average('size')[-1]))
print("average count = {}".format(snapshot_reporter.average('count')[-1]))

