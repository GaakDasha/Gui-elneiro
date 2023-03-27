import eel
# установка пути к файлам интерфейса
eel.init('web')

# функция для отображения главного окна
@eel.expose
def show_main_window():
    eel.start("main.html", size=(1024,1600), mode='default')

# функция для отображения второго окна
@eel.expose
def show_second_window():
    eel.start('second.html', size=(1024,1600), mode='default')

# функция для отображения третьего окна
@eel.expose
def show_third_window():
    eel.start('third.html', size=(1024,1600), mode='default')

# запуск главного окна
eel.start('main.html', size=(1024,1600), mode='default')