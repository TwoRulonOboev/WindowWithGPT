from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

# Создание приложения
app = QApplication(sys.argv)

# Создание главного окна
main_window = QMainWindow()

# Установка размера окна
main_window.resize(1200, 800)

# Создание виджета просмотра веб-страниц
browser = QWebEngineView()

# Установка названия окна
main_window.setWindowTitle('Чат GPT')  

# Установка иконки окна
main_window.setWindowIcon(QIcon('Logo.ico')) 

# Установка URL для отображения
browser.setUrl(QUrl('https://gpt-chatbotru-chat-main.ru/#/chat'))

# Добавление виджета просмотра веб-страниц в главное окно
main_window.setCentralWidget(browser)

# Отображение главного окна
main_window.show()

# Запуск приложения
sys.exit(app.exec_())
