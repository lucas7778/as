"""
Título do Projeto: Sistema inteligente para levantamento dos fatores de uso de
cargas elétricas nos FPSOs correlacionados às demandas de produção
Número de registro do Projeto: 5900.0117579.21.9

Back-end: X
Módulo: Machine Learning
Caso de uso:

Versão 0.0:
Data de início: 30/11/2021 12:08:56
Data de Entrega para Revisão: 15/12/2021
Data de Release: --/--/----

Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br

Versão 0.1:
Alterações gerais de métodos e padronização e formatação do código.
Caso de uso:
Data de Início: 15/12/2021
Data de Entrega para Revisão: 15/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Formatação geral dos nomes de atributos. Adicionadas docstrings faltantes.
Adicionada opção de devolver a predição em função da carga nominal (fator de
carga). Separação do ferramental gráfico (a solução utilizará o desenvolvido
pelo Front-end). Simplificação do método bbb_cstat: será chamado de forma
automática ao terminar o bm_fit() (em uma atualização futura bbb_cstat passará
a fazer parte da classe bdm_DtMn ao invés de bbb_BBox). Adicionado o método
bbb_stats, que retorna todas métricas calculadas. Adicionado o método bc_class.
Adicionado o método bdm_ftab. Alteração do método fit() de todos os modelos.
Adicionadas opções de hiperparâmetros.

Versão 0.2:
Alterações gerais de métodos e padronização e formatação do código.
Caso de uso:
Data de Início: 16/01/2022
Data de Entrega para Revisão: 18/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Padronização dos nomes de variáveis e argumentos dos métodos de bbb_BBox.
Ajustes nas docstrings refletindo as alterações. Adicionado o parâmetro
bbb_normt para ajuste de estratégia de normalização. Padronização parcial dos
nomes de variáveis e argumentos dos métodos de bdm_DtMn. Ajustes nas docstrings
refletindo as alterações. Padronização dos nomes de variáveis e argumentos dos
métodos em bml_model.py. Ajustes nas docstrings refletindo as alterações.
Padronização dos nomes de variáveis e argumentos em bdm_DtMn. Padronização dos
nomes de variáveis e argumentos em bc_Check. Ajustes nas docstrings refletindo
as alterações. Padronização de nomes de variável em bbb_BBox ("s" para
"bbb_str").

Versão 0.3:
Alterações gerais de métodos e padronização e formatação do código.
Caso de uso:
Data de Início: 24/01/2022
Data de Entrega para Revisão: 24/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Ajustes de cabeçalho: Ajustes de nome do responsável (alteração de Daniel 
Araujo para Vitor Hugo Ferreira), incluída. Data de Entrega para Revisão.

Versão 0.4:
Novos métodos adicionados e ajustes gerais de métodos e padronização do código.
Caso de uso:
Data de Início: 28/01/2022
Data de Entrega para Revisão: 28/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Ajustes na string retornada em bc_outn. Adicionado suporte a multi-output
para a Support Vector Machine (SVM). Adicionado suporte a multi-output para o
Gradient Boosting Regressor (GBR). Ajustes nas docstrings de bml_model.py
(erro de digitação). Adicionados métodos para salvar modelos. Adicionado método
para carregar modelos. Métodos de bc_Check convertidos para métodos estáticos.
Adicionado comentário explicando a não padronização dos imports de bml_dtmn.

Versão 0.5:
Adicão da classe bp_Perfm para medição de qualidade dos modelos.
Caso de uso:
Data de Início: 01/02/2022
Data de Entrega para Revisão: 01/02/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Adicionado controle de entrada para o método bbb_sstat. Adicionada a
funcionalidade de salvar as tabelas em formato excel. Adicionado o parâmetro
bbb_normt à classe bbb_BBox (guarda informações sobre normalização), junto com
getter apropriado. Removido o parâmetro bdm_normt da classe bdm_DtMn. Métodos
de bdm_DtMn convertidos para métodos estáticos. Classe bdm_DtMn separada nas
classes bp_Perfm e bdm_DtMn (para tomada de métricas do modelo e manipulações
gerais de dados). Cálculo do IQR movido parao método bp_apred. Instanciamento
da classe bdm_DtMn em bbb_BBox removido. Método bbb_cstat removido (a lógica
agora faz parte do processamento de bm_fit). Ajustes nas propriedades bbb_sdf e
bbb_smry. Ajustes nos métodos refletindo alterações. Valor padrão de bbb_form
alterado para False. (os dataframes de estatísticas serão retornados/salvos em
formato numérico por padrão).

Versão 0.6:
Hiperparâmetros adicionados. Classe que atua como gerenciador de modelos
adicionada.
Caso de uso:
Data de Início: 25/02/2022
Data de Entrega para Revisão: 02/03/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Adicionado o hiperparâmetro alpha para o modelo Ridge (em
bml_model.bm_RDG.fit). Adicionado o hiperparâmetro max_depth para o modelo GBR.
Adicionados hiperparâmetros para o modelo RFR (n_estimators, max_depth,
max_leaf_nodes, criterion). Adicionado controle de entrada para o
hiperparâmetro "criterion" no modelo RFR. Adicionado hiperparâmetros para o
modelo DTR (max_depth, max_leaf_nodes, criterion). Adicionado controle de
entrada para todos os modelos (somente uma variável de saída). Adicionado o
parâmetro bbb_param, que contém um dicionário com os hiperparâmetros definidos.
Formatação dos nomes dos hiperparâmetros para o modelo GBR segundo padronização.
Formatação dos nomes dos hiperparâmetros para o modelo RFR segundo padronização.
Formatação dos nomes dos hiperparâmetros para o modelo DTR segundo padronização.
Atualização na descrição da classe bdm_DtMn. Adicionado o módulo bml_mman e a
classe bmm_MM. Métodos para salvamento e carregamento de modelos movidos para a
classe bmm_MM. Adicionado o método bmm_MM.bmm_amdls, que retorna os nomes dos
modelos disponíveis. Adicionado o método bmm_MM.getm, que retorna um modelo
construido conforme requisitado. Adicionadas descrições em __init__.py
refletindo o novo módulo. Método bbb_save removido devido a problemas de
importação circular (e também redundância).

Versão 0.7:
Adicionada Grid Search. Classe que retorna valores default adicionada.
Modificações gerais na estrutura do pré-processamento. Ajustes de documentação
e correção de bugs. Desenvolvimentos gerais do pacote.
Caso de uso:
Data de Início: 02/03/2022
Data de Entrega para Revisão: 30/03/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste: Iahn Igel
Bloco geral de observações importantes:
    Adicionado controle de entrada para o argumento bbb_fator no método
bbb_pred. Adicionado suporte para condição do tipo "==" (igual) em bc_bound.
Adicionado atributo bbb_prepx, que guarda o objeto utilizado para
pré-processamento de inputs. Adicionados argumentos para pré-processamento no
método bbb_pdata. Adicionado código em bml_dtmn para ignorar aviso caso um
DataFrame tenha shape (n_samples, 1) ao inves de (n_samples,). Alterado o
formato padrão dos dados (treinamento, predição etc) de NumPy para DataFrame,
conforme padronização do projeto. Parâmetro bbb_normt removido. Passagem de
parâmetros bbb_onom, bbb_dsspl movida de __init__ para o método bbb_pdata.
Métodos bdm_nds, bdm_dnorm e bdm_norm removidos (deprecated).
Adicionado atributo bbb_prepy, que guarda o objeto utilizado para
pré/pós-processamento de outputs. Adicionados atributos bbb_pcolx e bbb_pcoly,
que guardam listas contendo os nomes das colunas para apresentação do
pré-processamento. Método bm_fit atualizado para o novo método de
pré-processamento. Adicionados métodos bbb_trnsx e bbb_trnsy que permitem
visualização dos dados após o pré-processamento. Atualização ao método bp_gets
e bp_apred refletindo alterações no sistema de pré-processamento. Atualização
ao método bdm_ids adicionando flexibilidade para permitir testes independentes
do módulo de KDD ou respeitar as divisões de escopo estabelecidas conforme
necessidade (será atualizado futuramente). Adicionado "else" statement caso
select_columns for igual a False em bdm_ids. Variáveis chn_variables (diversos)
e add_time (bdm_ids) removidas (não mais necessárias). Controle de entrada de
bbb_pred alterado refletindo alterações na estratégia de pré-processamento.
Método bdm_gettr adicionado, que gera o preprocessadores. Adicionadas
estratégias de préprocessamento de variáveis: conversão de intervalos,
normalização, binning, discretização kbins e binarização. Alterações nos
métodos envolvendo atividades de préprocessamento refletindo alterações no
fluxo de dados: leitura inicial do dataframe passado, preprocessamento,
predição/treinamento. Atualização no método de particionamento do DataFrame
para treinamento, validação e teste: métodos bdm_dfpar, bdm_dfsim, bdm_dfgrn,
bdm_gdiv adicionados, possibilitando a divisão das partições de forma granular
(cada partição cobrirá o mesmo horizonte de tempo que o DataFrame original).
Alteração no valor padrão de bbb_setup em bbb_pdata. Adicionado parâmetro
bbb_noneg no método bbb_pred, que controla a conversão de valores negativos das
previsões para 0. Correção de bug (tentativa de transformação inversa incorreta
e/ou conversão para fator de carga ao se passar processamento especial para
variável de saída). Adicionado argumento bbb_fread ao método bbb_pred, que
verifica se é necessário fazer o procedimento inicial de leitura (chamar o
método bdm_ids). Adicionado método bc_isfit em bc_Check para checar se o modelo
pode ser usado para atividades que requerem treinamento. Adicionado parâmetro
bbb_isfit que contém informações a respeito do status de treinamento do modelo.
Método bm_fitgs adicionado aos modelos (executa Grid Search). Método bbb_fit
adicionado a classe bbb_BBox. Métodos bm_fit e bm_fitgs ambos extendem o método
bbb_fit. Hiperparâmetro incorreto removido de bm_grid em bm_DTR.bm_fitgs.
Opções de pré-processamento de variáveis temporais adicionadas:
days_since_start e months_since_start. Argumento bbb_sscr adicionado ao método
bbb_BBox.bbb_fit, que controla a métrica utilizada na Grid Search. Parâmetro
bbb_gsr adicionado a classe bbb_BBox (DataFrame que contém os resultados da
GridSearch). Parâmetro bbb_isdp adicionado a classe bbb_BBox: informa se o
modelo está pronto para ser treinado. Funcionalidade para salvar resultados da
Grid Search adicionada ao Método bbb_sstat. Método bp_eval adicionado a
bp_Perfm. Método bmm_comp adicionado a bmm_MM. Método bmm_compt adicionado a
bmm_MM. Argumento bp_df adicionado ao método bp_apred. Cálculo do score de
validação passado para o método bp_apred. bbb_info passa a informar se foi
realizado um treinamento normal ou com Grid Search. Processamento de bm_grid
passado para o método bbb_fit. Classe bmm_Dflt adicionada (devolve valores
padrões para os métodos a serem utilizados pelo Front-End). Padronização de
variáveis em bbb_BBox. Ajustes nas docstrings de bml_model e bml_bbox.
Docstrings para os parâmetros de bbb_BBox adicionada. Método bbb_BBox.bbb_testm
adicionado, que retorna métricas sobre o dataset de teste. Ajustes gerais na
documentação do módulo.

Versão 0.8:
Controle de entrada base implementado. Ajustes gerais e padronização de
código e documentação.
Caso de uso:
Data de Início: 30/03/2022
Data de Entrega para Revisão: 02/05/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste: Iahn Igel
Bloco geral de observações importantes:
    Bug corrigido em bbb_fit (o for loop declarado na linha 728 agora acessa a
variável correta). Método argumento bmm_obj do método bmm_gdict convertido
para argumento opcional. Método bmm_getm alterado para opcionalmente já
preparar o modelo para treinamento. Variável bbb_log que contém o log interno
de utilização do modelo adicionada. Método bbb_addl, que adiciona informações
ao log, adicionado. Atualização parcial nos métodos do módulo bml_check de
forma a possibilitar o tratamento de exceções. Type hints parcialmente
adicionadas. Argumento **kwargs adicionado aos métodos de bml_bbox e bml_model
Valores default adicionados para argumentos bm_name/bbb_name e bm_inn/bbb_inn.
Método bc_ds adicionado a bc_Check, que checa a pertinencia do dataset passado
para o modelo. Progresso parcial no tratamento de erros. Adicionado argumento
bmm_name ao método bmm_auto. Padronização das keywords dos dicionários de
bm_grid (equivalente a padronização de bm_fit). Métodos bdm_mlsk e bdm_tdict
adicionados. Progresso parcial no tratamento de erros. Método bmm_fdflt movido
para bml_dtmn. Método bc_schek adicionado. Métodos bc_range, bc_svar, bc_pintn
adicionados. Método bc_array atualizado. Rotinas de controle de entrada de
hiperparâmetros atualizada. Error catching geral adicionado em bbb_fit,
bbb_pdata, bbb_trnsx, bbb_trnsy, bbb_pred, bbb_sstat. Progresso parcial no
tratamento de erros de bbb_setup. Variável bbb_compt, que segura os resultados
de bmm_auto, adicionada à classe BBox. Atualizações nos métodos bbb_stats e
bbb_sstat, refletindo adição de bbb_compt. Classe BBox atualizada para sempre
imprimir registros novos do log. Progresso parcial no controle de entrada
(rotinas para checagem do dataset e partições atualizadas). Variável bbb_isbc
adicionada a classe bbb_BBox, que reporta se o modelo foi instanciado
corretamente. Ajustes no controle de entrada no método __init__ de BBox.
Progresso parcial na adição de type hints. Adição do controle de entrada do
método bbb_pdata concluido. Documentação atualizada.
"""

