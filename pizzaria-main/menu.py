import customtkinter as ctk
import json
from tkinter import messagebox

# Carregar configurações do JSON
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)



class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, item):
        self.itens.append(item)
    
    def exibir_itens(self):
        return "\n".join(self.itens) if self.itens else "Carrinho vazio."
    
    def limpar(self):
        self.itens.clear()
    
    def confirmar_compra(self):
        if not self.itens:
            messagebox.showinfo("Carrinho", "O carrinho está vazio!")
            return
        messagebox.showinfo("Compra Confirmada", "Seu pedido foi finalizado com sucesso!")
        self.limpar()

carrinho = Carrinho()



class FrameDeTamanhos(ctk.CTkFrame):
    def __init__(self, app, titulo, tamanhos_dict):
        super().__init__(app)
        self.app = app
        self.titulo = titulo
        self.tamanhos = tamanhos_dict
        self.valores = list(tamanhos_dict.values())  # Obtém os limites de sabores
        self.tamanho = ctk.IntVar(value=-1)
        self.max_sabores = 0  # Variável para armazenar o número máximo de sabores permitido

        self.titulo_frame = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="sew")
        
        for i, (nome, valor) in enumerate(tamanhos_dict.items()):
            radiobutton = ctk.CTkRadioButton(
                self, 
                text=f'{nome}: {(i+1)*4} fatias, até {valor} sabores', 
                variable=self.tamanho, 
                value=i, 
                command=self.acessar_Tamanho
            )
            radiobutton.grid(row=i+1, column=0, columnspan=2, padx=10, pady=5, sticky="sew")

    def acessar_Tamanho(self):
        tamanho = self.tamanho.get()
        if tamanho != -1:
            self.max_sabores = self.valores[tamanho]  # Define o limite de sabores baseado no tamanho
            self.app.limitarSabores(self.max_sabores)  # Chama a função para limitar a escolha de sabores
        self.app.atualizarPreco_total()

    def confirmarEscolha(self):
        if self.tamanho.get() == -1:
            messagebox.showerror('ERRO', 'É obrigatório escolher algum tamanho de pizza.')
            return False
        return True



class FrameDeSabores(ctk.CTkFrame):
    def __init__(self, app, titulo, sabores):
        super().__init__(app)
        self.app = app
        self.vars = {}

        self.titulo_frame = ctk.CTkLabel(self, text=titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="sew")
        
        self.sabores = sabores
        
        for i, (sabor, valor) in enumerate(self.sabores.items(), start=1):
            self.vars[sabor] = ctk.IntVar(value=0)
            ctk.CTkCheckBox(self, text=f"{sabor} - R${valor}", variable=self.vars[sabor],
                            onvalue=1, offvalue=0, command=self.verificarLimiteSabores).grid(row=i, column=0, padx=10, pady=5, sticky="we")

    def verificarLimiteSabores(self):
        # Verificar o número de sabores selecionados
        selected_sabores = [sabor for sabor, var in self.vars.items() if var.get() == 1]
        max_sabores = self.app.frame_de_tamanhos.max_sabores

        if len(selected_sabores) > max_sabores:
            # Excedeu o limite, desmarcar todos os sabores e mostrar aviso
            for var in self.vars.values():
                var.set(0)
            if max_sabores == 0:
                messagebox.showwarning("Limite Excedido", f"Você deve escolher um tamanho de pizza primeiro antes de selecionar um sabor.")
            else:
                messagebox.showwarning("Limite Excedido", f"Você não pode escolher mais do que {max_sabores} sabores para este tamanho de pizza.")
        
        # Atualiza o valor total ao vivo
        self.app.atualizarPreco_total()

    def verificarSaboresMarcados(self):
        return any(var.get() == 1 for var in self.vars.values())



