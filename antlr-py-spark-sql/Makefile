
virtenv:
	virtualenv -p /usr/local/bin/python3 env

activate:
	source ./env/bin/activate

deactivate:
	deactivate

dependency:
	pip install -r requirements.txt

prep:
	curl -s http://www.antlr.org/download/antlr-4.5.1-complete.jar -o bin/antlr-4.5.1-complete.jar
	alias antlr4='java -jar ./bin/antlr-4.5.1-complete.jar'

gen-grammar:
	antlr4 -Dlanguage=Python3 -visitor grammar/Sparksql.g4 -o apps/

unalias:
	unalias antlr4
