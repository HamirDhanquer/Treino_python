import os 
import shutil


# Mover os arquivos de Lugar. 
caminho_original = r'E:\xampp1\htdocs\uploads'
caminho_novo  = r'E:\projetos\projetos_tutoriais\treino_python\wdocs\img'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.png' in file: 
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso.')