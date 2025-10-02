from image_palette_processor import load_image, save_image, transfer_palette, blend_images

# Carregar imagens
img1 = load_image("examples/source.jpg")
img2 = load_image("examples/target.jpg")

# Transferir paleta
result1 = transfer_palette(img1, img2)
save_image(result1, "examples/result_palette.jpg")

# Mesclar imagens
result2 = blend_images(img1, img2, alpha=0.6)
save_image(result2, "examples/result_blend.jpg")

print("Imagens processadas e salvas em /examples/")
