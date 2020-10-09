# encoding:utf-8
#判断文件存不存在
import os
import zipfile
import shutil

import Parameter


class FileUtils:

    # 判断文件是否存在如果不存在就创建该文件
    def isFolderExist(self,path):
        if not os.path.exists(path):
            os.makedirs(path)
            pass
        pass

    def getChannelApkPath(self,path):
        self.isFolderExist(path)
        return path

    # 解压zip文件
    def decodeZipFile(self,path,zipFileName):
        r = zipfile.is_zipfile(path+zipFileName)
        if r:
            fz = zipfile.ZipFile(path+zipFileName, 'r')
            self.isFolderExist(path + self.prefixName)
            fz.extractall(path + self.prefixName)
        else:
            print('This is not zip file.')
        # self.deleteMETA_INF(path + self.prefixName)

    #删除META-INF文件夹
    def deleteMETA_INF(self,path):
        if os.path.exists(path+'\\'+'META-INF'):
            shutil.rmtree(path+'\\'+'META-INF')

    #将文件压缩成zip文件
    def encodeZipFile(self,dirname,zipfilename):
        filelist = []
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else:
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root, name))

        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(dirname):]
            zf.write(tar, arcname)
        zf.close()


     #更换EXCFG文件
    def replaceEXCFG(self ,srcpath,despath):

        if os.path.exists(despath +'\\'+'assets\\EXCFG'):
            os.remove(despath +'\\'+'assets\\EXCFG')
            print('已删除EXCFG')
        shutil.copy(srcpath,despath +'\\'+'assets\\EXCFG')
        # f = open(srcpath)
        # lines = f.read()
        # f.close()
        # print('lines:'+lines)


    #重签名apk
    def resignedApk(self,apkFilePath,srcApkFilePath,zip_name,new_zip_name):
        self.isFolderExist(srcApkFilePath)
        # print(channel + "：签名")
        os.system(
            "jarsigner -verbose -keystore " + Parameter.keystorePath + "\\" + Parameter.keystoreFileName + " -signedjar " + apkFilePath +  new_zip_name + " " + apkFilePath + zip_name + " " + Parameter.keystoreAlias + " -storepass " + Parameter.keystoreStorepass)
        # print(Parameter.keystorePath+'\\'+Parameter.keystoreFileName)
        # print(channel + "：对齐")
        os.system(
            "zipalign -v 4 " + apkFilePath + new_zip_name + " " + srcApkFilePath+ "\\" + Parameter.channel + ".apk ")

    # python更换后缀名,并将生成的新文件放到新的目录中
    def changeFileSuffix(self, srcpath, despath, presuffix, aftersuffix):
        self.isFolderExist(despath)

        # 列出当前目录下所有的文件
        files = os.listdir(srcpath)
        print('files', files)
        for filename in files:
            portion = os.path.splitext(filename)
            if portion[1] == presuffix:
                # 重新组合文件名和后缀名
                newname = portion[0] + aftersuffix
                self.setApkPrefixName(portion[0])  # 存储apk的文件名，不包括后缀名
                filenamedir = srcpath + filename
                newnamedir = despath + newname
                shutil.copy(filenamedir, newnamedir)
                # 存储zip的文件名包括后缀名
                self.setApkAllFileName(newname)

    #存储apk最开始的文件名
    def  storeOriginFileName(self,srcpath,suffix):
        files = os.listdir(srcpath)
        print('files', files)
        for filename in files:
            portion = os.path.splitext(filename)
            if portion[1] == suffix:
                # 存储zip的文件名包括后缀名
                self.setApkOriginfixName(portion[0])


    def setApkAllFileName(self,fileName):
        self.fileName = fileName

    def getApkAllFileName(self):
        return self.fileName

    def getApkPrefixName(self):
        return self.prefixName

    def setApkPrefixName(self,prefixName):
        self.prefixName = prefixName

    def getApkOriginfixName(self):
        return self.originfixName

    def setApkOriginfixName(self, originfixName):
        self.originfixName = originfixName
