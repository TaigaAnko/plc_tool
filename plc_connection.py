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
        self.plc = PLC()

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

        # 読み込みテスト
        _read_bit_test_label = QLabel("ビットデバイスの読み込み", self)

        # デバイス番号のテキストボックス
        self._read_device_label = QLabel("デバイス番号:", self)
        self._read_device_textbox = QLineEdit(self)
        self._read_device_textbox.setFixedSize(100, 30)

        # 読み込むデバイス数
        self._read_device_num_label = QLabel("デバイス数:", self)
        self._read_device_num_textbox = QLineEdit(self)
        self._read_device_num_textbox.setFixedSize(100, 30)

        self._bit_read_label = QLabel("", self)
        _read_bit_button = QPushButton("確認", self)
        _read_bit_button.clicked.connect(self.confirm_bit_read)

        # 書き込みテスト

        # レイアウト
        ip_prort_grid = QGridLayout()
        ip_prort_grid.addWidget(self._ip_label, 0, 0)
        ip_prort_grid.addWidget(self._ip_textbox, 0, 1)
        ip_prort_grid.addWidget(self._port_label, 1, 0)
        ip_prort_grid.addWidget(self._port_textbox, 1, 1)
        ip_prort_grid.addWidget(self._save_label, 2, 0)
        ip_prort_grid.addWidget(_save_button, 2, 0)

        confirm_label_grid = QGridLayout()
        confirm_label_grid.addWidget(_confirm_label, 0, 0)
        confirm_label_grid.addWidget(self._confirm_plc_label, 1, 0)
        confirm_label_grid.addWidget(_confirm_plc_button, 1, 1)

        read_bit_grid = QGridLayout()
        read_bit_grid.addWidget(_read_bit_test_label, 0, 0)
        read_bit_grid.addWidget(self._read_device_label, 1, 0)
        read_bit_grid.addWidget(self._read_device_textbox, 1, 1)
        read_bit_grid.addWidget(self._read_device_num_label, 2, 0)
        read_bit_grid.addWidget(self._read_device_num_textbox, 2, 1)
        read_bit_grid.addWidget(self._bit_read_label, 3, 0)
        read_bit_grid.addWidget(_read_bit_button, 3, 1)

        b6_station_grid = QGridLayout()
        b6_station_grid.addWidget(b6_station_label, 0, 0)
        b6_station_grid.addWidget(self._b6_AGV1_label, 1, 0)
        b6_station_grid.addWidget(self._b6_AGV1_textbox, 1, 1)
        b6_station_grid.addWidget(self._b6_AGV2_label, 2, 0)
        b6_station_grid.addWidget(self._b6_AGV2_textbox, 2, 1)

        c1_station_grid = QGridLayout()
        c1_station_grid.addWidget(c1_station_label, 0, 0)
        c1_station_grid.addWidget(self._c1_AGV1_label, 1, 0)
        c1_station_grid.addWidget(self._c1_AGV1_textbox, 1, 1)
        c1_station_grid.addWidget(self._c1_AGV2_label, 2, 0)
        c1_station_grid.addWidget(self._c1_AGV2_textbox, 2, 1)

        # ウィジェットにレイアウトを設定
        first_phase = QHBoxLayout()
        first_phase.addLayout(empty_station_grid)
        first_phase.addSpacing(10)
        first_phase.addLayout(b1_station_grid)

        second_phase = QHBoxLayout()
        second_phase.addLayout(b6_station_grid)
        second_phase.addSpacing(10)
        second_phase.addLayout(c1_station_grid)

        layout = QVBoxLayout(self)
        layout.addLayout(ip_prort_grid)
        layout.addLayout(first_phase)
        layout.addLayout(second_phase)
        layout.addSpacing(10)
        layout.addWidget(_save_button)

        self.setLayout(layout)

        # ウィンドウの設定
        self.setGeometry(0, 0, 420, 400)
        self.setWindowTitle("設定")
        self.setFixedSize(420, 400)

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
        res = self.plc.connect()
        if res:
            self._confirm_plc_label.setText("接続を確認しました")
        else:
            self._confirm_plc_label.setText("接続できませんでした")

    def confirm_bit_read(self):
        res = self.plc.connect()
        if res:
            req = self.plc.read_bit()
            self._confirm_bit_read_label.setText(f"読み込みに成功:{req}")
        else:
            self._confirm_bit_read_label.setText("PLC接続できませんでした")

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
    ip_adress, port = IPAndPort().load()
    print(ip_adress, port)
