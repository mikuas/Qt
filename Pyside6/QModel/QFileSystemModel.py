# coding:utf-8

import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileSystemModel
from PySide6.QtCore import Qt, QDir


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.fileModel = QFileSystemModel(self)
        
        # 设置模型根路径
        self.fileModel.setRootPath('C:\\')
        
        # 设置路径,名称过滤器
        self.fileModel.setFilter(QDir.Filter.AllEntries | QDir.NoDotAndDotDot | QDir.Files)
        self.fileModel.setNameFilters(['*.py', '*.txt'])
        
        # 设置文件系统模型参数
        self.fileModel.setOption(QFileSystemModel.Option.DontWatchForChanges, True)
        
        # 设置是否是只读的
        self.fileModel.setReadOnly(False)
        
        # 获取文件信息
        print(self.fileModel.fileInfo(self.fileModel.index('C:\\write.py')))
        
        # 获取文件图标
        print(self.fileModel.fileIcon(self.fileModel.index("C:\\write.py")))
        
        # 获取文件名, 获取路径和文件名
        print(self.fileModel.fileName(self.fileModel.index('C:\\write.py')))
        print(self.fileModel.filePath(self.fileModel.index('C:\\write.py')))
        
        # 获取表头数据
        print(self.fileModel.headerData(0, Qt.Orientation.Horizontal))
        
        # 获取是否有子目录或文件
        print(self.fileModel.hasChildren(self.fileModel.index('C:\\')))
        
        # 获取是否是路径
        print(self.fileModel.isDir(self.fileModel.index('C:\\write.py')))
        # 获取最后修改时间
        print(self.fileModel.lastModified(self.fileModel.index('C:\\write.py')).toString("yyyy-MM-dd hh:mm:ss"))
        
        # 创建目录, 并返回指向该目录的模型数据索引
        print(self.fileModel.mkdir(self.fileModel.index('C:\\'), 'test'))
        
        # 删除文件或目录,成功返回True
        print(self.fileModel.remove(self.fileModel.index('C:\\test')))
        
        # 返回根目录Dir
        print(self.fileModel.rootDirectory())
        
        # 返回根路径
        print(self.fileModel.rootPath())
        
        # 返回目录下文件数量
        print(self.fileModel.rowCount())
        
        # self.fileModel.sibling()
        
        # 返回路径或文件类型
        print(self.fileModel.type(self.fileModel.index('C:\\write.py')))
        
        # 获取文件大小
        print(self.fileModel.size(self.fileModel.index('C:\\write.py')))

        # 获取父索引下的列数
        print(self.fileModel.columnCount())
        
        # self.fileModel.directoryLoaded
        # self.fileModel.rootPathChanged
        # self.fileModel.fileRenamed
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 520)
    window.show()
    sys.exit(app.exec())