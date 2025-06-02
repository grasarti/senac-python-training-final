try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou: {numero}")
    
except ValueError:
    print("Erro: Você não digitou um número inteiro")
    

try:
    num_str = input("Digite um número: ")
    num_int = int(num_str)
    resultado = 10 /num_int
    print(f"10 dividido por {num_int} é {resultado}")
    
except ValueError:
    print("Erro: Entrada inválida. Por favor digite um número.")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

except Exception as e:
    print(f"Ocorreu um erro inesperado {e}")

# else só vai ser executado se não houve nenhuma exceção
else:
    print("Deu tudo certo")

# executa mesmo que tenha erro ou não no try
finally:
    num_str = input("Digite um número: ")
    
    
arquivo = None;

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print("Arquivo lido com sucesso!")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado")

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")

else:
    print("Processamento do arquivo concluído com sucesso")
    
finally:
    if arquivo:
        arquivo.close()
        print("Arquivo fechado.")
        
    