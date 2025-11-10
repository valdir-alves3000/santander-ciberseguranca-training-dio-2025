import os
from cryptography.fernet import Fernet

# Carrega a chave de criptografia do arquivo para descriptografia
def load_key():
    return open("key.key", "rb").read()

# Descriptografa um arquivo individual usando a chave fornecida
def decrypt_file(filename,key):
    f =Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        decrypted_data = f.decrypt(file_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Encontra todos os arquivos em um diretório que devem ser descriptografados
def find_files(directory):
    list = []
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            if name != "ransomware.py" and not name.endswith(".key"):
                list.append(path)
    return list


# Função principal que orquestra todo o processo de descriptografia
def main():
    key = load_key()
    files = find_files("test_files")
    for file in files:
        decrypt_file(file, key)
    print("Arquivos restaurados com sucesso")

if __name__ == "__main__":
    main()