from abc import ABC, abstractmethod


class SchemaVersioner(ABC):
    @abstractmethod
    def has_schema_version(self) -> bool:
        pass

    @abstractmethod
    def _get_schema_version(self) -> int:
        pass

    def get_schema_version(self) -> int:
        if not self.has_schema_version():
            return 0
        return self._get_schema_version()

    @abstractmethod
    def set_schema_version(self, v: int):
        pass
