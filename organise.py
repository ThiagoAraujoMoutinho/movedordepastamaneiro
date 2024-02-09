import os 
import shutil

from_dir = "C:/Users/mouti/Downloads"
to_dir = "C:/Users/mouti/byjus/imagens_baixadas"

list_of_files = os.listdir(from_dir)

#movendo todos os arquivos de imagem da pasta dowloads para outra pasta
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue

    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'arquivos_imagem'
        path3 = to_dir + '/' + 'arquivos_imagem' + '/' + file_name

        #verificando se a pasta existe antes de mover
        if os.path.exists(path2):
            print('movendo ' + file_name + '...')

            shutil.move(path1, path3)

        #caso contrario crie uma nova pasta e em seguida mova o arquivo
        else:
            os.makedirs(path2)
            print('movendo ' + file_name + '...')

            shutil.move(path1, path3)