class FrameDeAdicionais(ctk.CTkFrame):
    def __init__(self, app, titulo, adicionais):
        super().__init__(app)
        self.app = app
        
        self.titulo_frame = ctk.CTkLabel(self, text=titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="sew")

        self.adicionais = adicionais
        self.comboboxes = {}
        
        for i, (adicional, valor) in enumerate(self.adicionais.items(), start=1):
            ctk.CTkLabel(self, text=f"{adicional} - R${valor}").grid(row=i, column=0, padx=10, pady=5, sticky="we")
            combobox = ctk.CTkComboBox(self, values=[str(i) for i in range(11)], state="readonly", command=self.app.atualizarPreco_total)
            combobox.set("0")
            combobox.grid(row=i, column=1, padx=10, pady=5, sticky='we')
            self.comboboxes[adicional] = combobox



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Menu')
        self.geometry('900x600')
        
        self.total_label = ctk.CTkLabel(self, text='Total: R$0.00', font=("Arial", 14))
        self.total_label.grid(row=4, column=0, columnspan=4, padx=10, pady=5, sticky="sew")
        
        self.frame_de_tamanhos = FrameDeTamanhos(self, tamanhos_dict=config["tamanhos"], titulo='Escolha o tamanho da pizza:')
        self.frame_de_tamanhos.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.frame_de_sabores = FrameDeSabores(self, titulo='Escolha seus sabores', sabores=config["sabores"])
        self.frame_de_sabores.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        self.frame_de_adicionais = FrameDeAdicionais(self, titulo='Escolha seus adicionais', adicionais=config["adicionais"])
        self.frame_de_adicionais.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        
        self.botao_confirmar = ctk.CTkButton(self, text='Adicionar ao Carrinho', command=self.adicionar_ao_carrinho)
        self.botao_confirmar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="sew")
        
        self.botao_ver_carrinho = ctk.CTkButton(self, text='Ver Carrinho', command=self.ver_carrinho)
        self.botao_ver_carrinho.grid(row=3, column=2, padx=10, pady=10, sticky="sew")
        
        self.botao_limpar_carrinho = ctk.CTkButton(self, text='Limpar Carrinho', command=self.limpar_carrinho)
        self.botao_limpar_carrinho.grid(row=5, column=0, padx=10, pady=10, sticky="sew")
        
        self.botao_confirmar_compra = ctk.CTkButton(self, text='Confirmar Compra', command=self.confirmar_compra)
        self.botao_confirmar_compra.grid(row=5, column=2, padx=10, pady=10, sticky="sew")
    
    def atualizarPreco_total(self):
        total = sum(valor for sabor, valor in self.frame_de_sabores.sabores.items() if self.frame_de_sabores.vars[sabor].get())
        total += sum(int(self.frame_de_adicionais.comboboxes[adicional].get()) * valor for adicional, valor in self.frame_de_adicionais.adicionais.items())
        self.total_label.configure(text=f'Total: R${total:.2f}')
    
    def adicionar_ao_carrinho(self):
        if not self.frame_de_tamanhos.confirmarEscolha():
            return
        
        if not self.frame_de_sabores.verificarSaboresMarcados():
            messagebox.showerror('ERRO', 'É obrigatório escolher pelo menos um sabor.')
            return
        
        tamanho = list(config["tamanhos"].keys())[self.frame_de_tamanhos.tamanho.get()]
        sabores = [sabor for sabor, var in self.frame_de_sabores.vars.items() if var.get()]
        adicionais = {adicional: int(self.frame_de_adicionais.comboboxes[adicional].get()) for adicional in config["adicionais"] if int(self.frame_de_adicionais.comboboxes[adicional].get()) > 0}
        total = float(self.total_label.cget("text").split('R$')[-1])
        
        pedido = f"{tamanho} - Sabores: {', '.join(sabores)} - Adicionais: {adicionais} - Total: R${total:.2f}"
        carrinho.adicionar_item(pedido)
        messagebox.showinfo("Sucesso", "Pedido adicionado ao carrinho!")
    
    def ver_carrinho(self):
        messagebox.showinfo("Carrinho", carrinho.exibir_itens())
    
    def limpar_carrinho(self):
        carrinho.limpar()
        messagebox.showinfo("Carrinho", "Carrinho esvaziado com sucesso!")
    
    def confirmar_compra(self):
        carrinho.confirmar_compra()

ctk.set_appearance_mode('dark')