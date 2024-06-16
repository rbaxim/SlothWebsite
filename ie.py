import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple PyQt Browser')
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://localhost:3000'))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.back_button = QPushButton('<')
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton('>')
        self.forward_button.clicked.connect(self.browser.forward)

        self.reload_button = QPushButton('⟳')
        self.reload_button.clicked.connect(self.browser.reload)
        
        nav_bar = QToolBar()
        nav_bar.addWidget(self.back_button)
        nav_bar.addWidget(self.forward_button)
        nav_bar.addWidget(self.reload_button)
        nav_bar.addWidget(self.url_bar)

        self.addToolBar(nav_bar)
        self.setCentralWidget(self.browser)
        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

def main():
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
