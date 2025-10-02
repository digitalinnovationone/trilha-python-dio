# Image Palette Processor 🎨

Um pacote simples em Python para brincar com processamento de imagens, 
permitindo **transferência de paleta de cores** e **mesclagem de imagens**.

## Instalação

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Exemplo de uso:

```python
from image_palette_processor import load_image, save_image, transfer_palette, blend_images

# Carregar imagens
img1 = load_image("source.jpg")
img2 = load_image("target.jpg")

# Transferir paleta de cores
result1 = transfer_palette(img1, img2)
save_image(result1, "result_palette.jpg")

# Mesclar imagens
result2 = blend_images(img1, img2, alpha=0.7)
save_image(result2, "result_blend.jpg")
```

## Dependências
- Pillow
- Numpy

Instale com:
```bash
pip install pillow numpy
```

## Estrutura do projeto
```
image_palette_processor/
    ├── image_palette_processor/
    │   ├── __init__.py
    │   ├── palette.py
    │   ├── utils.py
    ├── examples/
    │   └── example.py
    ├── README.md
    ├── requirements.txt
    └── setup.py
```