"""
O pacote machine_learning conta com os seguintes módulos:

Módulos
----------

    bml_bbox: Define a superclasse bbb_BBox, classe base que define métodos e 
        atributos comuns a todos os modelos. 
        
    bml_check: Define a classe bc_Check, que objetiva oferecer utilitários que 
        auxiliam na detecção de erros de utilização dos métodos e funções do 
        pacote (para utilização interna).
        
    bml_dtmn: Define a classe bdm_DtMn, que objetiva oferecer utilitários que 
        auxiliam na manipulação dados (para utilização interna).
        
    bml_mman: Define a classe bmm_MM, que atua como gerenciador de modelos, e a
        classe bmm_Dflt, que objetiva retornar valores default.

    bml_log: Define a classe bl_Log, responsável pela criação e manutenção de 
        logs.
        
    bml_model: Define as classes referentes aos modelos oferecidos pelo pacote:
        bm_MLP: Multilayer Perceptron
        bm_MVR: Multivariate Regression
        bm_SVM: Support-Vector Machine
        bm_GBR: Gradient Boosting Regression
        bm_RFR: Random Forest Regression
        bm_RDG: Ridge Regression
        bm_DTR: Decision Tree Regression
        
    bml_perfm: Define a classe bp_Perfm, que objetiva oferecer utilitários que 
        auxiliam na tomada de métricas dos modelos (para utilização interna).

"""
