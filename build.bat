del .\FPSO_Energy_Analytics\FPSO_Solucao\Front_end\FPSO_Interface\fpso_interface.spec
del .\FPSO_Energy_Analytics\FPSO_Solucao\Front_end\FPSO_Interface\fpso_interface.zip
rmdir /s /q .\FPSO_Energy_Analytics\FPSO_Solucao\Front_end\FPSO_Interface\__pycache__
rmdir /s /q .\FPSO_Energy_Analytics\FPSO_Solucao\Front_end\FPSO_Interface\build
rmdir /s /q .\FPSO_Energy_Analytics\FPSO_Solucao\Front_end\FPSO_Interface\dist
pip install pipenv
rem pipenv --python 3.7
rem pipenv --rm
pipenv install
pipenv shell < build_env.bat
