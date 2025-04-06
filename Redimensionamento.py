import os
from PIL import Image

# Diretório com as imagens originais
pasta_origem = r'D:Nome da sua pasta' # Use duas barras (\\) para os diretórios

# Solicita ao usuário o caminho da pasta de destino
pasta_destino = input('Digite o caminho da pasta onde deseja salvar as imagens cortadas: ')

if not os.path.exists(pasta_origem):
    print(f"Erro: O diretório de origem '{pasta_origem}' não foi encontrado.")
    exit() 

# Cria a pasta de destino, se não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Itera sobre todos os arquivos na pasta de origem
for arquivo in os.listdir(pasta_origem):
    # Caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    
    # Verifica se é uma imagem (por extensão)
    if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        try:
            # Abre a imagem
            img = Image.open(caminho_arquivo)

            # Obtém as dimensões originais da imagem
            width, height = img.size

            # Se a imagem for menor que 600x600, redimensiona mantendo a proporção
            if width < 600 or height < 600:
                aspect_ratio = width / height
                if width < height:
                    new_width = 600
                    new_height = int(600 / aspect_ratio)
                else:
                    new_height = 600
                    new_width = int(600 * aspect_ratio)
                img = img.resize((new_width, new_height), Image.LANCZOS)
                width, height = img.size  # Atualiza as dimensões após o redimensionamento

            # Calcula as coordenadas para cortar uma região central de 600x600
            left = (width - 600) / 2
            top = (height - 600) / 2
            right = (width + 600) / 2
            bottom = (height + 600) / 2

            # Corta a imagem
            img = img.crop((left, top, right, bottom))
            
            # Salva a imagem na pasta de destino
            img.save(os.path.join(pasta_destino, arquivo))

        except Exception as e:
            print(f'Erro ao processar a imagem {arquivo}: {e}')

print(f'Processo concluído! Todas as imagens foram salvas na pasta "{pasta_destino}".')
