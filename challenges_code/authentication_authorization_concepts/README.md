### **Desafio: Conceitos de Autenticação e Autorização**

#### Descrição
Na cibersegurança, é fundamental entender os conceitos de autenticação e autorização, pois eles ajudam a proteger dados e controlar acessos a sistemas. Neste desafio, você deve associar os conceitos básicos às suas definições corretas.

#### Entrada
A entrada consistirá no nome do conceito, e sua tarefa será retornar a descrição correspondente. 

**Conceitos válidos:**
- `Autenticação`
- `Autorização` 
- `MFA`
- `OAuth`

#### Saída
A saída esperada é a descrição associada ao conceito fornecido.

**Possíveis descrições:**
- "Verificação da identidade de um usuário"
- "Permissão para acessar recursos específicos"
- "Verificação usando múltiplos fatores de segurança"
- "Padrão aberto para delegar acesso sem compartilhar senha"

#### Exemplos

| Entrada | Saída |
|---------|-------|
| Autenticação | Verificação da identidade de um usuário |
| MFA | Verificação usando múltiplos fatores de segurança |
| OAuth | Padrão aberto para delegar acesso sem compartilhar senha |
| Autorização | Permissão para acessar recursos específicos |

#### Template da Solução

```python
# Entrada do conceito
entrada = input()

def descrever_conceito(conceito):
    # Dicionário com os conceitos e suas descrições
    descricoes = {
        "Autenticação": "Verificação da identidade de um usuário",
        "Autorização": "Permissão para acessar recursos específicos", 
        "MFA": "Verificação usando múltiplos fatores de segurança",
        "OAuth": "Padrão aberto para delegar acesso sem compartilhar senha"
    }
    
    return descricoes.get(conceito)

# Saída da descrição correspondente
print(descrever_conceito(entrada))
```

#### Como testar:
1. Execute o código
2. Digite um dos conceitos (ex: `Autenticação`)
3. Verifique se a saída corresponde à definição correta

#### Conceitos abordados:
- **Autenticação**: Confirmar quem você é
- **Autorização**: Determinar o que você pode acessar  
- **MFA**: Camada extra de segurança com múltiplos fatores
- **OAuth**: Protocolo para autorização segura entre aplicações

Ótimo desafio para consolidar esses conceitos essenciais em cibersegurança! 🔐