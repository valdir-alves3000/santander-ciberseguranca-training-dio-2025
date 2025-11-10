# Simulador de Ransomware

⚠️ **AVISO IMPORTANTE**: Este projeto é estritamente para fins educacionais e de pesquisa em segurança cibernética. O uso malicioso de ransomware é crime.

## Descrição

Este projeto simula o comportamento de um ransomware para fins educacionais, demonstrando como a criptografia pode ser usada para sequestrar dados. Inclui tanto a funcionalidade de criptografia quanto descriptografia.

## Estrutura do Projeto

```
projeto/
├── ransomware.py          # Script de criptografia (simulação)
├── decrypt.py            # Script de descriptografia
├── key.key               # Chave de criptografia (gerada automaticamente)
├── LEIA ISSO.txt         # Mensagem de resgate (gerada automaticamente)
└── test_files/           # Diretório com arquivos de teste
```

## Pré-requisitos

- Python 3.6+
- Biblioteca cryptography

## Configuração do Ambiente

```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate

# No Windows use:
# .venv\Scripts\activate

# Atualizar pip e instalar dependências
pip install --upgrade pip
pip install cryptography
```

## Como Usar

### 1. Preparação dos Arquivos de Teste

```bash
# Criar diretório de teste
mkdir test_files

# Criar alguns arquivos de exemplo
echo "Este é um arquivo de teste 1" > test_files/documento1.txt
echo "Arquivo de teste 2 com conteúdo importante" > test_files/planilha.csv
echo "Dados confidenciais para teste" > test_files/relatorio.pdf
```

### 2. Executar a Simulação de Ransomware

```bash
python ransomware.py
```

**Saída esperada:**
```
Ransomware executado! Arquivos criptografados!
```

**O que acontece:**
- Gera uma chave de criptografia (`key.key`)
- Criptografa todos os arquivos no diretório `test_files`
- Cria uma mensagem de resgate (`LEIA ISSO.txt`)

### 3. Verificar os Arquivos Criptografados

```bash
# Tentar ler um arquivo criptografado
cat test_files/documento1.txt
```

O conteúdo aparecerá como dados binários criptografados.

### 4. Recuperar os Arquivos (Descriptografia)

```bash
python decrypt.py
```

**Saída esperada:**
```
Arquivos restaurados com sucesso
```

### 5. Verificar se os Arquivos Foram Restaurados

```bash
# Verificar o conteúdo dos arquivos
cat test_files/documento1.txt
cat test_files/planilha.csv
```

Os arquivos devem retornar ao seu conteúdo original legível.

## Funcionalidades

### ransomware.py
- `generate_key()`: Gera chave de criptografia
- `encrypt_file()`: Criptografa arquivos individuais
- `find_files()`: Localiza arquivos no diretório especificado
- `create_rescue_message()`: Cria mensagem de resgate

### decrypt.py
- `decrypt_file()`: Descriptografa arquivos individuais
- `find_files()`: Localiza arquivos criptografados
- Usa a mesma chave gerada pelo ransomware

## Arquivos Gerados

- `key.key`: Chave de criptografia (NUNCA compartilhe este arquivo)
- `LEIA ISSO.txt`: Mensagem simulada de resgate

## ⚠️ Alertas de Segurança

1. **USO APENAS EDUCACIONAL**: Nunca execute em sistemas de produção
2. **AMBIENTE ISOLADO**: Execute apenas em máquinas virtuais ou containers
3. **BACKUP**: Sempre tenha backup dos seus dados importantes
4. **LEGALIDADE**: Verifique as leis da sua região antes de usar

## Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'cryptography'"
```bash
pip install cryptography
```

### Erro: "No such file or directory: 'test_files'"
```bash
mkdir test_files
# Crie alguns arquivos de teste dentro da pasta
```

### Arquivo key.key não encontrado
- Execute `ransomware.py` primeiro para gerar a chave
- A chave é necessária para a descriptografia

## Aprendizados

Este projeto demonstra:
- Como a criptografia simétrica funciona
- Vulnerabilidades de sistemas de arquivos
- Importância de backups regulares
- Mecanismos de proteção contra ransomware

## Licença

Este projeto é para fins educacionais. Use com responsabilidade.

---

**Nota**: Considere renomear `ransomware.py` para algo como `file_encryptor.py` ou `crypto_simulator.py` para evitar detecções incorretas por software de segurança.