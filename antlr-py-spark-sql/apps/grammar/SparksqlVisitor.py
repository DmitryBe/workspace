# Generated from grammar/Sparksql.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SparksqlParser import SparksqlParser
else:
    from SparksqlParser import SparksqlParser

# This class defines a complete generic visitor for a parse tree produced by SparksqlParser.

class SparksqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SparksqlParser#root.
    def visitRoot(self, ctx:SparksqlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#select_statement.
    def visitSelect_statement(self, ctx:SparksqlParser.Select_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#limit_clause.
    def visitLimit_clause(self, ctx:SparksqlParser.Limit_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#order_by_clause.
    def visitOrder_by_clause(self, ctx:SparksqlParser.Order_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#order_by_expression.
    def visitOrder_by_expression(self, ctx:SparksqlParser.Order_by_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#query_expression.
    def visitQuery_expression(self, ctx:SparksqlParser.Query_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#with_expression.
    def visitWith_expression(self, ctx:SparksqlParser.With_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#common_table_expression.
    def visitCommon_table_expression(self, ctx:SparksqlParser.Common_table_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#column_name_list.
    def visitColumn_name_list(self, ctx:SparksqlParser.Column_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#query_specification.
    def visitQuery_specification(self, ctx:SparksqlParser.Query_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#union.
    def visitUnion(self, ctx:SparksqlParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_source.
    def visitTable_source(self, ctx:SparksqlParser.Table_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_source_item_joined.
    def visitTable_source_item_joined(self, ctx:SparksqlParser.Table_source_item_joinedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_source_item.
    def visitTable_source_item(self, ctx:SparksqlParser.Table_source_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#group_by_item.
    def visitGroup_by_item(self, ctx:SparksqlParser.Group_by_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#derived_table.
    def visitDerived_table(self, ctx:SparksqlParser.Derived_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_value_constructor.
    def visitTable_value_constructor(self, ctx:SparksqlParser.Table_value_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#expression_list.
    def visitExpression_list(self, ctx:SparksqlParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#subquery.
    def visitSubquery(self, ctx:SparksqlParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#join_part.
    def visitJoin_part(self, ctx:SparksqlParser.Join_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_name_with_hint.
    def visitTable_name_with_hint(self, ctx:SparksqlParser.Table_name_with_hintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#as_table_alias.
    def visitAs_table_alias(self, ctx:SparksqlParser.As_table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_alias.
    def visitTable_alias(self, ctx:SparksqlParser.Table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#with_table_hints.
    def visitWith_table_hints(self, ctx:SparksqlParser.With_table_hintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_hint.
    def visitTable_hint(self, ctx:SparksqlParser.Table_hintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#index_value.
    def visitIndex_value(self, ctx:SparksqlParser.Index_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#column_alias_list.
    def visitColumn_alias_list(self, ctx:SparksqlParser.Column_alias_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#column_alias.
    def visitColumn_alias(self, ctx:SparksqlParser.Column_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#expression.
    def visitExpression(self, ctx:SparksqlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#aggregate_windowed_function.
    def visitAggregate_windowed_function(self, ctx:SparksqlParser.Aggregate_windowed_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#all_distinct_expression.
    def visitAll_distinct_expression(self, ctx:SparksqlParser.All_distinct_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#constant.
    def visitConstant(self, ctx:SparksqlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#sign.
    def visitSign(self, ctx:SparksqlParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#number.
    def visitNumber(self, ctx:SparksqlParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#select_list.
    def visitSelect_list(self, ctx:SparksqlParser.Select_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#select_list_elem.
    def visitSelect_list_elem(self, ctx:SparksqlParser.Select_list_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#full_column_name.
    def visitFull_column_name(self, ctx:SparksqlParser.Full_column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#column_name.
    def visitColumn_name(self, ctx:SparksqlParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#case_expr.
    def visitCase_expr(self, ctx:SparksqlParser.Case_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#table_name.
    def visitTable_name(self, ctx:SparksqlParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#search_condition.
    def visitSearch_condition(self, ctx:SparksqlParser.Search_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#search_condition_or.
    def visitSearch_condition_or(self, ctx:SparksqlParser.Search_condition_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#search_condition_not.
    def visitSearch_condition_not(self, ctx:SparksqlParser.Search_condition_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#predicate.
    def visitPredicate(self, ctx:SparksqlParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#id_1.
    def visitId_1(self, ctx:SparksqlParser.Id_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#comparison_operator.
    def visitComparison_operator(self, ctx:SparksqlParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#simple_id.
    def visitSimple_id(self, ctx:SparksqlParser.Simple_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SparksqlParser#null_notnull.
    def visitNull_notnull(self, ctx:SparksqlParser.Null_notnullContext):
        return self.visitChildren(ctx)



del SparksqlParser