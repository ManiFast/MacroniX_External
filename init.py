from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QRadioButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QPixmap, QPainter, QBrush
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # COLORS
        color_of_minimize = "#444"
        color_of_close = "#ff0000"
        color_of_activate = "#191B28"
        color_of_text = "#d7ecf4"

        # Загружаем интерфейс из .ui файла
        loadUi('ui/untitled.ui', self)  # Укажите путь к вашему .ui файлу

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(800, 600)

        # Убираем стандартную рамку окна
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Устанавливаем прозрачный фон для закругленных углов
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Добавляем изображение № 1
        self.label = self.findChild(QLabel, "label_2")  # Замените "labelName" на имя вашего QLabel
        # Добавляем изображение № 2
        self.label1 = self.findChild(QLabel, "label_3")  # Замените "labelName" на имя вашего QLabel

        # Загружаем изображение
        pixmap = QPixmap("Images/scope1.png")  # Укажите путь к вашему изображению
        pixmap1 = QPixmap("Images/scope2.png")  # Укажите путь к вашему изображению

        # Масштабируем изображение с сохранением пропорций
        scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        scaled_pixmap1 = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)  # 100x100 с сохранением пропорций

        # Устанавливаем изображение в QLabel
        self.label.setPixmap(scaled_pixmap)
        self.label1.setPixmap(scaled_pixmap1)

        # Находим радио-кнопку по имени
        self.radioButton_1 = self.findChild(QRadioButton, 'radioButton_1')

        # Применяем стили только для radioButton_1
        if self.radioButton_1:
            self.radioButton_1.setStyleSheet("""
                QRadioButton {
                    background-color: """ + color_of_activate + """;
                    padding: 11px;
                    border: none;
                    border-radius: 6px;
                    text-align: left;
                    color: #FFFFFF;
                }
                QRadioButton:hover {
                    color: #FFFFFF;
                    background-color: """ + color_of_activate + """;
                }
                QRadioButton::indicator {
                    width: 0;
                    height: 0;
                    border: none;
                }
                QRadioButton:checked {
                    color: #FFFFFF;
                    background-color: """ + color_of_activate + """;
                }
            """)

            # Создаем эффект тени для свечения
            self.radio_shadow_effect = QGraphicsDropShadowEffect(self.radioButton_1)
            self.radio_shadow_effect.setBlurRadius(20)  # Радиус размытия тени
            self.radio_shadow_effect.setColor(QColor(0, 255, 0))  # Зеленый цвет свечения по умолчанию
            self.radio_shadow_effect.setOffset(0, 0)  # Смещение тени
            self.radioButton_1.setGraphicsEffect(self.radio_shadow_effect)

            # Изначально эффект свечения скрыт
            self.radio_shadow_effect.setEnabled(False)

            # Подключаем события радио-кнопки
            self.radioButton_1.enterEvent = self.radio_button_enter_event
            self.radioButton_1.leaveEvent = self.radio_button_leave_event
            self.radioButton_1.mousePressEvent = self.radio_button_mouse_press_event
            self.radioButton_1.mouseReleaseEvent = self.radio_button_mouse_release_event
            self.radioButton_1.toggled.connect(self.radio_button_toggled)  # Подключаем сигнал toggled

        # Находим кнопку pushButton (Активировать)
        self.pushButton = self.findChild(QPushButton, 'pushButton')

        if self.pushButton:
            # Применяем стили для кнопки "Активировать"
            self.pushButton.setStyleSheet("""
                QPushButton {
                    border: 1px solid green;
                    background-color: transparent;
                    color: """ + color_of_text + """;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    border: 1px solid green;
                    background-color: """ + color_of_activate + """;
                }
                QPushButton:pressed {
                    border: 1px solid red;
                    background-color: """ + color_of_activate + """;
                }
            """)

            # Создаем эффект тени для свечения
            self.shadow_effect = QGraphicsDropShadowEffect(self.pushButton)
            self.shadow_effect.setBlurRadius(20)  # Радиус размытия тени
            self.shadow_effect.setColor(QColor(0, 255, 0))  # Зеленый цвет свечения по умолчанию
            self.shadow_effect.setOffset(0, 0)  # Смещение тени
            self.pushButton.setGraphicsEffect(self.shadow_effect)

            # Изначально эффект свечения скрыт
            self.shadow_effect.setEnabled(False)

            # Подключаем события кнопки
            self.pushButton.enterEvent = self.button_enter_event
            self.pushButton.leaveEvent = self.button_leave_event
            self.pushButton.mousePressEvent = self.button_mouse_press_event
            self.pushButton.mouseReleaseEvent = self.button_mouse_release_event

        # Находим кнопки "Свернуть" и "Закрыть"
        self.minimize_button = self.findChild(QPushButton, 'minimize_button')  # Имя кнопки "Свернуть"
        self.close_button = self.findChild(QPushButton, 'close_button')  # Имя кнопки "Закрыть"

        # Применяем стили для кнопки "Свернуть"
        if self.minimize_button:
            self.minimize_button.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: """ + color_of_text + """;
                    font-size: 16px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: """ + color_of_minimize + """ ;
                }
            """)
            self.minimize_button.clicked.connect(self.showMinimized)  # Сворачиваем окно

        # Применяем стили для кнопки "Закрыть"
        if self.close_button:
            self.close_button.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: """ + color_of_text + """;
                    font-size: 16px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: """ + color_of_close + """ ;
                }
            """)
            self.close_button.clicked.connect(self.close)  # Закрываем окно

    def paintEvent(self, event):
        # Переопределяем метод paintEvent для отрисовки закругленных углов
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Включаем сглаживание
        painter.setBrush(QBrush(QColor("#191B28")))  # Цвет фона окна
        painter.setPen(Qt.NoPen)  # Убираем границу
        painter.drawRoundedRect(self.rect(), 10, 10)  # Рисуем закругленный прямоугольник

    def button_enter_event(self, event):
        # Включаем эффект свечения при наведении (зеленый цвет)
        self.shadow_effect.setColor(QColor(0, 255, 0))  # Зеленый
        self.shadow_effect.setEnabled(True)
        QPushButton.enterEvent(self.pushButton, event)

    def button_leave_event(self, event):
        # Выключаем эффект свечения при уходе курсора
        self.shadow_effect.setEnabled(False)
        QPushButton.leaveEvent(self.pushButton, event)

    def button_mouse_press_event(self, event):
        # Меняем цвет свечения на красный при нажатии
        self.shadow_effect.setColor(QColor(255, 0, 0))  # Красный
        self.shadow_effect.setEnabled(True)
        QPushButton.mousePressEvent(self.pushButton, event)

    def button_mouse_release_event(self, event):
        # Возвращаем зеленый цвет свечения при отпускании кнопки
        self.shadow_effect.setColor(QColor(0, 255, 0))  # Зеленый
        self.shadow_effect.setEnabled(True)
        QPushButton.mouseReleaseEvent(self.pushButton, event)

    def radio_button_enter_event(self, event):
        # Включаем эффект свечения при наведении (зеленый цвет)
        self.radio_shadow_effect.setColor(QColor(0, 255, 0))  # Зеленый
        self.radio_shadow_effect.setEnabled(True)
        QRadioButton.enterEvent(self.radioButton_1, event)

    def radio_button_leave_event(self, event):
        # Выключаем эффект свечения при уходе курсора, если радио-кнопка не выбрана
        if not self.radioButton_1.isChecked():
            self.radio_shadow_effect.setEnabled(False)
        QRadioButton.leaveEvent(self.radioButton_1, event)

    def radio_button_mouse_press_event(self, event):
        # Меняем цвет свечения на красный при нажатии
        self.radio_shadow_effect.setColor(QColor(255, 0, 0))  # Красный
        self.radio_shadow_effect.setEnabled(True)
        QRadioButton.mousePressEvent(self.radioButton_1, event)

    def radio_button_mouse_release_event(self, event):
        # Возвращаем зеленый цвет свечения при отпускании кнопки
        self.radio_shadow_effect.setColor(QColor(0, 255, 0))  # Зеленый
        self.radio_shadow_effect.setEnabled(True)
        QRadioButton.mouseReleaseEvent(self.radioButton_1, event)

    def radio_button_toggled(self, checked):
        # Включаем или выключаем свечение в зависимости от состояния радио-кнопки
        if checked:
            self.radio_shadow_effect.setColor(QColor(0, 255, 0))  # Зеленый
            self.radio_shadow_effect.setEnabled(True)
        else:
            self.radio_shadow_effect.setEnabled(False)

    # Переопределяем метод для перемещения окна
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.drag_start_position)
            self.drag_start_position = event.globalPos()
            event.accept()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()