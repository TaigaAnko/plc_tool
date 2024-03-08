import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QStackedWidget,
    QWidget,
    QMessageBox,
    QScrollArea,
    QGridLayout,
    QHBoxLayout,
)
from PySide6.QtGui import QGuiApplication, QScreen

from config import IPAndPort
from plc import PLC


class SettingPage(QWidget):
    def __init__(self):
        super().__init__()

        self.ip_and_port = IPAndPort()

        # 初期化
        self.init_ui()
        self.load_config()

    def init_ui(self):

        # IPアドレスのテキストボックス
        self._ip_label = QLabel("IPアドレス:", self)
        self._ip_textbox = QLineEdit(self)
        self._ip_textbox.setFixedSize(100, 30)

        # ポート番号のテキストボックス
        self._port_label = QLabel("ポート番号:", self)
        self._port_textbox = QLineEdit(self)
        self._port_textbox.setFixedSize(100, 30)

        # 保存ボタン
        self._save_label = QLabel("", self)
        _save_button = QPushButton("保存", self)
        _save_button.clicked.connect(self.save_config)

        # 接続確認
        _confirm_label = QLabel("接続確認", self)

        self._confirm_plc_label = QLabel("", self)
        _confirm_plc_button = QPushButton("確認", self)
        _confirm_plc_button.clicked.connect(self.confirm_plc)

        # ビットデバイスの読み込みテスト
        _read_bit_test_label = QLabel("ビットデバイスの読み込み", self)

        # デバイス番号のテキストボックス
        self._bit_read_device_label = QLabel("デバイス番号:", self)
        self._bit_read_device_textbox = QLineEdit(self)
        self._bit_read_device_textbox.setFixedSize(100, 30)

        # 読み込むデバイス数
        self._bit_read_device_num_label = QLabel("デバイス数:", self)
        self._bit_read_device_num_textbox = QLineEdit(self)
        self._bit_read_device_num_textbox.setFixedSize(100, 30)

        self._bit_read_label = QLabel("", self)
        _read_bit_button = QPushButton("確認", self)
        _read_bit_button.clicked.connect(self.confirm_bit_read)

        # ワードデバイスの読み込みテスト
        _read_word_test_label = QLabel("ワードデバイスの読み込み", self)

        # デバイス番号のテキストボックス
        self._word_read_device_label = QLabel("デバイス番号:", self)
        self._word_read_device_textbox = QLineEdit(self)
        self._word_read_device_textbox.setFixedSize(100, 30)

        # 読み込むデバイス数
        self._word_read_device_num_label = QLabel("デバイス数:", self)
        self._word_read_device_num_textbox = QLineEdit(self)
        self._word_read_device_num_textbox.setFixedSize(100, 30)

        self._word_read_label = QLabel("", self)
        _read_word_button = QPushButton("確認", self)
        _read_word_button.clicked.connect(self.confirm_word_read)

        # ビットデバイスへ書き込みテスト
        _write_bit_test_label = QLabel("ビットデバイスへ書き込み", self)

        # デバイス番号のテキストボックス
        self._bit_write_device_label = QLabel("デバイス番号:", self)
        self._bit_write_device_textbox = QLineEdit(self)
        self._bit_write_device_textbox.setFixedSize(100, 30)

        # 読み込むデバイス数
        self._bit_write_device_num_label = QLabel("デバイス数:", self)
        self._bit_write_device_num_textbox = QLineEdit(self)
        self._bit_write_device_num_textbox.setFixedSize(100, 30)

        self._bit_write_label = QLabel("", self)
        _write_bit_button = QPushButton("確認", self)
        _write_bit_button.clicked.connect(self.confirm_bit_write)

        # ワードデバイスへ書き込みテスト
        _write_word_test_label = QLabel("ワードデバイスへ書き込み", self)

        # デバイス番号のテキストボックス
        self._word_write_device_label = QLabel("デバイス番号:", self)
        self._word_write_device_textbox = QLineEdit(self)
        self._word_write_device_textbox.setFixedSize(100, 30)

        # 読み込むデバイス数
        self._word_write_device_num_label = QLabel("デバイス数:", self)
        self._word_write_device_num_textbox = QLineEdit(self)
        self._word_write_device_num_textbox.setFixedSize(100, 30)

        self._word_write_label = QLabel("", self)
        _write_word_button = QPushButton("確認", self)
        _write_word_button.clicked.connect(self.confirm_bit_write)

        # レイアウト
        ip_prort_grid = QGridLayout()
        ip_prort_grid.addWidget(self._ip_label, 0, 0)
        ip_prort_grid.addWidget(self._ip_textbox, 0, 1)
        ip_prort_grid.addWidget(self._port_label, 1, 0)
        ip_prort_grid.addWidget(self._port_textbox, 1, 1)
        ip_prort_grid.addWidget(self._save_label, 2, 0)
        ip_prort_grid.addWidget(_save_button, 2, 1)

        confirm_label_grid = QGridLayout()
        confirm_label_grid.addWidget(_confirm_label, 0, 0)
        confirm_label_grid.addWidget(self._confirm_plc_label, 1, 0)
        confirm_label_grid.addWidget(_confirm_plc_button, 1, 1)

        read_bit_grid = QGridLayout()
        read_bit_grid.addWidget(_read_bit_test_label, 0, 0)
        read_bit_grid.addWidget(self._bit_read_device_label, 1, 0)
        read_bit_grid.addWidget(self._bit_read_device_textbox, 1, 1)
        read_bit_grid.addWidget(self._bit_read_device_num_label, 2, 0)
        read_bit_grid.addWidget(self._bit_read_device_num_textbox, 2, 1)
        read_bit_grid.addWidget(self._bit_read_label, 3, 0)
        read_bit_grid.addWidget(_read_bit_button, 3, 1)

        read_word_grid = QGridLayout()
        read_word_grid.addWidget(_read_word_test_label, 0, 0)
        read_word_grid.addWidget(self._word_read_device_label, 1, 0)
        read_word_grid.addWidget(self._word_read_device_textbox, 1, 1)
        read_word_grid.addWidget(self._word_read_device_num_label, 2, 0)
        read_word_grid.addWidget(self._word_read_device_num_textbox, 2, 1)
        read_word_grid.addWidget(self._word_read_label, 3, 0)
        read_word_grid.addWidget(_read_word_button, 3, 1)

        write_bit_grid = QGridLayout()
        write_bit_grid.addWidget(_write_bit_test_label, 0, 0)
        write_bit_grid.addWidget(self._bit_write_device_label, 1, 0)
        write_bit_grid.addWidget(self._bit_write_device_textbox, 1, 1)
        write_bit_grid.addWidget(self._bit_write_device_num_label, 2, 0)
        write_bit_grid.addWidget(self._bit_write_device_num_textbox, 2, 1)
        write_bit_grid.addWidget(self._bit_write_label, 3, 0)
        write_bit_grid.addWidget(_write_bit_button, 3, 1)

        write_word_grid = QGridLayout()
        write_word_grid.addWidget(_write_word_test_label, 0, 0)
        write_word_grid.addWidget(self._word_write_device_label, 1, 0)
        write_word_grid.addWidget(self._word_write_device_textbox, 1, 1)
        write_word_grid.addWidget(self._word_write_device_num_label, 2, 0)
        write_word_grid.addWidget(self._word_write_device_num_textbox, 2, 1)
        write_word_grid.addWidget(self._word_write_label, 3, 0)
        write_word_grid.addWidget(_write_word_button, 3, 1)

        # ウィジェットにレイアウトを設定
        first_phase = QHBoxLayout()
        first_phase.addLayout(read_bit_grid)
        first_phase.addSpacing(10)
        first_phase.addLayout(read_word_grid)

        second_phase = QHBoxLayout()
        second_phase.addLayout(write_bit_grid)
        second_phase.addSpacing(10)
        second_phase.addLayout(write_word_grid)

        layout = QVBoxLayout(self)
        layout.addLayout(ip_prort_grid)
        layout.addSpacing(10)
        layout.addLayout(confirm_label_grid)
        layout.addSpacing(10)
        layout.addLayout(first_phase)
        layout.addSpacing(10)
        layout.addLayout(second_phase)
        layout.addSpacing(10)

        self.setLayout(layout)

        # ウィンドウの設定
        self.setGeometry(0, 0, 600, 500)
        self.setWindowTitle("PLCチェッカー")
        self.setFixedSize(600, 500)

        self.center_window()

    def center_window(self):
        # アプリケーションのプライマリスクリーンを取得
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # ウィンドウの中心座標を計算
        window_rect = self.frameGeometry()
        window_rect.moveCenter(screen_geometry.center())

        # ウィンドウを中央に配置
        self.move(window_rect.topLeft())

    def confirm_plc(self):
        self.plc = PLC()
        self._confirm_plc_label.setText("")
        res = self.plc.connect()
        print(res)
        if res:
            self._confirm_plc_label.setText("接続を確認しました")
        else:
            self._confirm_plc_label.setText("接続できませんでした")

    def confirm_bit_read(self):
        self.plc = PLC()
        res = self.plc.connect()
        if res:
            req = self.plc.read_bit()
            self._bit_read_label.setText(f"読み込みに成功:{req}")
        else:
            self._bit_read_label.setText("PLC接続できませんでした")

    def confirm_word_read(self):
        self.plc = PLC()
        res = self.plc.connect()
        if res:
            req = self.plc.read_word()
            self._word_read_label.setText(f"読み込みに成功:{req}")
        else:
            self._word_read_label.setText("PLC接続できませんでした")

    def confirm_bit_write(self):
        self.plc = PLC()
        res = self.plc.connect()
        if res:
            req = self.plc.write_bit()
            self._word_read_label.setText(f"書き込みに成功:{req}")
        else:
            self._word_read_label.setText("PLC接続できませんでした")

    def confirm_word_write(self):
        self.plc = PLC()
        res = self.plc.connect()
        if res:
            req = self.plc.write_word()
            self._word_read_label.setText(f"書き込みに成功:{req}")
        else:
            self._word_read_label.setText("PLC接続できませんでした")

    def load_config(self):
        _ip_address, _port_number = self.ip_and_port.load()
        self._ip_textbox.setText(_ip_address)
        self._port_textbox.setText(_port_number)

    def save_config(self):
        _ip_address = self._ip_textbox.text()
        _port_number = self._port_textbox.text()

        response = self.ip_and_port.save(_ip_address, _port_number)
        if response:
            self._save_label.setText("保存しました")
        else:
            self._save_label.setText("保存できませんでした")

    def closeEvent(self, event):
        confirmObject = QMessageBox.question(
            None, "Message", "設定を閉じますか？", QMessageBox.Yes, QMessageBox.No
        )

        if confirmObject == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = SettingPage()
    main_app.show()
    sys.exit(app.exec_())
