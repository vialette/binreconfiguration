from binreconfiguration.bin import UnitBin
from binreconfiguration.storageunit import SnapshotedStorageUnit
from binreconfiguration.simulator.nonreconfigurable import Overflow
from binreconfiguration.strategy import FirstFit
from binreconfiguration.strategy import RandomFit
from binreconfiguration.strategy import BestLoadFit
from binreconfiguration.strategy import WorstLoadFit
from binreconfiguration.strategy import BestCountFit
from binreconfiguration.strategy import WorstCountFit
from binreconfiguration.strategy import BestFreeSpaceFit
from binreconfiguration.strategy import WorstFreeSpaceFit
from binreconfiguration.strategy import BestAverageItemSizeFit
from binreconfiguration.strategy import WorstAverageItemSizeFit

def items():
	import random
	while True:
		yield random.random() / 10

s = Overflow(2, 1)

snapshots = s.run(BestLoadFit, items)
for (index, snapshot) in enumerate(snapshots):
	print("{} {}".format(index+1, snapshot))

# snapshots = s.run(WorstLoadFit, items)
# for (index, snapshot) in enumerate(snapshots):
# 	print("{} {}".format(index+1, snapshot))
