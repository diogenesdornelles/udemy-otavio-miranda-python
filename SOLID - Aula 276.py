# Single responsability principle
"""Uma classe deve ter apenas um motivo para mudar. Evitar conjunções aditivas.
Assim a classe não deve ser responsável por mais de uma função. Ex.: retirar, tratar e inserir dados em DB"""

# Open closed principle
"""Classes devem ser abertos para extensão e não para modificações. Lembrar exemplo Cliente CPF e CNPJ
Incluir pessoa jurídica"""

# Liskov substitution principle
"""Classes derivadas devem substituir totalmente classes-bases. Ex.: Animal e Cachorro."""

# Interface segregation principle
"""Os clientes não devem ser forçados a depender de interfaces que não utilizam.
Ex.: Classe Abstrata Cliente com métodos get_cpf e get_cnpj e classes filhas ClientePF e ClientePJ.
"""

# Dependency inversion principle

""" Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações, 
não o inverso. 
Forma errada: Meu e-commerce tem classe "ECommerce" e tem classe "PagarMercadoPago", API que é chamada por
método "pagar_compras" da primeira. Uma classe depende exclusivamente de serviços de outra classe.
Forma correta: Criar uma classe abstrata (GerenciadorPagamentos), uma interface que vai gerenciar as diversas formas de 
pagamento (paypal, pagseguro, mercado pago, etc), a qual contém o método "realizar_pagamento".
classe "ECommerce" vai depender dessa abstração.
"""
