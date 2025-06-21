class Funcionario:
    def __init__(self, numero_funcional, nome, salario, email=None):
        self.numero_funcional = numero_funcional
        self.nome = nome
        self.salario = salario
        self.email = email

    def __str__(self):
        return f"Número: {self.numero_funcional}, Nome: {self.nome}, Salário: R${self.salario:.2f}"


class Projeto:
    def __init__(self, nome, data_inicio, data_termino, tempo_estimado, valor_estimado, numero_funcionario_responsavel):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.tempo_estimado = tempo_estimado
        self.valor_estimado = valor_estimado
        self.numero_funcionario_responsavel = numero_funcionario_responsavel

    def __str__(self):
        status = "Finalizado" if self.data_termino else "Em andamento"
        return (f"Projeto: {self.nome}, Início: {self.data_inicio}, Término: {self.data_termino or '---'}, "
                f"Estimado: {self.tempo_estimado} meses, Valor: R${self.valor_estimado:.2f}, "
                f"Resp: {self.numero_funcionario_responsavel}, Status: {status}")


MAX_FUNCIONARIOS = 500
MAX_PROJETOS = 2000

funcionarios = []
projetos = []

funcionarios.append(Funcionario(101, "João Silva", 12000.00, "joao.silva@empresa.com"))
funcionarios.append(Funcionario(102, "Maria Souza", 9000.00, "maria.souza@empresa.com"))
funcionarios.append(Funcionario(103, "Pedro Santos", 15000.00, "pedro.santos@empresa.com"))

projetos.append(Projeto("Projeto Alpha", "01/01/2025", "", 12, 600000.00, 101))
projetos.append(Projeto("Projeto Beta", "15/03/2024", "20/06/2025", 14, 450000.00, 102))
projetos.append(Projeto("Projeto Gama", "10/07/2023", "10/12/2023", 5, 700000.00, 103))
projetos.append(Projeto("Projeto Delta", "01/05/2025", "", 6, 800000.00, 101))

def busca_binaria_funcionario(funcionarios, numero_funcional):
    esquerda, direita = 0, len(funcionarios) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if funcionarios[meio].numero_funcional == numero_funcional:
            return meio
        elif funcionarios[meio].numero_funcional < numero_funcional:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def busca_binaria_projeto(projetos, nome_projeto):
    esquerda, direita = 0, len(projetos) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if projetos[meio].nome == nome_projeto:
            return meio
        elif projetos[meio].nome < nome_projeto:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def inserir_funcionario(funcionarios, novo_funcionario):
    if len(funcionarios) >= MAX_FUNCIONARIOS:
        print("❌ Limite de funcionários atingido.")
        return

    if busca_binaria_funcionario(funcionarios, novo_funcionario.numero_funcional) != -1:
        print("❌ Já existe um funcionário com esse número funcional.")
        return

    i = 0
    while i < len(funcionarios) and funcionarios[i].numero_funcional < novo_funcionario.numero_funcional:
        i += 1
    funcionarios.insert(i, novo_funcionario)
    print("✅ Funcionário inserido com sucesso.")

def remover_funcionario(funcionarios, numero_funcional):
    index = busca_binaria_funcionario(funcionarios, numero_funcional)
    if index == -1:
        print("❌ Funcionário não encontrado.")
    else:
        del funcionarios[index]
        print("✅ Funcionário removido com sucesso.")

def alterar_funcionario(funcionarios, numero_funcional, novo_nome=None, novo_salario=None):
    index = busca_binaria_funcionario(funcionarios, numero_funcional)
    if index == -1:
        print("❌ Funcionário não encontrado.")
    else:
        if novo_nome is not None:
            funcionarios[index].nome = novo_nome
        if novo_salario is not None:
            funcionarios[index].salario = novo_salario
        print("✅ Funcionário alterado com sucesso.")

def listar_todos_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("📋 Lista completa de funcionários:")
        for f in funcionarios:
            print(f)

def insertion_sort_salarios(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j].salario < atual.salario:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual

def listar_funcionarios_salario_alto(funcionarios):
    filtrados = [f for f in funcionarios if f.salario > 10000]
    insertion_sort_salarios(filtrados)
    if not filtrados:
        print("⚠️ Nenhum funcionário com salário acima de R$10.000.")
    else:
        print("📋 Funcionários com salário acima de R$10.000 (ordem decrescente):")
        for f in filtrados:
            print(f"Nome: {f.nome}, Salário: R${f.salario:.2f}")

