### **Desafio: Sistema de Bloqueio por Tentativas Consecutivas**

#### Descrição
Em sistemas de autenticação segura, é comum bloquear contas após múltiplas tentativas de login inválidas consecutivas. Esse mecanismo evita ataques de força bruta e protege a conta do usuário.

Neste desafio, você deverá verificar uma lista de tentativas de login e identificar se a conta deve ser bloqueada com base em tentativas falhas seguidas.

Uma conta deve ser bloqueada se houver 3 ou mais tentativas consecutivas de falha.

#### Entrada
Uma lista com strings representando o resultado de tentativas de login. Cada string pode ser:

- `"sucesso"`
- `"falha"`

As tentativas são fornecidas em ordem cronológica, separadas por vírgula.

#### Saída
- `"Conta Bloqueada"`, se houver 3 ou mais falhas consecutivas
- `"Acesso Normal"`, caso contrário

#### Exemplos

| Entrada | Saída |
|---------|-------|
| sucesso, falha, falha, falha | Conta Bloqueada |
| falha, falha, sucesso, falha | Acesso Normal |
| falha, falha, falha, sucesso | Conta Bloqueada |
| sucesso, sucesso, falha, sucesso | Acesso Normal |

#### Template da Solução

```python
entrada = input().strip()  

tentativas = [item.strip().lower() for item in entrada.split(',')]

falhas_consecutivas = 0

for tentativa in tentativas:
    if tentativa == "falha":
        falhas_consecutivas += 1
        
        if falhas_consecutivas >= 3:
            print("Conta Bloqueada")
            break
    else:
        falhas_consecutivas = 0  
else:
    print("Acesso Normal")
```

#### Como testar:
1. Execute o código
2. Digite uma sequência de tentativas separadas por vírgula (ex: `falha, falha, falha`)
3. Verifique se a saída corresponde ao cenário de bloqueio ou acesso normal

#### Conceitos abordados:
- **Segurança de autenticação**: Proteção contra ataques de força bruta
- **Controle de acesso**: Mecanismos de bloqueio por tentativas consecutivas
- **Análise sequencial**: Verificação de padrões em sequências temporais

Ótimo desafio para entender mecanismos de proteção contra ataques de repetição! 🔐
