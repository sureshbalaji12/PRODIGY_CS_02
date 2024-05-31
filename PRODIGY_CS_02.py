from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    encrypted_image = Image.new("RGB", image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)  # Shift each color channel by the key
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    decrypted_image = Image.new("RGB", image.size)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)  # Reverse the encryption
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (encrypt/decrypt/exit): ").lower()
        if choice == 'exit':
            break
        elif choice == 'encrypt':
            image_path = input("Enter the path to the image you want to encrypt: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypt_image(image_path, key)
        elif choice == 'decrypt':
            image_path = input("Enter the path to the image you want to decrypt: ")
            key = int(input("Enter the decryption key (an integer): "))
            decrypt_image(image_path, key)
        else:
            print("Invalid choice. Please enter 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
