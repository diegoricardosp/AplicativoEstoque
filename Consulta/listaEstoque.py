from main import estoque

def consultaEstoque():
    for k, v in estoque.items():
            print(f'{k} - {v}.')