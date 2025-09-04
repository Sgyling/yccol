from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QTextEdit, QFrame, QApplication, QMessageBox, QMainWindow, QMenuBar, QMenu, QAction
from PyQt5.QtCore import Qt
import socket
from PyQt5.QtGui import QIcon, QMouseEvent

class SecondWindow(QMainWindow):

    def __init__(self, key, timea):
        super().__init__()
        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowTitle("Fifa0 - PRO - GUI(正式GUI版本)")
        self.setFixedSize(700, 700)
        # 设置无边框窗口
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 设置窗口整体背景颜色为深色
        self.setStyleSheet("""
            background-color: #121212;
            color: #B0B0B0;
            font-family: 'Arial', sans-serif;
        """)

        # 整体垂直布局
        main_layout = QVBoxLayout()

        # 标题栏布局
        title_bar = QWidget()
        title_bar.setStyleSheet("""
            background-color: #1C1C1C;
            padding: 5px;
        """)
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(0, 0, 0, 0)

        # 标题标签
        title_label = QLabel("Yccol - GUI(代理池获取和验证工具 V0.0.1) by : 杨CC", self)
        title_label.setStyleSheet("""
            font-size: 22px;
            color: #00B0FF;
            padding: 5px;
        """)
        title_layout.addWidget(title_label)

        # 关闭按钮
        close_button = QPushButton("X", self)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #E74C3C;
                font-size: 20px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #C0392B;
                border-radius: 5px;
            }
        """)
        close_button.clicked.connect(self.close)
        title_layout.addWidget(close_button)

        main_layout.addWidget(title_bar)

        # 创建菜单栏
        menubar = QMenuBar()
        menubar.setStyleSheet("""
            background-color: #2C2C2C;
            color: #B0B0B0;
            font-size: 14px;
        """)

        # 文件菜单
        file_menu = menubar.addMenu('文件')
        exit_action = QAction('退出', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # http相关菜单
        http_menu = menubar.addMenu('http(当前界面)')

        # socks4菜单
        socks4_menu = menubar.addMenu('socks4(暂不可用)')

        # socks5菜单
        socks5_menu = menubar.addMenu('socks5(暂不可用)')

        # 关于菜单
        about_menu = menubar.addMenu('关于')
        about_action = QAction('关于Yccol', self)
        about_action.triggered.connect(self.show_about_dialog)
        about_menu.addAction(about_action)

        main_layout.addWidget(menubar)

        central_widget = QWidget()
        content_layout = QVBoxLayout(central_widget)

        computer_name = socket.gethostname()
        # 创建一个水平布局来放置 key 和 timea
        top_layout = QHBoxLayout()
        # 创建 key 和 timea 的标签
        self.key_label = QLabel(f"欢迎回来: {computer_name}", self)
        self.key_label.setStyleSheet("""
            font-size: 18px;
            color: #00B0FF;
        """)
        self.timea_label = QLabel(f"结束时间: {timea}", self)
        self.timea_label.setStyleSheet("""
            font-size: 18px;
            color: #00B0FF;
        """)

        # 添加左侧内容（key）
        top_layout.addWidget(self.key_label)

        # 添加右侧内容（timea），并将其放置在右边
        top_layout.addStretch(1)  # 在 key 和 timea 之间插入一个伸缩项，使 timea 位于右侧
        top_layout.addWidget(self.timea_label)
        # 将水平布局添加到主布局中
        content_layout.addLayout(top_layout)

        # 创建文本框
        self.text_huoqu = QTextEdit(self)
        # 设置文本框高度为 480 像素
        self.text_huoqu.setFixedHeight(460)
        # 设置文本框样式
        self.text_huoqu.setStyleSheet("""
            QTextEdit {
                padding: 8px;
                font-size: 14px;
                border: 1px solid #2980B9;
                border-radius: 8px;
                background-color: #1C1C1C;
                color: #B0B0B0;
                transition: border-color 0.3s, box-shadow 0.3s;
            }
            QTextEdit:focus {
                border-color: #3498DB;
                box-shadow: 0 0 8px rgba(41, 128, 185, 0.6);
            }
        """)
        # 将文本框添加到布局中
        content_layout.addWidget(self.text_huoqu)

        # 创建按钮
        self.button_huoqu = QPushButton("获取ip池", self)
        # 设置按钮样式
        self.button_huoqu.setStyleSheet("""
            QPushButton {
                background-color: #2980B9;
                border: none;
                color: #B0B0B0;
                padding: 12px 24px;
                font-size: 16px;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
            }
            QPushButton:hover {
                background-color: #3498DB;
            }
            QPushButton:pressed {
                background-color: #21618C;
                transform: scale(0.98);
            }
        """)
        # 将按钮添加到布局中
        content_layout.addWidget(self.button_huoqu)

        # 创建验证按钮
        self.button_yanzheng = QPushButton("验证ip池", self)
        # 设置按钮样式
        self.button_yanzheng.setStyleSheet("""
            QPushButton {
                background-color: #2980B9;
                border: none;
                color: #B0B0B0;
                padding: 12px 24px;
                font-size: 16px;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
            }
            QPushButton:hover {
                background-color: #3498DB;
            }
            QPushButton:pressed {
                background-color: #21618C;
                transform: scale(0.98);
            }
        """)
        # 将按钮添加到布局中
        content_layout.addWidget(self.button_yanzheng)
        # 连接按钮的 clicked 信号到自定义的槽函数
        self.button_huoqu.clicked.connect(lambda: self.get_http_ip(key))
        self.button_yanzheng.clicked.connect(lambda: self.get_http_yanzheng())

        main_layout.addWidget(central_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 记录鼠标按下的位置，用于窗口拖动
        self.draggable = True
        self.dragging = False
        self.offset = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.draggable:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    # 按钮功能实现
    def get_http_ip(self, key):
        from get_response.get_ip_API import get_ip_1
        print(key)
        proxies_text, shuliang = get_ip_1(key)
        self.text_huoqu.setPlainText(proxies_text)

        if shuliang:
            # 创建一个消息框来显示代理个数信息
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("代理个数信息")
            msg_box.setText(f"获取代理成功,代理个数: {shuliang}")
            msg_box.exec_()
        else:
            # 创建一个消息框来显示代理个数信息
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("错误")
            msg_box.setText(f"未获取到代理详细信息")
            msg_box.exec_()

    # 验证功能
    def get_http_yanzheng(self):
        from get_response.http_yanzheng import main_yanzheng
        text_data = self.text_huoqu.toPlainText()
        a = main_yanzheng(text_data)
        if isinstance(a, list):
            # 将列表转换为字符串，每个代理占一行
            property_text = '\n'.join(a)
        elif isinstance(a, str):
            property_text = a
        else:
            property_text = "未知的错误,请联系开发者杨CC"
        self.text_huoqu.setPlainText(property_text)

        if property_text:
            # 创建一个消息框来显示代理个数信息
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("验证成功")
            msg_box.setText(f"验证成功")
            msg_box.exec_()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("验证失败")
            msg_box.setText(f"验证失败")
            msg_box.exec_()

    def show_about_dialog(self):
        QMessageBox.information(self, "关于Yccol", "---------------------------------------------------\n杨CC所编写的代理池获取和验证工具。\n\n当前版本号:V0.0.1\n---------------------------------------------------\n服务器每两个小时抓取一次最新的ip")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SecondWindow("key", "timea")
    window.show()
    sys.exit(app.exec_())
