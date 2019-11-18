# Yahoo! Cloud System Benchmark
# Workload A: Update heavy workload
#   Application example: Session store recording recent actions
#                        
#   Read/update ratio: 50/50
#   Default data size: 1 KB records (10 fields, 100 bytes each, plus key)
#   Request distribution: zipfian

#10GB 1KB value

recordcount=274989369
#recordcount=30000000
operationcount=10000
#operationcount=200000000

workload=com.yahoo.ycsb.workloads.CoreWorkload

readallfields=true

readproportion=0
updateproportion=0
scanproportion=1.0
insertproportion=0

fieldlength=4072
field_len_dist=ratio
requestdistribution=uniform
scanlengthdistribution=constant
maxscanlength=1000

largeproportion=0.1
midproportion=0.5
smallproportion=0.4
largesize=16384
midsize=1024
smallsize=100
