function calculadoraRankeadas(vitorias, derrotas) {
  let saldo = vitorias - derrotas;
  let rank;

  if (saldo < 10) {
      rank = 'Ferro';
  } else if (saldo >= 11 && saldo <= 20) {
      rank = 'Bronze';
  } else if (saldo >= 21 && saldo <= 50) {
      rank = 'Prata';
  } else if (saldo >= 51 && saldo <= 80) {
      rank = 'Ouro';
  } else if (saldo >= 81 && saldo <= 90) {
      rank = 'Diamante';
  } else if (saldo >= 91 && saldo <= 100) {
      rank = 'Lendário';
  } else if (saldo >= 101) {
      rank = 'Imortal';
  }

  return rank;
}

let vitorias = 120;
let derrotas = 10;
let resultado = calculadoraRankeadas(vitorias, derrotas);
console.log(resultado);