--3) Escreva um bloco anonimo para calcular a eficiência de um sistema de energia,
--onde a eficiência é definida como a razão entre a energia útil gerada e a energia total consumida.
--Trate exceções. Lance uma exceção personalizada quando a energia consumida for negativa.

SET SERVEROUTPUT ON
ACCEPT v_energia_gerada PROMPT 'Entre com a energia gerada:';
ACCEPT v_energia_consumida PROMPT 'Entre com a energia consumida:';
DECLARE
    v_energia_gerada NUMBER; -- := &v_energia_gerada;
    v_energia_consumida NUMBER; -- := &v_energia_consumida;
    v_eficiencia NUMBER;
BEGIN
    v_energia_gerada := &v_energia_gerada;
    v_energia_consumida := &v_energia_consumida;

    IF v_energia_gerada < 0 OR v_energia_consumida < 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Valores negativos nao sao aceitos');
    END IF;
    v_eficiencia := v_energia_gerada/v_energia_consumida;
    DBMS_OUTPUT.PUT_LINE('A eficiencia do sistema de energia e: '||v_eficiencia);
EXCEPTION
    WHEN ZERO_DIVIDE THEN
        DBMS_OUTPUT.PUT_LINE('Erro de divisao por zero!');
    WHEN VALUE_ERROR THEN
        DBMS_OUTPUT.PUT_LINE('Entre com valores numericos');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Ocorreu um erro: '||sqlerrm);
END;