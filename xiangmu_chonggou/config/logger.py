import logging
import os
# 使用logging模块：
class CLog:
    # ----------------------------------------------------------------------------
    def __init__(self):
        parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 日志文件的存放路径，根据自己的需要去修改
        LOG_FILE_PATH = parentDirPath+'\\log\\myapp.log'
        self.logger = logging.getLogger()
        fileHandler = logging.FileHandler(LOG_FILE_PATH)
        # 日志的输出格式
        fmt = '\n' + '%(asctime)s - %(filename)s:%(lineno)s  - %(message)s'
        formatter = logging.Formatter(fmt)  # 实例化formatter
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.NOTSET)


    def debug(self,message):
        # 定义debug级别日志打印方法
        self.logger.debug(message)

    def info(self,message):
        # 定义info级别日志打印方法
        self.logger.info(message)

    def warning(self,message):
        # 定义warning级别日志打印方法
        self.logger.warning(message)



