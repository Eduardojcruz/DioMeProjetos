let nomeHeroi = "Dood"
let rank = ""
let xpHeroi = 10001

if (xpHeroi <= 1000){
    rank = "Ferro"
}
else if(xpHeroi <= 2000){
    rank = "Bronze"
}
else if(xpHeroi <= 5000){
    rank = "Prata"
}
else if(xpHeroi <= 7000){
    rank = "Ouro"
}
else if(xpHeroi <= 8000){
    rank = "Platina"
}
else if(xpHeroi <= 9000){
    rank = "Ascendente"
}
else if(xpHeroi <= 10000){
    rank = "Imortal"
}
else if(xpHeroi > 10000){
    rank = "Radiante"
}else{
    rank = "Não foi possivel calcular."
}

console.log("O herói de nome " +  nomeHeroi + " está no nível de: " + rank)