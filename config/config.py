from dataclasses import dataclass
from abc import ABC, abstractmethod

from configparser import ConfigParser

class ConfigManager(ABC):
    def __init__(self) -> None:
        self._config_file = "config/config.ini"
        self._config = ConfigParser()

    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass

class IPAndPort(ConfigManager):
    def __init__(self) -> None:
        self._config_file = "config/config.ini"
        self._config = ConfigParser()

    def load(self) -> None:
        try:
            self._config.read(self._config_file)
            _ip_address = self._config.get(
                "Settings", "ip_address", fallback=""
            )
            _port_number = self._config.get(
                "Settings", "port_number", fallback=""
            )
            return _ip_address, _port_number
        except Exception as e:
            print(f"設定ファイルの読み込みエラー: {e}")

    def save(self, ip_address: str, port_number: str) -> bool:
        try:
            self._config.read(self._config_file)
            self._config["Settings"] = {
                "ip_address": ip_address,
                "port_number": port_number,
            }

            with open(self._config_file, "w") as configfile:
                self._config.write(configfile)

            print(
                f"設定が保存されました: IPアドレス={ip_address}, ポート番号={port_number}"
            )
            return True
        except Exception as e:
            print(f"設定ファイルの保存エラー: {e}")
            return False