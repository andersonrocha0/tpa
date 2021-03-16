# Entendendo Threads, Processos e AsyncIO com Python 3.8


Vamos usar o seguinte exemplo:

Imagine que você vai fazer um jantar para 10 amigos.

Os passos para fazer o prato proposto para a janta são os seguintes:

* Lavar os vegetais;
* Cortar os vegetais;
* Cozinhar;
* Servir;


Para cada passo acima, você leva os seguintes tempos:

* 5 minutos;
* 13 minutos;
* 30 minutos;
* 2 minutos;

A soma dos passos é: 50 minutos. Logo, para 10 amigos, você demoraria 500 minutos, um pouco
mais de 8 horas.


**Acredito que esse tempo possa ser reduzido!**


### Paralelismo

Imagine que você quer reduzir o tempo de cozimento para 250 minutos.

Se algum amigo te ajudar a cozinhar, logo, vocês executarão o serviço
em paralelo e irão reduzir o tempo para 250 minutos.

O que acontece nesse caso, é que cada pessoa está "cozinhando na sua própria cozinha"
ou seja, elas não estão disputando recursos em comum.

Ou seja, paralelismo acontece quando o computador tem vários cores. E existem processos
rodando em ao menos dois deles.

O paralelismo, acontece através da execução de diferentes processos.

### Concurrency / Concorrência / Simultaneidade

Podemos ver que o nosso maior gargalo acontece quando vamos cozinhar (levar os legumes)
para o forno.

Uma pergunta que podemos fazer é a seguinte: quantos pratos posso cozinhar por vez no forno?
Se pudessemos cozinhar os 10 pratos de uma só vez, economizaríamos 270 minutos.

Nesse caso, não utilizaríamos recurso algum de outra cozinha, simplesmente aproveitaríamos
da capacidade de um recurso ocioso.

A concorrência acontece dentro do mesmo processo, aproveitando ociosidade de um
recurso.

Poderíamos aplicar facilmente concorrência às outras etapas também.

Concorrência acontece dentro de uma thread que está sendo executada dentro de um processo.
Um processo pode ter várias threads. As threads podem compartilhar recursos entre elas, por exemplo
o forno.


### Quando usar um ou outro?

Falando por cima, se sua aplicação Python está executando operações vinculadas
à CPU, como processamento de números ou manipulação de texto, opte pelo paralelismo. 
A simultaneidade não trará muitos benefícios nesses cenários. 


| Técnica      | Problema  |
|--------------|-----------|
| Paralelismo  | CPU Bound |
| Concorrência | IO Bound  |


# Referências
* https://medium.com/fintechexplained/advanced-python-concurrency-and-parallelism-82e378f26ced
* https://danielflannery.ie/simulate-cpu-load-with-python/
* https://api.openbrewerydb.org/
* https://github.com/public-apis/public-apis

---

# Análises

CPU


[Single] Time taken : 56.68953728675842

[Threads] Time taken : 53.31462550163269

[Asyncio] Time taken : 55.30215883255005

[Multiprocessing] Time taken : 18.123328924179077


---

IO

[Single] Time taken : 12.819547176361084

[Multiprocessing] Time taken : 2.8636417388916016

[Threads] Time taken : 2.1719021797180176

[Async Manual] Time taken : 4.027798175811768

[Async] Time taken : 2.0230748653411865
   