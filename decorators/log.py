def log(func):
    from datetime import datetime
    def execução(*args, **kwargs):
        resultado = func(*args, **kwargs)
        arq = open('C:\\Users\\artur\\Projects\\PythonDIO\\log.txt', 'a')
        arq.write(f'{datetime.now()}, {func.__name__}, {args, kwargs}, {resultado} \n')
        return resultado
    return execução
