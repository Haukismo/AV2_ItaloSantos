import cv2
import numpy as np

ajustaBrilho = lambda img, value: cv2.convertScaleAbs(img, alpha=1, beta=value)

nome_imagem = input("Caminho da Imagem: ")
imagem = cv2.imread(nome_imagem)

brilho = float(input("Digite o fator de ajuste de brilho: "))
imagem_ajustada = ajustaBrilho(imagem, brilho)


cv2.imshow("Imagem Original", nome_imagem)


cv2.imshow("Imagem com Brilho Ajustado", imagem_ajustada)

cv2.waitKey(0)
cv2.destroyAllWindows()
