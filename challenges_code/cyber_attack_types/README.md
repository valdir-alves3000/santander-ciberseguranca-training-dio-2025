### **Desafio: Tipos de Ataques Cibernéticos**

#### Descrição
Proteger sistemas envolve conhecer os tipos mais comuns de ataques. Neste desafio, você deverá associar os nomes de ataques cibernéticos às suas descrições corretas, reforçando sua familiaridade com esses conceitos.

#### Entrada
A entrada consistirá no nome de um tipo de ataque, e você deverá retornar a descrição correspondente.

**Conceitos válidos:**
- `Phishing`
- `DDoS`
- `Malware`
- `Engenharia Social`

#### Saída
A saída esperada é a descrição associada ao conceito fornecido.

**Possíveis descrições:**
- "Enganar usuários para roubar informações sensíveis"
- "Atacar um serviço com muitos acessos para derrubá-lo"
- "Software malicioso projetado para causar danos"
- "Manipulação psicológica para obter acesso ou dados"

#### Exemplos

| Entrada | Saída |
|---------|-------|
| Phishing | Enganar usuários para roubar informações sensíveis |
| DDoS | Atacar um serviço com muitos acessos para derrubá-lo |
| Malware | Software malicioso projetado para causar danos |
| Engenharia Social | Manipulação psicológica para obter acesso ou dados |

#### Template da Solução

```python
entrada = input()

def descrever_ataque(ataque):
    descricoes = {
        "Phishing": "Enganar usuários para roubar informações sensíveis",
        "DDoS": "Atacar um serviço com muitos acessos para derrubá-lo", 
        "Malware": "Software malicioso projetado para causar danos",
        "Engenharia Social": "Manipulação psicológica para obter acesso ou dados"
    }
    
    return descricoes.get(ataque)

print(descrever_ataque(entrada))
```

#### Como testar:
1. Execute o código
2. Digite um dos tipos de ataque (ex: `Phishing`)
3. Verifique se a saída corresponde à definição correta

#### Conceitos abordados:
- **Phishing**: Ataque por e-mail/fake sites para roubo de dados
- **DDoS**: Ataque de negação de serviço distribuído
- **Malware**: Software malicioso (vírus, trojans, ransomware)
- **Engenharia Social**: Manipulação psicológica de pessoas

Ótimo desafio para aprender sobre as principais ameaças cibernéticas! 🔒