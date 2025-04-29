import os
from PIL import Image

# Updated version with correct compression

input_folder = r"your\input\folder\path"    
output_folder = r"your\output\folder\path"    

def convert_to_jpeg(input_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    ext = ext.lower()

    if ext == '.svg':
        print(f"Skipping SVG file '{filename}' (requires special handling).")
        return

    original_size = os.path.getsize(input_path)

    img = Image.open(input_path)

    # Convert to RGB if needed
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    output_path = os.path.join(output_folder, f"{name}.jpeg")
    img.save(output_path, "JPEG", quality=85, optimize=True)

    new_size = os.path.getsize(output_path)

    reduction = 100 * (original_size - new_size) / original_size
    print(f"Converted '{filename}' ({ext[1:]}) ➔ JPEG. Size reduced by {reduction:.2f}%.")

def batch_convert(input_folder, output_folder):
    supported_extensions = ('.png', '.jpg', '.jpeg', '.webp')

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(supported_extensions + ('.svg',)):
                input_path = os.path.join(root, file)
                convert_to_jpeg(input_path, output_folder)

if __name__ == "__main__":
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
    else:
        batch_convert(input_folder, output_folder)
