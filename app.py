from flask import Flask, Response
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])  # Обрабатываем GET-запросы
def contacts():
    # Путь к HTML-файлу
    html_file_path = 'contacts.html'

    try:
        # Читаем содержимое HTML-файла
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Формируем ответ с типом контента text/html
        response = Response(html_content, mimetype='text/html')
        return response

    except FileNotFoundError:
        error_msg = '<h1>Ошибка: HTML-файл не найден!</h1>'
        return Response(error_msg, mimetype='text/html', status=404)
    except Exception as e:
        error_msg = f'<h1>Ошибка при чтении файла: {str(e)}</h1>'
        return Response(error_msg, mimetype='text/html', status=500)


if __name__ == '__main__':
    app.run(debug=True)  # Запуск сервера
