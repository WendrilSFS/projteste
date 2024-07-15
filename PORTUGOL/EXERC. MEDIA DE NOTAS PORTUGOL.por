programa {
  funcao inicio() {
    
    real n1,n2,media
    escreva("bom dia!")
    escreva("\n digite a primeira nota: ")
    leia(n1)
    escreva("digite a segunda nota: ")
    leia(n2)
    media = (n1+n2) / 2
    se(media >= 7){
      escreva("\n a primeira nota do estudante é: ",n1)
      escreva("\n a segunda nota do estudante é: ",n2)
      escreva("\n a media do estudante é: ",media)
      escreva("\n parabens aluno esta aprovado")
    }
    senao{
      escreva("\n aluno reprovado")
    }
    escreva("\n fim do programa!!")
  }
}
