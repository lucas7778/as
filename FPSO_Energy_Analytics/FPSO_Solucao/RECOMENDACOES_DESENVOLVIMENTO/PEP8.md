# PEP8 - Guia de estilo para código Python

## Documentando com as melhores práticas

### Angelo Cesar Colombini

[Python.org - PEP8](https://www.python.org/dev/peps/pep-0008/, "Pep8 - Oficial")

> __Motivação:__
> ___The Zen of Python, by Tim Peters___
>
> Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

### Algumas recomendações - há muito mais

1. No documento pep8.py há algumas instruções ou exemplos de como trabalhar com a PEP8 em seu código

2. Além disso, no documetno documentando com docstrings.py há recomendações mais específicas para trabalhos com funções

3. Incie sempre seu código com um cabeçalho contendo minimanete os seguintes tópicos:

    3.1. Título do projeto

    3.2. Nome(s), núcleo, contato e data

    3.3. Título do módulo

    3.4. Relação do módulo com outras partes do sistema

        3.4.1 Relacione todas as dependencias do módulo
        3.4.2 ....

    3.5. Breve descritivo do módulo

    3.6. Bibliotecas e suas versões

    3.7. Data de conclusão do módulo

4. Relatório:

> Conjuntamente com o programa devidamente documentado, deverá ser entregue um relatório. Pretende-se com a cobrança dos relatórios criar o hâbito de documentar, ainda que de forma mínima, os programas produzidos. Profissionalmente, dificilmente se desenvolverá um software para ser utilizado apenas por você. Para que terceiros possam usar um dado software de forma efetiva, ele deve vir acompanhado de uma documentação técnica adequada.
>
>A documentação também é importante para o negócio. Depois de um certo tempo equipes serão reestruturadas e corremos o risco de perder o histórico do software, não nos lembrando mais de decisões de projeto tomadas quando da confecção de um determinado software. Uma documentação de um software deve registrar estas decisões para facilitar a manutenção deste software. A documentação, portanto, é tão importante quanto o código. Por esta razão, documente bem o que você produz.
>

__Recomendações mínimas para um relatório:__

Informações de caráter administrativo:

a. Nome(s) autor(es):

b. Projeto:

c. Módulo:

d. Data de entrega:

> Descrição informal e sucinta do que o programa faz. Esta descrição deverá ser feita, de maneira global, a respeito do programa como um todo sem transcrever literalmente, comando por comando.
>
> Explicações sobre como operar o programa, ressaltando quais são as entradas, como serão solicitadas e quais são as saídas esperadas.
>
> Breve descrição dos algoritmos/técnicas/ferramentas/etc utilizados na resolução do problema proposto. Aqui cabe novamente a observação acima (seja sucinto e objetivo). Abstraia de detalhes de implementação. Produza descrições mais conceituais.
>
> As condições de contorno, ou seja, qual é o conjunto de dados de entrada válido para o correto funcionamento do programa. Em que situação o seu programa não funcionará adequadamente?
>
> Relação dos recursos de ambiente necessários para sua perfeita execução.
>
