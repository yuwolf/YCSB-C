//
// Created by wujy on 11/3/18.
//

#ifndef YCSB_C_LEVELDB_CONFIG_H
#define YCSB_C_LEVELDB_CONFIG_H


#include "leveldb/db.h"
#include "core/db.h"
#include <string>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/ini_parser.hpp>

using std::string;

namespace ycsbc {
    class ConfigLevelDB {
    private:
        boost::property_tree::ptree pt_;
        int bloomBits_;
        bool seekCompaction_;
        bool compression_;
        bool directIO_;
        bool noCompaction_;
        int numThreads_;
        int sizeRatio_;
        size_t blockCache_;
        size_t gcSize_;
        size_t memtable_;
        size_t smallThresh_;
        size_t midThresh_;

    public:
        ConfigLevelDB() {
            boost::property_tree::ini_parser::read_ini("./configDir/leveldb_config.ini", pt_);
            bloomBits_ = pt_.get<int>("config.bloomBits");
            seekCompaction_ = pt_.get<bool>("config.seekCompaction");
            compression_ = pt_.get<bool>("config.compression");
            directIO_ = pt_.get<bool>("config.directIO");
            blockCache_ = pt_.get<size_t>("config.blockCache");
            sizeRatio_ = pt_.get<int>("config.sizeRatio");
            gcSize_ = pt_.get<size_t>("config.gcSize");
            memtable_ = pt_.get<size_t>("config.memtable");
            noCompaction_ = pt_.get<bool>("config.noCompaction");
            numThreads_ = pt_.get<int>("config.numThreads");
            smallThresh_ = pt_.get<size_t>("config.smallThresh");
            midThresh_ = pt_.get<size_t >("config.midThresh");
        }

        int getBloomBits() {
            return bloomBits_;
        }

        bool getSeekCompaction() {
            return seekCompaction_;
        }

        bool getCompression() {
            return compression_;
        }

        bool getDirectIO() {
            return directIO_;
        }

        int getNumThreads(){
            return numThreads_;
        }

        size_t getBlockCache() {
            return blockCache_;
        }

        int getSizeRatio() {
            return sizeRatio_;
        }

        size_t getGcSize(){
            return gcSize_;
        }

        size_t getMemtable(){
            return memtable_;
        }

        bool getNoCompaction(){
            return noCompaction_;
        }

        size_t getSmallThresh(){
            return smallThresh_;
        }

        size_t getMidThresh(){
            return midThresh_;
        }
    };
}

#endif //YCSB_C_LEVELDB_DB_H
