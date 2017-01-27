# Generated from grammar/Sparksql.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SparksqlParser import SparksqlParser
else:
    from SparksqlParser import SparksqlParser

# This class defines a complete listener for a parse tree produced by SparksqlParser.
class SparksqlListener(ParseTreeListener):

    # Enter a parse tree produced by SparksqlParser#root.
    def enterRoot(self, ctx:SparksqlParser.RootContext):
        pass

    # Exit a parse tree produced by SparksqlParser#root.
    def exitRoot(self, ctx:SparksqlParser.RootContext):
        pass


    # Enter a parse tree produced by SparksqlParser#select_statement.
    def enterSelect_statement(self, ctx:SparksqlParser.Select_statementContext):
        pass

    # Exit a parse tree produced by SparksqlParser#select_statement.
    def exitSelect_statement(self, ctx:SparksqlParser.Select_statementContext):
        pass


    # Enter a parse tree produced by SparksqlParser#limit_clause.
    def enterLimit_clause(self, ctx:SparksqlParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by SparksqlParser#limit_clause.
    def exitLimit_clause(self, ctx:SparksqlParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by SparksqlParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:SparksqlParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by SparksqlParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:SparksqlParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by SparksqlParser#order_by_expression.
    def enterOrder_by_expression(self, ctx:SparksqlParser.Order_by_expressionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#order_by_expression.
    def exitOrder_by_expression(self, ctx:SparksqlParser.Order_by_expressionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#query_expression.
    def enterQuery_expression(self, ctx:SparksqlParser.Query_expressionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#query_expression.
    def exitQuery_expression(self, ctx:SparksqlParser.Query_expressionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#with_expression.
    def enterWith_expression(self, ctx:SparksqlParser.With_expressionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#with_expression.
    def exitWith_expression(self, ctx:SparksqlParser.With_expressionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:SparksqlParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:SparksqlParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#column_name_list.
    def enterColumn_name_list(self, ctx:SparksqlParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by SparksqlParser#column_name_list.
    def exitColumn_name_list(self, ctx:SparksqlParser.Column_name_listContext):
        pass


    # Enter a parse tree produced by SparksqlParser#query_specification.
    def enterQuery_specification(self, ctx:SparksqlParser.Query_specificationContext):
        pass

    # Exit a parse tree produced by SparksqlParser#query_specification.
    def exitQuery_specification(self, ctx:SparksqlParser.Query_specificationContext):
        pass


    # Enter a parse tree produced by SparksqlParser#union.
    def enterUnion(self, ctx:SparksqlParser.UnionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#union.
    def exitUnion(self, ctx:SparksqlParser.UnionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_source.
    def enterTable_source(self, ctx:SparksqlParser.Table_sourceContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_source.
    def exitTable_source(self, ctx:SparksqlParser.Table_sourceContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_source_item_joined.
    def enterTable_source_item_joined(self, ctx:SparksqlParser.Table_source_item_joinedContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_source_item_joined.
    def exitTable_source_item_joined(self, ctx:SparksqlParser.Table_source_item_joinedContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_source_item.
    def enterTable_source_item(self, ctx:SparksqlParser.Table_source_itemContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_source_item.
    def exitTable_source_item(self, ctx:SparksqlParser.Table_source_itemContext):
        pass


    # Enter a parse tree produced by SparksqlParser#group_by_item.
    def enterGroup_by_item(self, ctx:SparksqlParser.Group_by_itemContext):
        pass

    # Exit a parse tree produced by SparksqlParser#group_by_item.
    def exitGroup_by_item(self, ctx:SparksqlParser.Group_by_itemContext):
        pass


    # Enter a parse tree produced by SparksqlParser#derived_table.
    def enterDerived_table(self, ctx:SparksqlParser.Derived_tableContext):
        pass

    # Exit a parse tree produced by SparksqlParser#derived_table.
    def exitDerived_table(self, ctx:SparksqlParser.Derived_tableContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_value_constructor.
    def enterTable_value_constructor(self, ctx:SparksqlParser.Table_value_constructorContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_value_constructor.
    def exitTable_value_constructor(self, ctx:SparksqlParser.Table_value_constructorContext):
        pass


    # Enter a parse tree produced by SparksqlParser#expression_list.
    def enterExpression_list(self, ctx:SparksqlParser.Expression_listContext):
        pass

    # Exit a parse tree produced by SparksqlParser#expression_list.
    def exitExpression_list(self, ctx:SparksqlParser.Expression_listContext):
        pass


    # Enter a parse tree produced by SparksqlParser#subquery.
    def enterSubquery(self, ctx:SparksqlParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SparksqlParser#subquery.
    def exitSubquery(self, ctx:SparksqlParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SparksqlParser#join_part.
    def enterJoin_part(self, ctx:SparksqlParser.Join_partContext):
        pass

    # Exit a parse tree produced by SparksqlParser#join_part.
    def exitJoin_part(self, ctx:SparksqlParser.Join_partContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_name_with_hint.
    def enterTable_name_with_hint(self, ctx:SparksqlParser.Table_name_with_hintContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_name_with_hint.
    def exitTable_name_with_hint(self, ctx:SparksqlParser.Table_name_with_hintContext):
        pass


    # Enter a parse tree produced by SparksqlParser#as_table_alias.
    def enterAs_table_alias(self, ctx:SparksqlParser.As_table_aliasContext):
        pass

    # Exit a parse tree produced by SparksqlParser#as_table_alias.
    def exitAs_table_alias(self, ctx:SparksqlParser.As_table_aliasContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_alias.
    def enterTable_alias(self, ctx:SparksqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_alias.
    def exitTable_alias(self, ctx:SparksqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by SparksqlParser#with_table_hints.
    def enterWith_table_hints(self, ctx:SparksqlParser.With_table_hintsContext):
        pass

    # Exit a parse tree produced by SparksqlParser#with_table_hints.
    def exitWith_table_hints(self, ctx:SparksqlParser.With_table_hintsContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_hint.
    def enterTable_hint(self, ctx:SparksqlParser.Table_hintContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_hint.
    def exitTable_hint(self, ctx:SparksqlParser.Table_hintContext):
        pass


    # Enter a parse tree produced by SparksqlParser#index_value.
    def enterIndex_value(self, ctx:SparksqlParser.Index_valueContext):
        pass

    # Exit a parse tree produced by SparksqlParser#index_value.
    def exitIndex_value(self, ctx:SparksqlParser.Index_valueContext):
        pass


    # Enter a parse tree produced by SparksqlParser#column_alias_list.
    def enterColumn_alias_list(self, ctx:SparksqlParser.Column_alias_listContext):
        pass

    # Exit a parse tree produced by SparksqlParser#column_alias_list.
    def exitColumn_alias_list(self, ctx:SparksqlParser.Column_alias_listContext):
        pass


    # Enter a parse tree produced by SparksqlParser#column_alias.
    def enterColumn_alias(self, ctx:SparksqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by SparksqlParser#column_alias.
    def exitColumn_alias(self, ctx:SparksqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by SparksqlParser#expression.
    def enterExpression(self, ctx:SparksqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#expression.
    def exitExpression(self, ctx:SparksqlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#aggregate_windowed_function.
    def enterAggregate_windowed_function(self, ctx:SparksqlParser.Aggregate_windowed_functionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#aggregate_windowed_function.
    def exitAggregate_windowed_function(self, ctx:SparksqlParser.Aggregate_windowed_functionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#all_distinct_expression.
    def enterAll_distinct_expression(self, ctx:SparksqlParser.All_distinct_expressionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#all_distinct_expression.
    def exitAll_distinct_expression(self, ctx:SparksqlParser.All_distinct_expressionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#constant.
    def enterConstant(self, ctx:SparksqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by SparksqlParser#constant.
    def exitConstant(self, ctx:SparksqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by SparksqlParser#sign.
    def enterSign(self, ctx:SparksqlParser.SignContext):
        pass

    # Exit a parse tree produced by SparksqlParser#sign.
    def exitSign(self, ctx:SparksqlParser.SignContext):
        pass


    # Enter a parse tree produced by SparksqlParser#number.
    def enterNumber(self, ctx:SparksqlParser.NumberContext):
        pass

    # Exit a parse tree produced by SparksqlParser#number.
    def exitNumber(self, ctx:SparksqlParser.NumberContext):
        pass


    # Enter a parse tree produced by SparksqlParser#select_list.
    def enterSelect_list(self, ctx:SparksqlParser.Select_listContext):
        pass

    # Exit a parse tree produced by SparksqlParser#select_list.
    def exitSelect_list(self, ctx:SparksqlParser.Select_listContext):
        pass


    # Enter a parse tree produced by SparksqlParser#select_list_elem.
    def enterSelect_list_elem(self, ctx:SparksqlParser.Select_list_elemContext):
        pass

    # Exit a parse tree produced by SparksqlParser#select_list_elem.
    def exitSelect_list_elem(self, ctx:SparksqlParser.Select_list_elemContext):
        pass


    # Enter a parse tree produced by SparksqlParser#full_column_name.
    def enterFull_column_name(self, ctx:SparksqlParser.Full_column_nameContext):
        pass

    # Exit a parse tree produced by SparksqlParser#full_column_name.
    def exitFull_column_name(self, ctx:SparksqlParser.Full_column_nameContext):
        pass


    # Enter a parse tree produced by SparksqlParser#column_name.
    def enterColumn_name(self, ctx:SparksqlParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SparksqlParser#column_name.
    def exitColumn_name(self, ctx:SparksqlParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SparksqlParser#case_expr.
    def enterCase_expr(self, ctx:SparksqlParser.Case_exprContext):
        pass

    # Exit a parse tree produced by SparksqlParser#case_expr.
    def exitCase_expr(self, ctx:SparksqlParser.Case_exprContext):
        pass


    # Enter a parse tree produced by SparksqlParser#table_name.
    def enterTable_name(self, ctx:SparksqlParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SparksqlParser#table_name.
    def exitTable_name(self, ctx:SparksqlParser.Table_nameContext):
        pass


    # Enter a parse tree produced by SparksqlParser#search_condition.
    def enterSearch_condition(self, ctx:SparksqlParser.Search_conditionContext):
        pass

    # Exit a parse tree produced by SparksqlParser#search_condition.
    def exitSearch_condition(self, ctx:SparksqlParser.Search_conditionContext):
        pass


    # Enter a parse tree produced by SparksqlParser#search_condition_or.
    def enterSearch_condition_or(self, ctx:SparksqlParser.Search_condition_orContext):
        pass

    # Exit a parse tree produced by SparksqlParser#search_condition_or.
    def exitSearch_condition_or(self, ctx:SparksqlParser.Search_condition_orContext):
        pass


    # Enter a parse tree produced by SparksqlParser#search_condition_not.
    def enterSearch_condition_not(self, ctx:SparksqlParser.Search_condition_notContext):
        pass

    # Exit a parse tree produced by SparksqlParser#search_condition_not.
    def exitSearch_condition_not(self, ctx:SparksqlParser.Search_condition_notContext):
        pass


    # Enter a parse tree produced by SparksqlParser#predicate.
    def enterPredicate(self, ctx:SparksqlParser.PredicateContext):
        pass

    # Exit a parse tree produced by SparksqlParser#predicate.
    def exitPredicate(self, ctx:SparksqlParser.PredicateContext):
        pass


    # Enter a parse tree produced by SparksqlParser#id_1.
    def enterId_1(self, ctx:SparksqlParser.Id_1Context):
        pass

    # Exit a parse tree produced by SparksqlParser#id_1.
    def exitId_1(self, ctx:SparksqlParser.Id_1Context):
        pass


    # Enter a parse tree produced by SparksqlParser#comparison_operator.
    def enterComparison_operator(self, ctx:SparksqlParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by SparksqlParser#comparison_operator.
    def exitComparison_operator(self, ctx:SparksqlParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by SparksqlParser#simple_id.
    def enterSimple_id(self, ctx:SparksqlParser.Simple_idContext):
        pass

    # Exit a parse tree produced by SparksqlParser#simple_id.
    def exitSimple_id(self, ctx:SparksqlParser.Simple_idContext):
        pass


    # Enter a parse tree produced by SparksqlParser#null_notnull.
    def enterNull_notnull(self, ctx:SparksqlParser.Null_notnullContext):
        pass

    # Exit a parse tree produced by SparksqlParser#null_notnull.
    def exitNull_notnull(self, ctx:SparksqlParser.Null_notnullContext):
        pass


