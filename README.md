# Sberbank
для запуска приложения необходимо:
1) сколнировать репозиторий в любую пустую папку
2) командой <python3 -m venv venv> создать вритуальную среду
3) активировать виртуальную среду командой <source venv/bin/activate>
4) из папки /Sberbank командой <pip3 install -r requirements.txt> установить все зависимотси
5) в файле config.py заменить URI базы данных postgresql
6) выполнить команду <export FLASK_APP=tasks.py>
7) командой <flask run> запустить flask сервер
8) надеяться на лучшее
