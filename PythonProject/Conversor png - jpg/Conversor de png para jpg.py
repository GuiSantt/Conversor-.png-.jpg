import os
import cv2

pasta_origem = 'Pasta de origem'
pasta_destino = 'Imagens convertidas'

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.endswith('.png'):
        caminho_entrada = os.path.join(pasta_origem, nome_arquivo)
        imagem = cv2.imread(caminho_entrada)
        novo_nome = nome_arquivo.replace('.png', '.jpg')
        caminho_saida = os.path.join(pasta_destino, novo_nome)
        cv2.imwrite(caminho_saida, imagem)
        print(f'Convertido: {nome_arquivo} -> {novo_nome}')


