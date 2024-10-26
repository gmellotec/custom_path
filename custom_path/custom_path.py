import os

class CustomPath:
    def __init__(self, directories):
        # current = os.path.dirname(os.path.abspath(__file__))
        # self.root = os.path.dirname(current)
        self.root = self._get_project_root()
        self.directories = directories
        self.paths = {}

        for directory in self.directories:
            dir_path = os.path.join(self.root, *directory.split('/'))
            dir_key = directory.split('/')[-1]
            setattr(self, f"_{dir_key}", dir_path)
            self.paths[dir_key] = dir_path
            self._create_directory(dir_path)
            
    def _get_project_root(self):
        """Obtém a raiz do projeto de forma robusta."""
        # Usar o diretório atual como raiz do projeto
        return os.getcwd()

    def _create_directory(self, path):
        """Cria o diretório se ele não existir."""
        if not os.path.exists(path):
            os.makedirs(path)

    def _get_path(self, directory_path, file_name):
        """Constrói o caminho completo para um diretório ou para um arquivo dentro dele."""
        if file_name:
            return os.path.join(directory_path, file_name)
        return directory_path

    def __getattr__(self, name):
        def path_method(file_name=None):
            directory_path = self.paths.get(name)
            if directory_path:
                return self._get_path(directory_path, file_name)
            raise AttributeError(f"'Paths' object has no attribute '{name}'")
        return path_method

    def clear_dirs(self, directory_path):
        # Deletar todos os arquivos dentro de um diretório especificado.
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