def inserir_projeto(projetos, novo_projeto):
    if len(projetos) >= MAX_PROJETOS:
        print("❌ Limite de projetos atingido.")
        return

    if busca_binaria_projeto(projetos, novo_projeto.nome) != -1:
        print("❌ Já existe um projeto com esse nome.")
        return

    i = 0
    while i < len(projetos) and projetos[i].nome < novo_projeto.nome:
        i += 1
    projetos.insert(i, novo_projeto)
    print("✅ Projeto inserido com sucesso.")

def merge_sort_projetos_por_valor(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort_projetos_por_valor(esquerda)
        merge_sort_projetos_por_valor(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i].valor_estimado < direita[j].valor_estimado:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

def listar_projetos_valor_alto_em_andamento(projetos):
    filtrados = [p for p in projetos if p.data_termino == "" and p.valor_estimado > 500000]
    merge_sort_projetos_por_valor(filtrados)
    if not filtrados:
        print("⚠️ Nenhum projeto em andamento com valor acima de R$500.000.")
    else:
        print("📋 Projetos em andamento com valor > R$500.000 (ordenados por valor):")
        for p in filtrados:
            print(p)

def data_para_meses(data_str):
    if not data_str:
        return None
    dia, mes, ano = map(int, data_str.split("/"))
    return ano * 12 + mes

def listar_projetos_atrasados(projetos, mes_atual, ano_atual):
    data_atual_em_meses = ano_atual * 12 + mes_atual
    atrasados = []
    for p in projetos:
        inicio_em_meses = data_para_meses(p.data_inicio)
        estimado_fim = inicio_em_meses + p.tempo_estimado

        if p.data_termino == "":
            if data_atual_em_meses > estimado_fim:
                atraso = data_atual_em_meses - estimado_fim
                atrasados.append((p, "Em andamento", atraso))
        else:
            fim_real = data_para_meses(p.data_termino)
            if fim_real > estimado_fim:
                atraso = fim_real - estimado_fim
                atrasados.append((p, "Finalizado", atraso))

    for i in range(1, len(atrasados)):
        atual = atrasados[i]
        j = i - 1
        while j >= 0 and atrasados[j][2] < atual[2]:
            atrasados[j + 1] = atrasados[j]
            j -= 1
        atrasados[j + 1] = atual

    if not atrasados:
        print("✅ Nenhum projeto com atraso detectado.")
    else:
        print("📋 Projetos com atraso (ordem decrescente do atraso):")
        for projeto, status, atraso in atrasados:
            print(f"{projeto.nome} - {status} - Atraso: {atraso} mês(es)")

def get_responsaveis_em_andamento(projetos):
    responsaveis = set()
    for p in projetos:
        if p.data_termino == "":
            responsaveis.add(p.numero_funcionario_responsavel)
    return responsaveis

def get_nomes_funcionarios_por_numeros(numeros_funcionais, funcionarios):
    nomes = []
    for numero in numeros_funcionais:
        index = busca_binaria_funcionario(funcionarios, numero)
        if index != -1:
            nomes.append(funcionarios[index].nome)
    return nomes

def insertion_sort_alfabetica(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual

def listar_responsaveis_por_projetos_em_andamento(funcionarios, projetos):
    numeros = get_responsaveis_em_andamento(projetos)
    nomes = get_nomes_funcionarios_por_numeros(numeros, funcionarios)

    if not nomes:
        print("⚠️ Nenhum responsável por projetos em andamento.")
        return

    insertion_sort_alfabetica(nomes)

    print("📋 Responsáveis por projetos em andamento (ordem alfabética):")
    for nome in nomes:
        print(f"- {nome}")

TAM_HASH = 101

class HashEntry:
    def __init__(self, email=None):
        self.email = email
        self.ocupado = False

tabela_hash = [HashEntry() for _ in range(TAM_HASH)]

def hash_function(email):
    h = 0
    for c in email:
        h = (h * 31 + ord(c)) % TAM_HASH
    return h

def inserir_email(tabela, email):
    index = hash_function(email)
    for i in range(TAM_HASH):
        pos = (index + i) % TAM_HASH
        if not tabela[pos].ocupado:
            tabela[pos].email = email
            tabela[pos].ocupado = True
            return True
        elif tabela[pos].email == email:
            return True
    return False

def buscar_email(tabela, email):
    index = hash_function(email)
    for i in range(TAM_HASH):
        pos = (index + i) % TAM_HASH
        if not tabela[pos].ocupado:
            return None
        if tabela[pos].email == email:
            return tabela[pos].email
    return None

def inserir_emails_gerentes(projetos, tabela, funcionarios):
    for p in projetos:
        idx_func = busca_binaria_funcionario(funcionarios, p.numero_funcionario_responsavel)
        if idx_func != -1:
            email = getattr(funcionarios[idx_func], 'email', None)
            if email:
                inserir_email(tabela, email)

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Inserir funcionário")
        print("2. Remover funcionário")
        print("3. Alterar funcionário")
        print("4. Buscar funcionário por número funcional")
        print("5. Listar funcionários com salário > R$10.000")
        print("6. Listar todos os funcionários")
        print("7. Inserir projeto")
        print("8. Listar projetos em andamento com valor > R$500.000")
        print("9. Listar projetos com atraso")
        print("10. Listar responsáveis por projetos em andamento")
        print("11. Inserir e-mails de gerente")
        print("12. Buscar e-mail")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                numero = int(input("Número funcional: "))
                nome = input("Nome: ")
                salario = float(input("Salário: "))
                email = input("Email (opcional): ").strip()
                if email == "":
                    email = None
                f = Funcionario(numero, nome, salario, email)
                inserir_funcionario(funcionarios, f)
            except Exception as e:
                print("Erro na entrada de dados:", e)

        elif opcao == '2':
            try:
                numero = int(input("Número funcional do funcionário a remover: "))
                remover_funcionario(funcionarios, numero)
            except:
                print("Entrada inválida.")

        elif opcao == '3':
            try:
                numero = int(input("Número funcional do funcionário a alterar: "))
                novo_nome = input("Novo nome (enter para não alterar): ").strip()
                novo_salario_input = input("Novo salário (enter para não alterar): ").strip()
                novo_salario = float(novo_salario_input) if novo_salario_input else None
                alterar_funcionario(funcionarios, numero, novo_nome if novo_nome else None, novo_salario)
            except:
                print("Entrada inválida.")

        elif opcao == '4':
            try:
                numero = int(input("Número funcional para busca: "))
                idx = busca_binaria_funcionario(funcionarios, numero)
                if idx == -1:
                    print("Funcionário não encontrado.")
                else:
                    print(funcionarios[idx])
            except:
                print("Entrada inválida.")

        elif opcao == '5':
            listar_funcionarios_salario_alto(funcionarios)

        elif opcao == '6':
            listar_todos_funcionarios(funcionarios)

        elif opcao == '7':
            try:
                nome = input("Nome do projeto: ")
                data_inicio = input("Data início (DD/MM/AAAA): ")
                data_termino = input("Data término (DD/MM/AAAA ou vazio se em andamento): ").strip()
                tempo_estimado = int(input("Tempo estimado (meses): "))
                valor_estimado = float(input("Valor estimado: "))
                num_resp = int(input("Número funcional do responsável: "))
                p = Projeto(nome, data_inicio, data_termino, tempo_estimado, valor_estimado, num_resp)
                inserir_projeto(projetos, p)
            except Exception as e:
                print("Erro na entrada de dados:", e)

        elif opcao == '8':
            listar_projetos_valor_alto_em_andamento(projetos)

        elif opcao == '9':
            try:
                mes_atual = int(input("Mês atual (1-12): "))
                ano_atual = int(input("Ano atual (ex: 2025): "))
                listar_projetos_atrasados(projetos, mes_atual, ano_atual)
            except:
                print("Entrada inválida.")

        elif opcao == '10':
            listar_responsaveis_por_projetos_em_andamento(funcionarios, projetos)

        elif opcao == '11':
            inserir_emails_gerentes(projetos, tabela_hash, funcionarios)
            print("✅ E-mails inseridos na tabela hash.")

        elif opcao == '12':
            email_busca = input("Informe o e-mail para busca: ")
            resultado = buscar_email(tabela_hash, email_busca)
            if resultado:
                print(f"E-mail encontrado: {resultado}")
            else:
                print("E-mail não encontrado.")

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
