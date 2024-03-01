from typing import Union, List

import pymcprotocol

from config import IPAndPort


class PLC:
    def __init__(self) -> None:

        self.ip, port = IPAndPort().load()
        self.port = int(port)

    def connect(self) -> Union[pymcprotocol.Type3E, None]:
        self.pymc3e = pymcprotocol.Type3E()
        try:
            self.pymc3e.connect(self.ip, self.port)
            return self.pymc3e
        except Exception as e:
            print("エラー:", str(e))
            self.pymc3e = None
            return self.pymc3e

    def close(self):
        try:
            self.pymc3e.close()
        except Exception:
            pass

    def read_bit(self, head, size) -> List[int]:
        """
        PLCのビットデータを読み取る。

        Args:
            head (str): ビットデータの先頭デバイス
            size (int): ビットデータのサイズ（先頭デバイスからのビット分）

        Returns:
            list: ビットデータのリスト
        """
        bit_read_values = self.pymc3e.batchread_bitunits(headdevice=head, readsize=size)
        return bit_read_values

    def read_word(self, head, size) -> List[int]:
        """
        PLCのワードデータを読み取る。

        Args:
            head (str): ワードデータの先頭デバイス
            size (int): ワードデータのサイズ（先頭デバイスからのワード分）

        Returns:
            list: ワードデータのリスト
        """
        word_read_values = self.pymc3e.batchread_wordunits(
            headdevice=head, readsize=size
        )
        return word_read_values

    def write_bit(self, head, values) -> None:
        """
        PLCにビットデータを書き込む。

        Args:
            bw_head_device (str): 書き込みビットの先頭デバイス
            bw_values : 書き込みビットのlist（先頭デバイスからのビット分）
        """
        self.pymc3e.batchwrite_bitunits(headdevice=head, values=values)

    def write_word(self, head, values) -> None:
        """
        PLCにワードデータを書き込む。

        Args:
            ww_head_device (str): 書き込みワードの先頭デバイス
            ww_values (int): 書き込みワードのlist（先頭デバイスからのワード分）
        """
        self.pymc3e.batchwrite_wordunits(headdevice=head, values=values)

    def is_connected(self):
        return hasattr(self, "pymc3e") and self.pymc3e is not None


if __name__ == "__main__":
    pass