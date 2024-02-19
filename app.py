# Импорт класса Flask из библиотеки Flask и функции render_template для рендеринга HTML-шаблонов
from flask import Flask, render_template  
# Импорт класса SQLAlchemy для работы с базами данных SQLAlchemy в приложении Flask
from flask_sqlalchemy import SQLAlchemy  



# Создание экземпляра веб-приложения Flask с указанием текущего модуля в качестве имени
app = Flask(__name__)  
# Установка параметров конфигурации для подключения к базе данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
# Создание экземпляра SQLAlchemy и связывание его с приложением Flask
db = SQLAlchemy(app)  


# Определение модели данных Article для отображения в базе данных
class Article(db.Model):  
    # Поле id - первичный ключ таблицы
    id = db.Column(db.Integer, primary_key=True)  

    # Поле title - строка с максимальной длиной 100 символов, не может быть пустым
    title = db.Column(db.String(100), nullable=False)  

    # Поле content - текстовое поле, не может быть пустым
    content = db.Column(db.Text, nullable=False)  

    # Метод для строкового представления объекта Article
    def __repr__(self):  
        return f"Article(title='{self.title}', content='{self.content}')"



# Декоратор для установки маршрута '/' для вызова функции index
@app.route('/')  
# Декоратор для установки маршрута '/home' для вызова функции index
@app.route('/home')  
def index():  
    # Функция для отображения главной страницы приложения
    return render_template('index.html')  


# Декоратор для установки маршрута '/about' для вызова функции about
@app.route('/about')  
def about():  
    # Функция для отображения страницы "О нас"
    return render_template('about.html')


@app.route('/sign_in')  
def sign_in():  
    # Функция для отображения страницы "О нас"
    return render_template('sign_in.html')
  


@app.route('/sign_up')  
def login():  
    # Функция для отображения страницы "О нас"
    return render_template('sign_up.html')
  

# Декоратор для установки маршрута '/user/<string:name>/<int:id>'
@app.route('/user/<string:name>/<int:id>')  
def user(name, id):  
    # Функция для отображения страницы пользователя с указанным именем и идентификатором
    return 'User page:',  name + " - " + str(id)  


@app.route('/hello')  
def hello():  
    
    return 'Привет мир!'


@app.route('/test')  
def test():  
    # Функция для отображения страницы "О нас"
    return render_template('test.html')
  





# Условие для проверки, запущен ли этот скрипт напрямую
if __name__ == '__main__':  
    # Запуск веб-приложения Flask в режиме отладки
    app.run(debug=True)  
