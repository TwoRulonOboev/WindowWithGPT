import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QUrl, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile
from webbrowser import open_new_tab

class WebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if url.host() == 'gpt-chatbotru-chat-main.ru':
            return True
        return False

# Создание приложения
app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Создание главного окна
main_window = QMainWindow()
main_window.setWindowTitle('Чат GPT')
main_window.setWindowIcon(QIcon('Logo.png'))
main_window.resize(1200, 800)
print("Созданно окно")

# Создание виджета просмотра веб-страниц
browser = QWebEngineView()
browser.setPage(WebEnginePage(browser))
browser.setUrl(QUrl('https://gpt-chatbotru-chat-main.ru/#/chat'))
main_window.setCentralWidget(browser)
print("Создан виджет просмотра веб-страниц")

# Функция для отображения окна из трея
def show_window():
    main_window.showNormal()
    main_window.activateWindow()

# Функция для закрытия приложения
def quit_app():
    QCoreApplication.quit()

# Функция для открытия сайта в браузере
def open_site():
    open_new_tab('https://github.com/TwoRulonOboev')

# Путь к папке документов пользователя
documents_folder = os.path.join(os.path.expanduser('~'), 'Documents')

# Путь к папке GPT в документах
gpt_folder = os.path.join(documents_folder, 'GPT')

# Создание папки GPT, если она не существует
if not os.path.exists(gpt_folder):
    os.makedirs(gpt_folder)
    print("Создалась папка с куки")

# Установка пути для хранения cookies
QWebEngineProfile.defaultProfile().setPersistentStoragePath(gpt_folder)

# Функция для очистки cookies
def clear_cookies():
    QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
    print("Куки отчизенны")

# Переопределение метода closeEvent главного окна
def closeEvent(event):
    event.ignore()
    main_window.hide()

main_window.closeEvent = closeEvent

# Создание иконки в трее
tray_icon = QSystemTrayIcon(QIcon('Logo.png'), parent=app)
tray_icon.setToolTip('Чат GPT')
print("Добавилось в трее")

# Функция для обработки клика по иконке трея
def on_tray_icon_activated(reason):
    if reason == QSystemTrayIcon.Trigger:
        show_window()

# Связывание сигнала activated с функцией on_tray_icon_activated
tray_icon.activated.connect(on_tray_icon_activated)

print("Кнопки в трее создались")

menu = QMenu()
openAction = QAction('Открыть', main_window)
openAction.triggered.connect(show_window)
menu.addAction(openAction)

clearCookiesAction = QAction('Очистить cookies', main_window)
clearCookiesAction.triggered.connect(clear_cookies)
menu.addAction(clearCookiesAction)

visitSiteAction = QAction('Посетить сайт разработчика', main_window)
visitSiteAction.triggered.connect(open_site)
menu.addAction(visitSiteAction)

exitAction = QAction('Закрыть', main_window)
exitAction.triggered.connect(quit_app)
menu.addAction(exitAction)

tray_icon.setContextMenu(menu)
tray_icon.show()

# JavaScript для удаления элемента 
def on_load_finished():
    browser.page().runJavaScript("""
    var sidebarTitle = document.querySelector('.home_sidebar-title__l3KhW');
    if (sidebarTitle) {
        sidebarTitle.remove();
    }
    """)
    print("Текст удалён")

browser.loadFinished.connect(on_load_finished)

# Отображение главного окна
main_window.show()

# Запуск приложения
sys.exit(app.exec_())
