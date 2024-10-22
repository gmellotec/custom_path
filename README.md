# Custom Path Package

Este pacote Python permite criar e gerenciar diretórios personalizados e construir caminhos para arquivos de forma dinâmica. Ele é útil para projetos que precisam organizar e acessar diretórios de maneira consistente e automatizada.

## Funcionalidades

- **Criação automática de diretórios**: Se o diretório não existir, ele será criado automaticamente.
- **Geração de caminhos completos**: Cria caminhos completos para arquivos dentro dos diretórios especificados.
- **Limpeza de diretórios**: Remove todos os arquivos dentro de um diretório específico.

## Instalação

Para instalar o pacote diretamente do GitHub, use o seguinte comando:

```bash
pip install git+https://github.com/gmellotec/custom_path.git
```

## Como Usar
### Inicialização do Pacote
Ao inicializar a classe CustomPath, você deve fornecer uma lista de diretórios que deseja utilizar. Cada item na lista é um caminho relativo que será convertido em um caminho absoluto.

```python
from custom_path import CustomPath

# Inicializando o CustomPath com uma lista de diretórios
path = CustomPath(["data/logs", "data/output", "temp/files"])
```

### Acessando Diretórios e Arquivos
Após a inicialização, você pode acessar os diretórios e arquivos dinamicamente:

```python
# Obtendo o caminho absoluto para o diretório 'logs'
print(path.logs())  # Exemplo de saída: /caminho/para/projeto/data/logs

# Obtendo o caminho absoluto para 'log.txt' dentro de 'logs'
print(path.logs("log.txt"))  # Exemplo de saída: /caminho/para/projeto/data/logs/log.txt
```
### Limpando Diretórios

A função clear_dirs permite limpar o conteúdo de um diretório específico:

```python
# Limpando todos os arquivos dentro do diretório 'logs'
path.clear_dirs(path.logs())
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests no GitHub.

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.