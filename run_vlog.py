import funcs
import sys
import os

dbPath = "/mnt/vlog/"
#valueSizes = ["128B","256B","512B","1KB","2KB","3KB","4KB"]
valueSizes = ["8KB"]
dbSize = "40GB"
for valueSize in valueSizes:
    dbfilename = dbPath+"leveldb_vlog"+valueSize+dbSize
    #vlogfilename = "/mnt/expdb/vlogs"
    vlogfilename = dbfilename+"/vlogs"
    workload = "./workloads/workload"+valueSize+dbSize+".spec"
    #gcSize = 10*1024*1024*1024
    gcSize = 0
    memtable = 64
    resultfile = "./resultDir/vlog"+valueSize+dbSize+"memtable"+str(memtable)

    configs = {
        "bloomBits":"10",
        "seekCompaction":"false",
        "directIO":"false",
        "compression":"false",
        "blockCache":str(64*1024*1024),
        "gcSize":str(gcSize),
        "memtable":str(memtable*1024*1024),
        "noCompaction":"true",
    }

    vlogs = {
        "vlogFilename":vlogfilename,
        "scanThreads":"1",
    }
    
    phase = sys.argv[1]

    os.system("sync && echo 3 > /proc/sys/vm/drop_caches")
    os.system("ulimit -n 50000")
    print(workload)
    print(vlogfilename)
    print(dbfilename)
    if phase == "load":
        configs["gcSize"] = "0"
    for cfg in configs:
        funcs.modifyConfig("./configDir/leveldb_config.ini","config",cfg,configs[cfg])
    for vlog in vlogs:
        funcs.modifyConfig("./configDir/leveldb_config.ini","vlog",vlog,vlogs[vlog])

    if len(sys.argv) == 3:
        resultfile = sys.argv[2]

    if phase=="load":
        os.system("rm -rf {0}".format(vlogs["vlogFilename"]))
        resultfile = resultfile+"_load"
        funcs.load("vlog",dbfilename,workload,resultfile)

    if phase=="run":
        os.system("sync && echo 3 > /proc/sys/vm/drop_caches")
        resultfile = resultfile+"_run"
        funcs.run("vlog",dbfilename,workload,resultfile)

    if phase =="both":
        os.system("rm -rf {0}".format(vlogfilename))
        resultfile1 = resultfile+"_load"
        funcs.load("vlog",dbfilename,workload,resultfile1)
        resultfile2 = resultfile+"_run"
        funcs.run("vlog",dbfilename,workload,resultfile2)
