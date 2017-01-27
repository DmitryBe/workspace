import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from apps.grammar import *


class CustomVisitor1(SparksqlVisitor):

    def __init__(self):
        super(CustomVisitor1, self).__init__()

    def visitSelect_statement(self, ctx:SparksqlParser.Select_statementContext):
        print('select begin')
        return self.visitChildren(ctx)


class CustomErrorListener(ErrorListener):

    def __init__(self):
        super(CustomErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception('Error: %s; Line: %s, Col: %s' % (msg, line, column))


class Parser1(object):

    def __init__(self):

        self.is_valid = False
        self.error = None
        self.tree = None
        self.tree_str = None

    def parse(self, sql):

        in_stream = InputStream(sql)
        lexer = SparksqlLexer(in_stream)
        token_stream = CommonTokenStream(lexer)

        try:

            parser = SparksqlParser(token_stream)
            parser._listeners = [CustomErrorListener()]
            self.tree = parser.select_statement()
            self.tree_str = Trees.toStringTree(self.tree, None, parser)
            self.is_valid = True

        except Exception as ex:
            self.is_valid = False
            self.error = ex

def main():

    sql = sys.argv[1]
    print(sql)
    p = Parser1()
    p.parse(sql)
    print(p.is_valid)


if __name__ == '__main__':
    main()
