# encoding:utf-8

import time

import Parameter
from FileUtils import FileUtils


if __name__ == "__main__":

    fileUtils = FileUtils()
    srcpath = "H:\\channel\\"  # 母包存放地址
    despath = fileUtils.getChannelApkPath(str(srcpath) + 'channelApk') + '\\'  # 渠道包存放地址

    fileUtils.storeOriginFileName(srcpath,'.apk')

    fileUtils.changeFileSuffix(srcpath,despath,'.apk','.zip')
    fileUtils.decodeZipFile(despath,fileUtils.getApkAllFileName())
    fileUtils.deleteMETA_INF(despath + fileUtils.prefixName)

    for i in Parameter.channelList:
        Parameter.channel = 'bcbuy_'+ i + Parameter.Version+Parameter.resVersion + time.strftime("%y%m%d_%H%M", time.localtime())
        print('正在开始重打包:'+Parameter.channel)

        fileUtils.replaceEXCFG(srcpath + i ,despath + fileUtils.getApkOriginfixName())

        fileUtils.encodeZipFile(despath + fileUtils.getApkOriginfixName(),despath + fileUtils.getApkOriginfixName()+'.zip')
        fileUtils.changeFileSuffix(despath,despath,'.zip','.apk')
        fileUtils.resignedApk(despath ,despath+'resignedApk', fileUtils.getApkAllFileName(),fileUtils.getApkOriginfixName()+'_signed.apk')