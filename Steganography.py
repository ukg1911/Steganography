import cv2
import numpy as np
from cryptography.fernet import Fernet
import os

# Generate or load encryption key
def load_key():
    key_file = "secret.key"
    if os.path.exists(key_file):
        with open(key_file, "rb") as key:
            return key.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

def message_to_binary(message):
    return ''.join(format(byte, '08b') for byte in message)

def binary_to_message(binary_string):
    bytes_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return bytes([int(byte, 2) for byte in bytes_list])

def hide_data(image_path, message, output_path):
    key = load_key()
    encrypted_message = encrypt_message(message, key)
    binary_message = message_to_binary(encrypted_message) + '1111111111111110'  # End delimiter
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or incorrect format.")
    
    data_index = 0
    message_length = len(binary_message)
    
    for row in image:
        for pixel in row:
            for channel in range(3):  # Iterate over R, G, B
                if data_index < message_length:
                    pixel[channel] = pixel[channel] & 254 | int(binary_message[data_index])
                    data_index += 1
                else:
                    break
    
    cv2.imwrite(output_path, image)
    print("Data successfully hidden in", output_path)

def extract_data(image_path):
    key = load_key()
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or incorrect format.")
    
    binary_message = ""
    
    for row in image:
        for pixel in row:
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)
    
    end_marker = "1111111111111110"
    binary_message = binary_message[:binary_message.find(end_marker)]
    extracted_bytes = binary_to_message(binary_message)
    
    try:
        decrypted_message = decrypt_message(extracted_bytes, key)
        print("Extracted message:", decrypted_message)
    except Exception as e:
        print("Error in decryption:", str(e))

if __name__ == "__main__":
    choice = input("Do you want to (1) Hide data or (2) Extract data? ")
    if choice == "1":
        image_path = input("Enter the path of the image: ")
        message = input("Enter the secret message: ")
        output_path = input("Enter the output image filename: ")
        hide_data(image_path, message, output_path)
    elif choice == "2":
        image_path = input("Enter the path of the encoded image: ")
        extract_data(image_path)
    else:
        print("Invalid choice.")
