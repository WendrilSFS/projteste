programa {
  funcao inicio() {
    
    real saldo,saque,res
    escreva("\n bem vindo ao banco! ")
    escreva("\n vamos confirmar seu saldo")
    escreva("\n digite o valor do saldo da sua conta: ")
    leia (saldo)
    escreva("\n digite o valor q voce quer sacar: ")
    leia(saque)
    res = saldo - saque
    escreva("\n seu saldo final é: ",res)

  
  }
}
