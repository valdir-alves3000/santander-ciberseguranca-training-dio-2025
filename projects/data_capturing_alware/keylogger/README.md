# Keylogger 

## 📋 Índice
- [Descrição](#descrição)
- [Aviso Legal](#aviso-legal)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Uso](#uso)
- [Solução de Problemas](#solução-de-problemas)
- [Desinstalação](#desinstalação)

## Descrição

Este projeto consiste em dois keyloggers desenvolvidos em Python com arquitetura modular:

- **`main.pyw`** - Keylogger básico com salvamento local
- **`keylogger.pyw`** - Keylogger avançado com envio de email

Ambos executam em segundo plano capturando e registrando todas as teclas pressionadas.

## Aviso Legal

**🔒 ESTE SOFTWARE DEVE SER USADO APENAS PARA FINS EDUCACIONAIS E LEGÍTIMOS:**

- Monitoramento de seus próprios sistemas
- Estudos de segurança cibernética
- Desenvolvimento de ferramentas de diagnóstico
- Testes de penetração autorizados
- Com consentimento explícito do usuário monitorado

**🚫 É ILEGAL USAR ESTE SOFTWARE PARA:**

- Monitorar usuários sem consentimento
- Coletar informações pessoais sem autorização
- Qualquer atividade maliciosa ou fraudulenta
- Violação de privacidade

**O desenvolvedor não se responsabiliza pelo uso indevido desta ferramenta.**

## Funcionalidades

### ✅ Funcionalidades Comuns
- Execução em segundo plano (.pyw)
- Captura completa de todas as teclas pressionadas
- Gravação sequencial em arquivo `log.txt`
- Suporte a teclas especiais (Shift, Ctrl, Alt, etc.)
- Suporte ao teclado numérico
- Detecção de sequência "hacker_discovered" para encerramento
- Ignora teclas de modificação desnecessárias

### 🚀 Funcionalidades do Keylogger com Email
- Envio automático de logs por email a cada 60 segundos
- Configuração flexível de servidor SMTP
- Tratamento de erros robusto
- Log em tempo real com timestamp


## Pré-requisitos

- **Python 3.6** ou superior
- **Bibliotecas necessárias:**
  - `pynput` - Captura de teclas
  - Para keylogger com email: acesso SMTP

## Instalação e Configuração

### 1. Configuração do Ambiente

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Arquivo requirements.txt
```txt
pynput==1.7.6
secure-smtplib==0.1.1
```

### 3. Configuração do Email (Opcional - para keylogger.pyw)

Edite `src/config/settings.py`:
```python
# Configurações de Email
EMAIL_ORIGIN = "seu_email@gmail.com"
EMAIL_DESTINATION = "email_destino@gmail.com"
PASS_EMAIL = "sua_senha_de_app"
EMAIL_INTERVAL = 60  # segundos
```

**📧 Para configurar o Gmail:**
1. Ative a verificação em 2 etapas
2. Gere uma senha de app
3. Use a senha de 16 caracteres no campo `PASS_EMAIL`

## Uso

### 🔧 Keylogger Básico (main.pyw)

```bash
# Executar
python src/main.pyw

# Funcionalidades:
# - Salva teclas em log.txt
# - Para com "hacker_discovered"
# - Execução em segundo plano
```

### 🚀 Keylogger com Email (keylogger.pyw)

```bash
# Executar
python src/keylogger.pyw

# Funcionalidades:
# - Salva teclas em log.txt
# - Envia email a cada 60 segundos
# - Para com "hacker_discovered"
```

### 🎯 Como Parar os Programas

1. **Digite a sequência:** `hacker_discovered`
2. **Gerenciador de Tarefas:** Encerre `pythonw.exe`
3. **PowerShell:**
   ```powershell
   taskkill /f /im pythonw.exe
   ```

### 🎹 Personalização de Teclas

Edite `src/config/key_mappings.py` para:
- Adicionar/remover teclas ignoradas
- Modificar mapeamento de teclas especiais
- Configurar teclado numérico

## Desinstalação

### 1. Parar os Processos
```powershell
# PowerShell
taskkill /f /im pythonw.exe
Get-Process python* | Stop-Process
```

### 2. Remover Arquivos
```bash
# Remover ambiente virtual
deactivate
rmdir /s .venv  # Windows
rm -rf .venv    # Linux/Mac

# Remover logs (opcional)
del log.txt
```

### 3. Limpeza de Registro (Windows)
- Verifique a pasta de inicialização
- Remova referências do Agendador de Tarefas


## 🔐 Considerações de Segurança

- **Use em ambientes controlados**
- **Obtenha consentimento explícito**
- **Mantenha os logs seguros**
- **Delete os dados após uso**

## 📄 Licença

Este projeto é para fins educacionais. Use com responsabilidade.


**⚠️ LEMBRETE: Respeite a privacidade alheia e use esta ferramenta apenas para fins legítimos e autorizados.**
