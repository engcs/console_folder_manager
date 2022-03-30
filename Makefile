## @ registrar menu de contexto
.PHONY: registrar-menu
registrar-menu:
	python ./scripts/customize-contextmenu-win10.py

## @ testes e cobertura
.PHONY: cobertura-menu
cobertura:
	coverage run --source app -m unittest tests.test_utils.TestInputStr  tests.test_utils.TestInputInt tests -v
	coverage html