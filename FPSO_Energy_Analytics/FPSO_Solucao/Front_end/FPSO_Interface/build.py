import os
import sys
import subprocess

# Instala os pacotes Python necessários
os.system('python --version')
os.system('pip uninstall -y typing')    # remover porque vai apagar o env anterior
os.system('pip install dash')   # colocar todos os installs na mesma linha
os.system('pip install dash_daq')
os.system('pip install dash')
os.system('pip install numpy')
os.system('pip install pandas')  # o pandas mais novo que tem no Jenkins é 1.1.5
os.system('pip install PyQt5')
os.system('pip install pytz')
os.system('pip install scipy')
os.system('pip install setuptools')
os.system('pip install statsmodels')
os.system('pip install openpyxl')
os.system('pip install sklearn')
os.system('pip install pandapower')

# Pega o caminho de instalação dos pacotes para acrescentar o Dash manualmente ao pyinstaller
os.chdir(sys.argv[1])
sproc = subprocess.Popen("pip show dash", shell=True, stdout=subprocess.PIPE)
piptok = sproc.stdout.read().split()
locpos = piptok.index(b'Location:')
pypkgpath = piptok[locpos + 1].decode('utf-8')

# Gera o executável e os arquivos auxiliares
os.system('pyinstaller --add-data "assets\\dashstyle.css;assets" ' +
                      '--add-binary "assets\\petro2.png;assets" ' +
                      '--add-binary "assets\\add.png;assets" ' +
                      '--add-binary "assets\\minus.png;assets" ' +
                      '--add-binary "imgs\\db_icon.png;imgs" ' +
                      '--add-binary "imgs\\ml_icon.png;imgs" ' +
                      '--add-binary "imgs\\imgs.qrc;imgs" ' +
                      '--add-binary "P67_TAGS_SISTEMAS.xlsx;." ' +
                      '--add-data "2022-03-23_Variáveis_Sistemas_P67.csv;." ' +
                      '--add-data "' + pypkgpath + '\\dash\\dcc;dash\\dcc" ' +
                      '--add-data "' + pypkgpath + '\\dash\\html;dash\\html" ' +
                      '--add-data "' + pypkgpath + '\\dash\\dash_table;dash\\dash_table" ' +
                      '--add-data "' + pypkgpath + '\\dash_daq;dash_daq" ' +
                      '--add-data "fpso_interface5.ui;." ' +
                      '--add-data "eqp2.ui;." ' +
                      '--add-data "fcfi2.ui;." ' +
                      '--add-data "fpso_fp_eq_interface.ui;." ' +
                      '--add-data "cria_rede.ui;." ' +
                      '--add-data "subsis.ui;." ' +
                      '--add-data "subsistema_interface2.ui;." ' +
                      '--add-binary "eqs.pickle;." ' +
                      '--add-binary "example.pickle;." ' +
                      '--hidden-import "multiSelCombo2" ' +
                      '--hidden-import="sklearn.utils._typedefs" ' +
                      '--hidden-import="sklearn.utils._heap" ' +
                      '--hidden-import="sklearn.utils.murmurhash" ' +
                      '--hidden-import="sklearn.utils._cython_blas" ' +
                      '--hidden-import="sklearn.utils._fast_dict" ' +
                      '--hidden-import="sklearn.utils._openmp_helpers" ' +
                      '--hidden-import="sklearn.utils._random" ' +
                      '--hidden-import="sklearn.utils._seq_dataset" ' +
                      '--hidden-import="sklearn.utils._sorting" ' +
                      '--hidden-import="sklearn.utils._vector_sentinel" ' +
                      '--hidden-import="sklearn.utils._weight_vector" ' +
                      '--hidden-import="sklearn.neighbors._partition_nodes" ' +
                      '--hidden-import="sklearn.neighbors._quad_tree" ' +
                      '--hidden-import="sklearn.__check_build._check_build" ' +
                      '--add-data "' + pypkgpath + '\\dash\\deps;dash\\deps" ' +
                      '--add-data "' + pypkgpath + '\\dash\\dash-renderer;dash\\dash-renderer" ' +
                      'fpso_interface.py')
