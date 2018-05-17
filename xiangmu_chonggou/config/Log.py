#encoding=utf-8
import os,time
import logging.config
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logging.config.fileConfig(parentDirPath + u"\config\Logger.conf")
#选择一个日志格式
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
logger = logging.getLogger(nowtime)
LOG_FILE_PATH = parentDirPath+'\\log\\myapp.log'
fileHandler = logging.FileHandler(LOG_FILE_PATH)
fmt = '\n' + '%(asctime)s - %(filename)s:%(lineno)s  - %(message)s'
# fmt = '\n' + '%(asctime)s - %(filename)s:%(lineno)s  - %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.NOTSET)


def debug(message):
    #定义debug级别日志打印方法
    logger.debug(message)

def info(message):
    # 定义info级别日志打印方法
    logger.info(message)
def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)

