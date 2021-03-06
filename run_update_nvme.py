import sys
import os

disks = {"vtable":"/dev/nvme0n1p1","titandb":"/dev/nvme0n1p1","rocksdb":"/dev/nvme0n1p1","vtablenolarge":"/dev/nvme0n1p1","vtablenomid":"/dev/nvme0n1p1"}
paths = {"vtable":"/mnt/expdb","titandb":"/mnt/titan","rocksdb":"/mnt/rocksdb","vtablenolarge":"/mnt/expdb","vtablenomid":"/mnt/expdb"}
backupPath = "/mnt/backup/"

for db,disk in disks.items():
    os.system("umount {0}".format(disk))
    os.system("mkfs.ext4 {0} -F".format(disk))
    os.system("mount {0} {1}".format(disk, paths[db]))
    os.system("python run_{0}.py both".format(db))