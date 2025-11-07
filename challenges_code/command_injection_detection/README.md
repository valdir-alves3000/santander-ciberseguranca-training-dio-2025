### **Desafio: Detecção de Injeção de Comandos**

#### Descrição
Em cibersegurança, é fundamental monitorar a entrada de dados fornecidos pelo usuário para prevenir injeção de comandos. Comandos maliciosos podem ser executados no sistema, comprometendo sua segurança. Neste desafio, você deve criar uma lógica para identificar se um comando fornecido pelo usuário contém caracteres que possam ser usados para realizar injeções de comandos.

O objetivo é identificar se o comando fornecido contém caracteres frequentemente utilizados para executar múltiplos comandos de forma encadeada ou maliciosa, como `;`, `&`, `|`, e `$`.

#### Regras de Detecção
- O comando será considerado suspeito se contiver qualquer um dos seguintes caracteres: `;`, `&`, `|`, ou `$`
- Se o comando contiver qualquer um desses caracteres, será considerado suspeito e o sistema deve alertar sobre um possível risco de injeção de comando

#### Entrada
A entrada será composta por uma string representando o comando fornecido pelo usuário.

#### Saída
- `"Comando Suspeito"` se o comando contiver qualquer um dos caracteres mencionados
- `"Comando Seguro"` caso contrário

#### Exemplos

| Entrada | Saída |
|---------|-------|
| ls -la | Comando Seguro |
| rm -rf / | Comando Seguro |
| cat file.txt; rm -rf / | Comando Suspeito |
| echo $PATH | Comando Suspeito |
| whoami && ls | Comando Suspeito |
| pwd | Comando Seguro |

#### Template da Solução

```python
def verificar_comando(comando):
    caracteres_suspeitos = [';', '&', '|', '$']
    
    for caracter in caracteres_suspeitos:
        if caracter in comando:
            return "Comando Suspeito"
    
    return "Comando Seguro"

comando_usuario = input()

print(verificar_comando(comando_usuario))
```

#### Como testar:
1. Execute o código
2. Digite um comando para análise (ex: `ls -la` ou `cat file.txt; rm -rf /`)
3. Verifique se a saída identifica corretamente comandos seguros ou suspeitos

#### Conceitos abordados:
- **Injeção de comandos**: Ataque onde comandos maliciosos são executados no sistema
- **Validação de entrada**: Verificação de caracteres perigosos em entradas do usuário
- **Caracteres perigosos**: `;` (sequência), `&` (background), `|` (pipe), `$` (variáveis)
- **Segurança de aplicações**: Prevenção contra execução de comandos não autorizados

Ótimo desafio para entender princípios de validação de entrada e prevenção contra injeção de comandos! 🔒
