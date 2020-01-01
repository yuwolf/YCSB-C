import funcs
import sys
import os

dbPath = "/mnt/expdb/"
disk = "/dev/md0"
#dbPath = "/mnt/raidstore/"
valueSizes = ["1KB"]
maxSortedRuns = [1,5,10,15,20]
dbSize = "300GB"
smallThresh = 64
midThresh = 30000
for msr in maxSortedRuns:
    os.system("umount {0}".format(disk))
    os.system("mkfs.ext4 -b 4096 -E stride=128,stripe-width=512 {0} -F".format(disk))
    os.system("mount {0} {1}".format(disk, dbPath))
    for valueSize in valueSizes:
        dbfilename = dbPath+"titandb_vtablenolarge"+valueSize+dbSize
        workload = "./workloads/workload"+valueSize+dbSize+".spec"
        memtable = 64
        threads = 8
        gcThreads = 2
        resultfile = "./resultDir/vtablenolarge"+valueSize+dbSize+"memtable"+str(memtable)+"threads"+str(threads)+"gc"+str(gcThreads)+"sortedrun"+str(msr)
        sepBeforeFlush = "false"
        if sepBeforeFlush == "true":
            resultfile = resultfile + "before"


        configs = {
            "bloomBits":"10",
            "seekCompaction":"false",
            "directIO":"false",
            "compression":"false",
            "noCompaction":"false",
            "blockCache":str(8*1024*1024),
            "memtable":str(memtable*1024*1024),
            "numThreads":str(threads),
            "gcThreads":str(gcThreads),
            "tiered":"false",
            "levelMerge":"true",
            "rangeMerge":"true",
            "sepBeforeFlush":sepBeforeFlush,
            "midThresh":str(midThresh),
            "smallThresh":str(smallThresh),
            "maxSortedRuns":str(msr),
        }

        phase = sys.argv[1]

        if __name__ == '__main__':
            #set configs
            os.system("sync && echo 3 > /proc/sys/vm/drop_caches")

            if phase=="load":
                configs["noCompaction"] = "false"

            for cfg in configs:
                funcs.modifyConfig("./configDir/leveldb_config.ini","config",cfg,configs[cfg])

            for cfg in configs:
                funcs.modifyConfig("./configDir/leveldb_config.ini","config",cfg,configs[cfg])

            if len(sys.argv) == 3:
                resultfile = sys.argv[2]

            if phase=="load":
                resultfile = resultfile+"_load"
                funcs.load("titandb",dbfilename,workload,resultfile)
                os.system("du -sh {0} >> db_size && date >> db_size".format(dbfilename))

            if phase=="run":
                resultfile = resultfile+"_run"
                print(resultfile)
                funcs.run("titandb",dbfilename,workload,resultfile)

            if phase=="both":
                resultfile1 = resultfile+"_both"
                funcs.both("titandb",dbfilename,workload,resultfile1)
                os.system("du -sh {0} >> db_size && date >> db_size".format(dbfilename))

                workloads = ["20scan","100scan","1000scan","10000scan","zipf20scan","zipf100scan","zipf1000scan","zipf10000scan"]
                for wl in workloads:
                    for i in range (1,10):
                        workload = "./workloads/workload"+valueSize+wl+dbSize+".spec"
                        resultfile1 = "./resultDir/vtablenolarge"+valueSize+wl+dbSize+"memtable"+str(memtable)+"threads"+str(threads)+"gc"+str(gcThreads)+"sortedrun"+str(msr)+"round"+str(i)
                        funcs.run("titandb",dbfilename,workload,resultfile1)