# Yahoo! Cloud System Benchmark
# Workload A: Update heavy workload
#   Application example: Session store recording recent actions
#                        
#   Read/update ratio: 50/50
#   Default data size: 1 KB records (10 fields, 100 bytes each, plus key)
#   Request distribution: zipfian

#10GB 1KB value

recordcount=26214400
#operationcount=26214400
operationcount=78643200
workload=com.yahoo.ycsb.workloads.CoreWorkload

readallfields=true

readproportion=0
updateproportion=1.0
scanproportion=0
insertproportion=0

fieldlength=4072
requestdistribution=zipfian
scanlengthdistribution=constant
maxscanlength=1000

