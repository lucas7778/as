# Diretório Ferramentas Computacionais

## Andre Abel Augusto

## Descrição

Esse diretório contém toda os dados coletados (artigos, apresentações, manuais etc.) referentes às ferramentas computacionais as serem utilizadas no projeto FPSO Power Demand Analytics. No subdiretório Documentação encontram-se os artigos, manuais e apresentações sobre as ferramentas. Na pasta Relatórios estão os relatórios gerados para cada ferramenta ou grupo de ferramentas.

## Instruções
Os relatórios devem ser sucintos e cobrir principalmente os seguintes aspectos: 

 - Licensa de Uso
 - Principais Funcionalidades
 - Histórico de Versão
 - Popularidade
 - Requisitos de Instalação e Uso
 - Entrada de Dados
 
As ferramentas pesquisadas, devidamente documentadas e com relatório pronto devem ser submetidas ao Prof. Abel e Vitor Hugo para validação. A atualização das pastas deverá ser assinalada na seção **Registros** desse documento.

## Registros

Definição da Estrutura das pastas
BACK_END
├── LICENSE.md
├── fpso_backend
│   ├── app.py
│   ├── common
│   │   └── __init__.py
│   ├── analytics
│   │   └── __init__.py
│   │   └── settings.py
│   ├── machine_learning
│   │   └── __init__.py
│   │   └── settings.py
│   ├── powerflow
│   │   └── __init__.py
│   │   └── settings.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── data_preparation.py
│   │   ├── data_splitter.py
│   │   └── settings.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── resources
│   └── testes
│       ├── __init__.py
├── README.md
└── .gitignore