import os

def read_file_content(filepath):
    """Lê o conteúdo de um arquivo e o retorna como uma string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo {filepath}: {e}")
        return None

def generate_combined_prompt():
    """
    Lê todos os arquivos .txt na pasta do script
    e os combina em um único prompt formatado como >mensagem>prompt>scripts.
    """
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    combined_content_parts = []
    source_counter = 1
    file_contents = {}

    # Primeiro, leia todos os arquivos .txt na pasta do script e armazene seus conteúdos com um ID de fonte
    for filename in os.listdir(script_directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(script_directory, filename)
            content = read_file_content(filepath)
            if content is not None:
                file_contents[filename] = {"content": content, "source_id": source_counter}
                source_counter += 1

    # Início da mensagem
    combined_content_parts.append(">analise esse prompt contendo as vulnerabilidades encontradas em um csv do openvas e analise se os scripts que irei enviar em seguida sao capazes de corrigir esses problemas ou nao, me informando uma porcentagem de correcao das vulnerabilidades\n")

    # Adicionar o conteúdo do 'Prompt usado.txt' como a seção de prompt
    if "Prompt usado.txt" in file_contents:
        prompt_content = file_contents["Prompt usado.txt"]["content"]
        prompt_source_id = file_contents["Prompt usado.txt"]["source_id"]
        combined_content_parts.append(f">Vulnerabilidades:\n{prompt_content}\n")

    # Adicionar os scripts como a seção de scripts
    combined_content_parts.append(">Scripts de correção:\n")
    # Ordenar os arquivos de script numericamente para clareza
    script_files = sorted([f for f in file_contents if f.startswith("1VTendoflife_") and f.endswith(".txt")],
                          key=lambda x: int(x.split('_')[-1].replace('.txt', '')))

    for filename in script_files:
        script_content = file_contents[filename]["content"]
        script_source_id = file_contents[filename]["source_id"]
        # Mantendo o formato original de upload de arquivo para os scripts
        combined_content_parts.append(f"{{type: uploaded file\nfileName: {filename}\nfullContent:\n{script_content}}}\n")

    return "".join(combined_content_parts) # Usar "".join para evitar nova linha no final

# Exemplo de uso:
if __name__ == "__main__":
    full_prompt = generate_combined_prompt()
    if full_prompt:
        print("Conteúdo combinado para o prompt:")
        print(full_prompt)

        # Opcional: Salvar o prompt combinado em um arquivo
        with open("combined_analysis_prompt.txt", "w", encoding='utf-8') as f:
            f.write(full_prompt)
        print("\nConteúdo combinado salvo em 'combined_analysis_prompt.txt'")
