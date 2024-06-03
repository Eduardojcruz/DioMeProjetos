class Heroi {
    constructor(nome, idade, tipo){
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }
    atacar() { 
        let ataque;
        if (this.tipo === "mago"){
            ataque = "magia";
        }else if(this.tipo === "guerreiro"){
            ataque = "espada";
        }else if(this.tipo === "monge"){
            ataque = "artes marciais";
        }else if(this.tipo === "ninja"){
            ataque = "shuriken";
        }
        console.log(`O ${this.tipo} atacou usando ${ataque}`);
    }
}

let personagem = new Heroi("Edu", 25, "ninja");
personagem.atacar();