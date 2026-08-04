def log(func):
    from datetime import datetime
    def execução(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(datetime.now())
        return resultado
    return execução
    