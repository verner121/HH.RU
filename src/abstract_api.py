from abc import ABC, abstractmethod


class AbstractApi(ABC):
    """Абстрактный класс для класса по работе с API"""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str, page: int = 1):
        """Метод для получения списка вакансий по поисковому запросу"""
        pass
