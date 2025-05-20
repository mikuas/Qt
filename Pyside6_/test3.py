from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QApplication, QGraphicsOpacityEffect
)
from PySide6.QtCore import Qt, Signal, QPropertyAnimation, QPoint, QEasingCurve
import sys

class Pager(QWidget):
    page_changed = Signal(int)

    def __init__(self, total_pages=20, parent=None):
        super().__init__(parent)
        self.total_pages = total_pages
        self.current_page = 1
        self.max_buttons = 5
        self.buttons = []
        self.animations = []

        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout(self)

        self.first_btn = QPushButton("⏮")
        self.prev_btn = QPushButton("◀")
        self.next_btn = QPushButton("▶")
        self.last_btn = QPushButton("⏭")

        self.jump_input = QLineEdit()
        self.jump_input.setFixedWidth(40)
        self.jump_input.setPlaceholderText("页")
        self.total_label = QLabel(f"共计 {self.total_pages}")

        self.first_btn.clicked.connect(self.go_first)
        self.prev_btn.clicked.connect(self.go_prev)
        self.next_btn.clicked.connect(self.go_next)
        self.last_btn.clicked.connect(self.go_last)
        self.jump_input.returnPressed.connect(self.go_jump)

        self.layout.addWidget(self.first_btn)
        self.layout.addWidget(self.prev_btn)

        # 按钮区域用个widget包起来
        self.page_buttons_widget = QWidget()
        self.page_buttons_layout = QHBoxLayout(self.page_buttons_widget)
        self.page_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.page_buttons_layout.setSpacing(5)
        self.layout.addWidget(self.page_buttons_widget)

        self.layout.addWidget(self.next_btn)
        self.layout.addWidget(self.last_btn)
        self.layout.addStretch()
        self.layout.addWidget(self.jump_input)
        self.layout.addWidget(self.total_label)

        self.setLayout(self.layout)
        self.update_buttons(initial=True)

    def clear_page_buttons(self):
        for btn in self.buttons:
            self.page_buttons_layout.removeWidget(btn)
            btn.deleteLater()
        self.buttons.clear()

    def fade_out_in(self, update_func):
        # 先透明度动画
        self.animations.clear()
        for btn in self.buttons:
            effect = QGraphicsOpacityEffect(btn)
            btn.setGraphicsEffect(effect)
            anim = QPropertyAnimation(effect, b"opacity", self)
            anim.setDuration(200)
            anim.setStartValue(1)
            anim.setEndValue(0)
            anim.setEasingCurve(QEasingCurve.InOutQuad)
            anim.start()
            self.animations.append(anim)

        if self.animations:
            self.animations[-1].finished.connect(lambda: (update_func(), self.fade_in()))
        else:
            update_func()
            self.fade_in()

    def fade_in(self):
        for btn in self.buttons:
            effect = QGraphicsOpacityEffect(btn)
            btn.setGraphicsEffect(effect)
            anim = QPropertyAnimation(effect, b"opacity", self)
            anim.setDuration(200)
            anim.setStartValue(0)
            anim.setEndValue(1)
            anim.setEasingCurve(QEasingCurve.InOutQuad)
            anim.start()
            self.animations.append(anim)

    def slide_animation(self, offset_x, update_func):
        anim = QPropertyAnimation(self.page_buttons_widget, b"pos", self)
        start_pos = self.page_buttons_widget.pos()
        end_pos = start_pos + QPoint(offset_x, 0)
        anim.setStartValue(start_pos)
        anim.setEndValue(end_pos)
        anim.setDuration(200)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.finished.connect(lambda: (update_func(), self.reset_position()))
        anim.start()
        self.animations.append(anim)

    def reset_position(self):
        # 重置位置到标准布局里
        self.page_buttons_widget.move(0, self.page_buttons_widget.y())
        self.fade_in()

    def update_buttons(self, initial=False, slide_offset=0):
        self.first_btn.setEnabled(self.current_page != 1)
        self.prev_btn.setEnabled(self.current_page != 1)
        self.next_btn.setEnabled(self.current_page != self.total_pages)
        self.last_btn.setEnabled(self.current_page != self.total_pages)

        def update():
            self.clear_page_buttons()
            pages = self.get_display_pages()
            for page in pages:
                if page == "...":
                    btn = QLabel("...")
                    btn.setAlignment(Qt.AlignCenter)
                else:
                    btn = QPushButton(str(page))
                    btn.setCheckable(True)
                    btn.setChecked(page == self.current_page)
                    btn.clicked.connect(lambda checked, p=page: self.go_page(p))
                self.page_buttons_layout.addWidget(btn)
                self.buttons.append(btn)

        if initial:
            update()
        else:
            # 有滑动偏移就滑动动画
            if slide_offset != 0:
                self.slide_animation(slide_offset, update)
            else:
                self.fade_out_in(update)

    def get_display_pages(self):
        pages = []
        if self.total_pages <= self.max_buttons:
            pages = list(range(1, self.total_pages + 1))
        else:
            if self.current_page <= 3:
                pages = [1, 2, 3, 4, 5, "...", self.total_pages]
            elif self.current_page >= self.total_pages - 2:
                pages = [1, "...", self.total_pages - 4, self.total_pages - 3, self.total_pages - 2, self.total_pages - 1, self.total_pages]
            else:
                pages = [1, "...", self.current_page - 1, self.current_page, self.current_page + 1, "...", self.total_pages]
        return pages

    def go_first(self):
        if self.current_page != 1:
            self.current_page = 1
            self.update_buttons(slide_offset=-50)
            self.page_changed.emit(self.current_page)

    def go_prev(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_buttons(slide_offset=30)
            self.page_changed.emit(self.current_page)

    def go_next(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_buttons(slide_offset=-30)
            self.page_changed.emit(self.current_page)

    def go_last(self):
        if self.current_page != self.total_pages:
            self.current_page = self.total_pages
            self.update_buttons(slide_offset=50)
            self.page_changed.emit(self.current_page)

    def go_jump(self):
        try:
            page = int(self.jump_input.text())
            if 1 <= page <= self.total_pages:
                offset = (page - self.current_page) * -10  # 根据跳跃量计算一点点滑动效果
                self.current_page = page
                self.update_buttons(slide_offset=offset)
                self.page_changed.emit(self.current_page)
        except ValueError:
            pass

    def go_page(self, page):
        if page != self.current_page:
            offset = (page - self.current_page) * -10
            self.current_page = page
            self.update_buttons(slide_offset=offset)
            self.page_changed.emit(self.current_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pager = Pager(total_pages=20)
    pager.page_changed.connect(lambda p: print(f"跳转到第 {p} 页"))
    pager.show()
    sys.exit(app.exec())
