from PIL import Image

def load_image(path: str) -> Image.Image:
    """Carrega uma imagem a partir de um caminho."""
    return Image.open(path).convert("RGB")

def save_image(image: Image.Image, path: str) -> None:
    """Salva uma imagem no caminho especificado."""
    image.save(path)
