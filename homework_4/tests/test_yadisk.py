# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.
import requests
import json


TOKEN = ''


def test_yadisk():
    yadisk_url = 'https://cloud-api.yandex.net'
    yadisk_headers = {'Authorization': TOKEN}
    requests.delete(url=f'{yadisk_url}/v1/disk/resources',
                    headers=yadisk_headers,
                    params={'path': '/test_dir'})
    create_dir_res = requests.put(url=f'{yadisk_url}/v1/disk/resources',
                                  headers=yadisk_headers,
                                  params={'path': '/test_dir'})
    dir_metadata_res = requests.get(url=f'{yadisk_url}/v1/disk/resources',
                                    headers=yadisk_headers,
                                    params={'path': '/'})
    assert create_dir_res.status_code == 201, \
        f'Current response status code is {create_dir_res.status_code}'
    assert [x for x in json.loads(dir_metadata_res.content.decode())['_embedded']['items'] if x['name'] == 'test_dir'],\
        f'Directory not found at root'
