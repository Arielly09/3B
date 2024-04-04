function nomeIdade(nome, idade){
    return 'meu nome é ${nome} e minha idade é ${idade}';
}
nomeIdade("José",18);

console.log(nomeIdade(17,"Kevely"))
console.log(nomeIdade)("Kevely",17)

function soma(numero1, numero2){
    return numero1+numero2;
}

function mutiplica(numero1=1, numero2=1){
    return numero1*numero2;
}
console.log(soma(2))
console.log(mutiplica(soma(4,5)))