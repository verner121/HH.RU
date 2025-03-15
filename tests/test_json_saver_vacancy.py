import json

import pytest

from src.json_saver_vacancy import JSONVacancyStorage
from src.vacancy import Vacancy


def test_add_vacancies(temp_json_file, vacancy_python_developer, vacancy_system_administrator):
    """Тестирование метода add_vacancies класса JSONVacancyStorage.  Проверяет, что после добавления вакансий в
    JSON-файл, количество записей соответствует добавленным вакансиям и данные корректно сохраняются."""
    storage = JSONVacancyStorage(temp_json_file)
    storage.add_vacancies([vacancy_python_developer, vacancy_system_administrator])

    with open(temp_json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == vacancy_python_developer.name
    assert data[1]["name"] == vacancy_system_administrator.name


def test_get_vacancies(temp_json_file, vacancy_python_developer, vacancy_system_administrator):
    """Тестирование метода get_vacancies класса JSONVacancyStorage. Проверяет, что метод возвращает корректную вакансию
    по заданным критериям."""
    storage = JSONVacancyStorage(temp_json_file)
    storage.add_vacancies([vacancy_python_developer, vacancy_system_administrator])

    result = storage.get_vacancies({"name": "Python_developer"})
    assert len(result) == 1
    assert result[0]["name"] == "Python_developer"


def test_delete_vacancies(temp_json_file, vacancy_python_developer, vacancy_system_administrator):
    """Тестирование метода delete_vacancies класса JSONVacancyStorage. Проверяет, что после удаления вакансии по
    заданным критериям, в JSON-файле остаётся только одна вакансия, которая не соответствует критериям удаления."""
    storage = JSONVacancyStorage(temp_json_file)
    storage.add_vacancies([vacancy_python_developer, vacancy_system_administrator])

    storage.delete_vacancies({"name": "Python_developer"})
    data = storage._load_data()

    assert len(data) == 1
    assert data[0]["name"] == "Системный администратор"


def test_add_invalid_vacancy(temp_json_file, vacancy_with_negative_salary):
    """Тестирование валидации при добавлении некорректной вакансии в JSONVacancyStorage. Проверяет, что при попытке
    добавить вакансию с отрицательной зарплатой выбрасывается исключение ValueError."""
    storage = JSONVacancyStorage(temp_json_file)
    with pytest.raises(ValueError):
        storage.add_vacancies([Vacancy(**vacancy_with_negative_salary)])
