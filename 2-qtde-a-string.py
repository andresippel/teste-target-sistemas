def count_a_in_string(texto):    
    count = texto.lower().count('a')
    return count

def main():
    texto = input("Informe um texto: ")
    
    count = count_a_in_string(texto)
    
    if count > 0:
        print(f"A letra 'a' ocorre {count} vezes na string.")
    else:
        print("A letra 'a' não ocorre nenhuma vez string.")

if __name__ == "__main__":
    main()
