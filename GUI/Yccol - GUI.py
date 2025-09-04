import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
import requests
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from GUi.SecondWindow import SecondWindow  # 请确保这里引用的是你实际使用的类路径

class KeyCheckWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yccol-GUI-秘钥检测(获取代理工具V0.0.1)")  # 设置窗口标题
        self.setWindowIcon(QIcon('icon.ico'))  # 设置窗口图标
        self.setFixedSize(600, 200)  # 设置窗口大小

        # 设置深色主题
        self.setStyleSheet("""
            QWidget {
                background-color: #2E2E2E;  /* 深色背景 */
                color: #FFFFFF;  /* 白色字体 */
            }
            QLabel {
                font-size: 14px;
                color: #B0B0B0;  /* 标签文字颜色 */
            }
            QLineEdit {
                background-color: #404040;  /* 输入框背景 */
                color: #FFFFFF;  /* 输入框文字 */
                border: 1px solid #555555;  /* 边框颜色 */
                padding: 5px;
                border-radius: 4px;
            }
            QPushButton {
                background-color: #4CAF50;  /* 按钮背景颜色 */
                color: #FFFFFF;  /* 按钮文字颜色 */
                border: none;
                padding: 10px;
                border-radius: 4px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049;  /* 按钮悬停时背景颜色 */
            }
            QPushButton:pressed {
                background-color: #388E3C;  /* 按钮点击时背景颜色 */
            }
        """)

        # 创建QVBoxLayout布局管理器
        layout = QVBoxLayout()

        # 创建标签，用于提示用户输入密钥
        self.label = QLabel("请输入密钥：")
        layout.addWidget(self.label)  # 将标签添加到布局中

        # 创建一个输入框，用于输入密钥
        self.key_input = QLineEdit(self)
        self.key_input.setEchoMode(QLineEdit.Password)  # 设置输入框的回显模式为密码
        layout.addWidget(self.key_input)  # 将输入框添加到布局中

        # 创建一个按钮，点击后检测密钥
        self.check_button = QPushButton("检测密钥", self)
        self.check_button.clicked.connect(self.check_key)  # 将按钮的点击事件连接到check_key方法
        layout.addWidget(self.check_button)  # 将按钮添加到布局中

        # 创建一个标签，用于显示检测结果
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)  # 将结果标签添加到布局中

        # 设置窗口的主布局
        self.setLayout(layout)

    def check_key(self):
        # 获取输入框中的内容
        input_key = self.key_input.text()
        key_url = f'http://localhost:5000/api/key?key={input_key}'
        
        # 定义请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept': 'application/json',  # 告诉服务器返回JSON格式
        }

        print(key_url)
        try:
            # 发送Get请求,并获取相应
            yan_zheng = requests.get(key_url, headers=headers)

            # 判断是否响应成功
            if yan_zheng.status_code == 200:
                data = yan_zheng.json()

                # 判断返回数据
                if data.get('message') == '秘钥有效，数据返回成功':
                    self.result_label.setText("秘钥正确")
                    self.result_label.setStyleSheet("color: #4CAF50;")  # 设置绿色文字

                    if data.get('end_time') is not None:
                        timea = data.get('end_time')
                        self.result_label.setText(f"欢迎回家~,结束时间:{timea}")
                        self.result_label.setStyleSheet("color: #4CAF50;")  # 绿色

                        # 打开第二个窗口
                        self.second_window = SecondWindow(input_key, timea)
                        self.second_window.show()

                        # 关闭当前窗口
                        self.close()
                    else:
                        self.show_error_message(data.get('message'))
                else:
                    self.show_error_message(data.get('message'))
            else:
                self.result_label.setText("杨CC温馨提示~,秘钥错了哦~")
                self.result_label.setStyleSheet("color: red;")

        except requests.RequestException as e:
            # 如果发生异常（例如网络问题），捕获并显示错误信息
            self.result_label.setText(f"请求失败: {str(e)}")
            self.result_label.setStyleSheet("color: red;")

    def show_error_message(self, message):
        # 显示错误提示框
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("错误")
        msg.exec_()

# 主函数，启动应用程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyCheckWindow()
    window.show()
    sys.exit(app.exec_())
