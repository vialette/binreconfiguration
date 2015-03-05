# a non-reconfigurable simulation that always goes to overflow
from binreconfiguration.simulator.nonreconfigurable import Overflow
from binreconfiguration.simulator.repeater import Repeater

# the strategy we are going to use (FirstFit consider the bins always in the same
# order and select the first with enough room to accomodate a given item)
from binreconfiguration.strategy import FirstFit

# other strategies include
# from binreconfiguration.strategy import RandomFit
# from binreconfiguration.strategy import MinLoad
# from binreconfiguration.strategy import MaxLoad
# from binreconfiguration.strategy import MinCount
# from binreconfiguration.strategy import MaxCount
# from binreconfiguration.strategy import MinFreeSpace
# from binreconfiguration.strategy import MinFreeSpace
# from binreconfiguration.strategy import MinAverageItemSize
# from binreconfiguration.strategy import MaxAverageItemSize

# a SnapshortReport is a convenient objet for reporting the simulation
from binreconfiguration.storageunit import SnapshotReporter

# Bin object
from binreconfiguration.item import Item

# Item generator
from binreconfiguration.itemgenerator import Uniform

# our item  generator
generator = Uniform()

# overflow simulator: 5 bins, each of unit size
number_of_bins = 2
capacity       = 1.
simulator = Overflow(number_of_bins, capacity)

# run the simulator till overflow using the FirstFir strategy. 
# The simulator gracefully intercepts the overflow exception.
snapshots = simulator.run(FirstFit, generator)

# we are now ready to read/report/analyse the results of the simulation

# some vocabulary
#  - storage unit: a collection of bins of equal capacity
#  - snapshot: a detailled picture of a storage unit
#  - snapshots: in our context, a sequence of pictures of a storage unit (each picture
#               is taken after adding an element since we are using a non-reconfigurable 
#               storage unit)
#  - snapshot_reporter: an object for easy access to the snapshots.

# raw data first. 
# we display the snapshots, and each snapshot is actually a snapshot of a bin.
for (index, snapshot) in enumerate(snapshots):
	print("{} {}\n\n".format(index+1, str(snapshot)))

# done with raw data, let's use a reporter for easy access.
snapshot_reporter = SnapshotReporter(snapshots)

# Full report of the simutation
#  - report the sizes (i.e. number of items) of the bins at each step
#  - report the loads (i.e. size / capacity) of the bins at each step
#  - report the number of items in the bins at each iteration
print("Full report")
print("bin size:")
for i, sizes in enumerate(snapshot_reporter.values('size')):
	print("#{}: {}".format(i+1, sizes))
print("bin load:")
for i, loads in enumerate(snapshot_reporter.values('load')):
	print("#{}: {}".format(i+1, loads))
print("bin count")
for i, counts in enumerate(snapshot_reporter.values('count')):
	print("#{}: {}".format(i+1, counts))
print("\n")

# Average report of the simulation
#  - report the average size of the bins at each step
#  - report the average load of the bins at each step
#  - report the average count of the bins at each step 
print("Average")
print("average size")
for i, size in enumerate(snapshot_reporter.average('size')):
	print("#{}: {}".format(i+1, size))
print("average load")
for i, load in enumerate(snapshot_reporter.average('load')):
	print("#{}: {}".format(i+1, load))
print("average count")
for i, count in enumerate(snapshot_reporter.average('count')):
	print("#{}: {}".format(i+1, count))
print("\n")

# Min report of the simulation
#  - report the min size of the bins at each step
#  - report the min load of the bins at each step
#  - report the min count of the bins at each step 
print("Min")
print("min size")
for i, size in enumerate(snapshot_reporter.min('size')):
	print("#{}: {}".format(i+1, size))
print("min load")
for i, load in enumerate(snapshot_reporter.min('load')):
	print("#{}: {}".format(i+1, load))
print("min count")
for i, count in enumerate(snapshot_reporter.min('count')):
	print("#{}: {}".format(i+1, count))
print("\n")

# Max report of the simulation
#  - report the max size of the bins at each step
#  - report the max load of the bins at each step
#  - report the max count of the bins at each step 
print("Max")
print("max size")
for i, size in enumerate(snapshot_reporter.max('size')):
	print("#{}: {}".format(i+1, size))
print("max load")
for i, load in enumerate(snapshot_reporter.max('load')):
	print("#{}: {}".format(i+1, load))
print("max count")
for i, count in enumerate(snapshot_reporter.max('count')):
	print("#{}: {}".format(i+1, count))
print("\n")

# Report last step of the simulation
print("Last configuration report")
print("average size = {}".format(snapshot_reporter.average('size')[-1]))
print("average load = {}".format(snapshot_reporter.average('load')[-1]))
print("average count = {}".format(snapshot_reporter.average('count')[-1]))
print("min size = {}".format(snapshot_reporter.min('size')[-1]))
print("min load = {}".format(snapshot_reporter.min('load')[-1]))
print("min count = {}".format(snapshot_reporter.min('count')[-1]))
print("max size = {}".format(snapshot_reporter.max('size')[-1]))
print("max load = {}".format(snapshot_reporter.max('load')[-1]))
print("max count = {}".format(snapshot_reporter.max('count')[-1]))
print("\n")

# The library provides convenient last_* methods for accessing the last step of the simulation
print("Last configuration report")
print("average size = {}".format(snapshot_reporter.last_average('size')))
print("average load = {}".format(snapshot_reporter.last_average('load')))
print("average count = {}".format(snapshot_reporter.last_average('count')))
print("min size = {}".format(snapshot_reporter.last_min('size')))
print("min load = {}".format(snapshot_reporter.last_min('load')))
print("min count = {}".format(snapshot_reporter.last_min('count')))
print("max size = {}".format(snapshot_reporter.last_max('size')))
print("max load = {}".format(snapshot_reporter.last_max('load')))
print("max count = {}".format(snapshot_reporter.last_max('count')))
print("\n")

repeater = Repeater(simulator, FirstFit, generator, 2)
