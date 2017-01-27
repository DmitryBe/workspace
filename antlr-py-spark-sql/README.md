## generate spark sql gramma parser using antlr4 for python

create python virtualenv
`virtualenv -p /usr/local/bin/python3 env`

activate virtual env
`source ./env/bin/activate`

install dependency
`pip install -r requirements.txt`

download antlr4
`curl -s http://www.antlr.org/download/antlr-4.5.1-complete.jar -o bin/antlr-4.5.1-complete.jar`

create antlr4 alias
`alias antlr4='java -jar ./bin/antlr-4.5.1-complete.jar'`

generate parser
`antlr4 -Dlanguage=Python3 -visitor grammar/Sparksql.g4 -o apps/`



