from PIL import Image
import numpy as np

def transfer_palette(source: Image.Image, target: Image.Image) -> Image.Image:
    """
    Transfere a paleta de cores da imagem source para a imagem target
    usando média dos canais de cor.
    """
    source_arr = np.array(source)
    target_arr = np.array(target)

    # calcula média de cada canal na imagem source
    source_means = source_arr.reshape(-1, 3).mean(axis=0)
    target_means = target_arr.reshape(-1, 3).mean(axis=0)

    # diferença entre as médias
    diff = source_means - target_means

    # aplica a diferença na imagem target
    new_arr = np.clip(target_arr + diff, 0, 255).astype(np.uint8)
    return Image.fromarray(new_arr)

def blend_images(img1: Image.Image, img2: Image.Image, alpha: float = 0.5) -> Image.Image:
    """
    Mescla duas imagens com um fator alpha (0 a 1).
    """
    img1 = img1.resize((min(img1.width, img2.width), min(img1.height, img2.height)))
    img2 = img2.resize(img1.size)

    return Image.blend(img1, img2, alpha)
