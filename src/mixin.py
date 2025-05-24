class CreatLoggerMixin:
    def __init__(self, *args, **kwargs):
        print(f"[LOG] Создан объект класса {self.__class__.__name__} с аргументами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)