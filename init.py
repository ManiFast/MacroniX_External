from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation
from PyQt5 import QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # COLORS
        color_of_minimize = "#444"
        color_of_close = "#ff0000"
        color_of_activate = "#191B28"
        color_of_text = "#d 7ecf4"

        # Загружаем интерфейс из .ui файла
        loadUi('ui/Main.ui', self)  # Укажите путь к вашему .ui файлу
        # Найдите кнопку по её имени (например, "toggleButton")
        self.toggle_button = self.findChild(QtWidgets.QPushButton, "toggleButton")
        self.toggle_button1 = self.findChild(QtWidgets.QPushButton, "toggleButton_3")
        self.toggle_button2 = self.findChild(QtWidgets.QPushButton, "toggleButton_4")
        self.toggle_button3 = self.findChild(QtWidgets.QPushButton, "toggleButton_5")
        self.toggle_button4 = self.findChild(QtWidgets.QPushButton, "toggleButton_6")
        self.toggle_button5 = self.findChild(QtWidgets.QPushButton, "toggleButton_7")

        # Если кнопка найдена, преобразуем её в ToggleSwitch
        if self.toggle_button or self.toggle_button1 or self.toggle_button5 or self.toggle_button4 or self.toggle_button3 or self.toggle_button2:
            self.toggle_button.setCheckable(True)
            self.toggle_button1.setCheckable(True)
            self.toggle_button2.setCheckable(True)
            self.toggle_button3.setCheckable(True)
            self.toggle_button4.setCheckable(True)
            self.toggle_button5.setCheckable(True)
            self.toggle_button.setFixedSize(60, 30)
            self.toggle_button1.setFixedSize(60, 30)
            self.toggle_button2.setFixedSize(60, 30)
            self.toggle_button3.setFixedSize(60, 30)
            self.toggle_button4.setFixedSize(60, 30)
            self.toggle_button5.setFixedSize(60, 30)
            self.toggle_button.setStyleSheet("""
                        QPushButton {
                            background-color: #191b28;
                            border-radius: 15px;
                            border: 1px #191b28;
                        }
                        QPushButton:checked {
                            background-color: #8778d1;
                            border: 1px solid #8778d1;
                        }
                    """)
            self.toggle_button1.setStyleSheet("""
                                    QPushButton {
                                        background-color: #191b28;
                                        border-radius: 15px;
                                        border: 1px #191b28;
                                    }
                                    QPushButton:checked {
                                        background-color: #8778d1;
                                        border: 1px solid #8778d1;
                                    }
                                """)
            self.toggle_button2.setStyleSheet("""
                                    QPushButton {
                                        background-color: #191b28;
                                        border-radius: 15px;
                                        border: 1px #191b28;
                                    }
                                    QPushButton:checked {
                                        background-color: #8778d1;
                                        border: 1px solid #8778d1;
                                    }
                                """)
            self.toggle_button3.setStyleSheet("""
                                    QPushButton {
                                        background-color: #191b28;
                                        border-radius: 15px;
                                        border: 1px #191b28;
                                    }
                                    QPushButton:checked {
                                        background-color: #8778d1;
                                        border: 1px solid #8778d1;
                                    }
                                """)
            self.toggle_button4.setStyleSheet("""
                                    QPushButton {
                                        background-color: #191b28;
                                        border-radius: 15px;
                                        border: 1px #191b28;
                                    }
                                    QPushButton:checked {
                                        background-color: #8778d1;
                                        border: 1px solid #8778d1;
                                    }
                                """)
            self.toggle_button5.setStyleSheet("""
                                    QPushButton {
                                        background-color: #191b28;
                                        border-radius: 15px;
                                        border: 1px #191b28;
                                    }
                                    QPushButton:checked {
                                        background-color: #8778d1;
                                        border: 1px solid #8778d1;
                                    }
                                """)

            # Создаем кружок (индикатор)
            self.circle = QtWidgets.QPushButton(self.toggle_button)
            self.circle1 = QtWidgets.QPushButton(self.toggle_button1)
            self.circle2 = QtWidgets.QPushButton(self.toggle_button2)
            self.circle3 = QtWidgets.QPushButton(self.toggle_button3)
            self.circle4 = QtWidgets.QPushButton(self.toggle_button4)
            self.circle5 = QtWidgets.QPushButton(self.toggle_button5)
            self.circle.setFixedSize(26, 26)
            self.circle1.setFixedSize(26, 26)
            self.circle2.setFixedSize(26, 26)
            self.circle3.setFixedSize(26, 26)
            self.circle4.setFixedSize(26, 26)
            self.circle5.setFixedSize(26, 26)
            self.circle.setStyleSheet("""
                        QPushButton {
                            background-color: white;
                            border-radius: 13px;
                            border: 1px solid #ccc;
                        }
                    """)
            self.circle1.setStyleSheet("""
                                    QPushButton {
                                        background-color: white;
                                        border-radius: 13px;
                                        border: 1px solid #ccc;
                                    }
                                """)
            self.circle2.setStyleSheet("""
                                    QPushButton {
                                        background-color: white;
                                        border-radius: 13px;
                                        border: 1px solid #ccc;
                                    }
                                """)
            self.circle3.setStyleSheet("""
                                    QPushButton {
                                        background-color: white;
                                        border-radius: 13px;
                                        border: 1px solid #ccc;
                                    }
                                """)
            self.circle4.setStyleSheet("""
                                    QPushButton {
                                        background-color: white;
                                        border-radius: 13px;
                                        border: 1px solid #ccc;
                                    }
                                """)
            self.circle5.setStyleSheet("""
                                    QPushButton {
                                        background-color: white;
                                        border-radius: 13px;
                                        border: 1px solid #ccc;
                                    }
                                """)
            self.circle.move(2, 2)
            self.circle1.move(2, 2)
            self.circle2.move(2, 2)
            self.circle3.move(2, 2)
            self.circle4.move(2, 2)
            self.circle5.move(2, 2)

            # Анимация для перемещения кружка
            self.animation = QPropertyAnimation(self.circle, b"geometry")
            self.animation1 = QPropertyAnimation(self.circle1, b"geometry")
            self.animation2 = QPropertyAnimation(self.circle2, b"geometry")
            self.animation3 = QPropertyAnimation(self.circle3, b"geometry")
            self.animation4 = QPropertyAnimation(self.circle4, b"geometry")
            self.animation5 = QPropertyAnimation(self.circle5, b"geometry")
            self.animation.setDuration(200)
            self.animation1.setDuration(200)
            self.animation2.setDuration(200)
            self.animation3.setDuration(200)
            self.animation4.setDuration(200)
            self.animation5.setDuration(200)

            # Подключение сигнала изменения состояния
            self.toggle_button.toggled.connect(self.animate_circle)
            self.toggle_button1.toggled.connect(self.animate_circle1)
            self.toggle_button2.toggled.connect(self.animate_circle2)
            self.toggle_button3.toggled.connect(self.animate_circle3)
            self.toggle_button4.toggled.connect(self.animate_circle4)
            self.toggle_button5.toggled.connect(self.animate_circle5)

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(1000, 850)

        # Убираем стандартную рамку окна
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Устанавливаем прозрачный фон для закругленных углов
        self.setAttribute(Qt.WA_TranslucentBackground)

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

    def animate_circle(self, checked):
        if checked:
            # Перемещение кружка вправо
            self.animation.setStartValue(QRect(2, 2, 26, 26))
            self.animation.setEndValue(QRect(32, 2, 26, 26))

        else:
            # Перемещение кружка влево
            self.animation.setStartValue(QRect(32, 2, 26, 26))
            self.animation.setEndValue(QRect(2, 2, 26, 26))
        self.animation.start()

    def animate_circle1(self, checked):
        if checked:
            # Перемещение кружка вправо
            self.animation1.setStartValue(QRect(2, 2, 26, 26))
            self.animation1.setEndValue(QRect(32, 2, 26, 26))

        else:
            # Перемещение кружка влево
            self.animation1.setStartValue(QRect(32, 2, 26, 26))
            self.animation1.setEndValue(QRect(2, 2, 26, 26))
        self.animation1.start()

    def animate_circle2(self, checked):
        if checked:
            # Перемещение кружка вправо
            self.animation2.setStartValue(QRect(2, 2, 26, 26))
            self.animation2.setEndValue(QRect(32, 2, 26, 26))

        else:
            # Перемещение кружка влево
            self.animation2.setStartValue(QRect(32, 2, 26, 26))
            self.animation2.setEndValue(QRect(2, 2, 26, 26))
        self.animation2.start()

    def animate_circle3(self, checked):
        if checked:
            # Перемещение кружка вправо
            self.animation3.setStartValue(QRect(2, 2, 26, 26))
            self.animation3.setEndValue(QRect(32, 2, 26, 26))

        else:
            # Перемещение кружка влево
            self.animation3.setStartValue(QRect(32, 2, 26, 26))
            self.animation3.setEndValue(QRect(2, 2, 26, 26))
        self.animation3.start()

    def animate_circle4(self, checked):
        if checked:
            # Перемещение кружка вправо
            self.animation4.setStartValue(QRect(2, 2, 26, 26))
            self.animation4.setEndValue(QRect(32, 2, 26, 26))

        else:
            # Перемещение кружка влево
            self.animation4.setStartValue(QRect(32, 2, 26, 26))
            self.animation4.setEndValue(QRect(2, 2, 26, 26))
        self.animation4.start()

    def animate_circle5(self, checked):
        if checked:
            # Перемещение кружка вправо
            self.animation5.setStartValue(QRect(2, 2, 26, 26))
            self.animation5.setEndValue(QRect(32, 2, 26, 26))

        else:
            # Перемещение кружка влево
            self.animation5.setStartValue(QRect(32, 2, 26, 26))
            self.animation5.setEndValue(QRect(2, 2, 26, 26))
        self.animation5.start()

    def paintEvent(self, event):
        # Переопределяем метод paintEvent для отрисовки закругленных углов и фона
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Включаем сглаживание

        # Рисуем закругленные углы поверх изображения
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



