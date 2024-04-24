--1) Imagine que voc� est� criando um programa para um simulador de clima. Este programa precisa classificar as cores com base em suas associa��es com temperaturas. Quando algu�m inserir uma cor, o programa dever� determinar se ela � quente ou fria, com base em seu relacionamento com a sensa��o de temperatura.
--Quando algu�m insere uma cor associada ao calor, como VERMELHA, AMARELA ou LARANJA, o programa responde com 'COR QUENTE', evocando a sensa��o de calor e fogo. Por outro lado, quando a cor inserida est� associada ao frio, como AZUL, VERDE ou CINZA, o programa responde com 'COR FRIA', fazendo refer�ncia � sensa��o de frescor e gelo.
--Escreva um bloco an�nimo em PL/SQL que simule essa intera��o, pedindo ao usu�rio que insira uma cor e dando a resposta correspondente com base na associa��o da cor com a temperatura


SET SERVEROUTPUT ON
ACCEPT v_cor PROMPT 'Entre com a cor:';
DECLARE
    v_cor VARCHAR2(10) := LOWER('&v_cor');
BEGIN
    CASE v_cor
    WHEN 'vermelha' THEN
        DBMS_OUTPUT.PUT_LINE('COR QUENTE');
    WHEN 'amarela' THEN
        DBMS_OUTPUT.PUT_LINE('COR QUENTE');
    WHEN 'laranja' THEN
        DBMS_OUTPUT.PUT_LINE('COR QUENTE');
    WHEN 'azul' THEN
        DBMS_OUTPUT.PUT_LINE('COR FRIA');
    WHEN 'verde' THEN
        DBMS_OUTPUT.PUT_LINE('COR FRIA');
    WHEN 'cinza' THEN
        DBMS_OUTPUT.PUT_LINE('COR FRIA');
    ELSE
        DBMS_OUTPUT.PUT_LINE('COR INVALIDA');
    END CASE;
END;


SET SERVEROUTPUT ON
ACCEPT v_cor PROMPT 'Entre com a cor:';
DECLARE
    v_cor VARCHAR2(10) := LOWER('&v_cor');
BEGIN
    CASE 
    WHEN v_cor IN ('vermelha', 'amarela', 'laranja') THEN
        DBMS_OUTPUT.PUT_LINE('COR QUENTE');
    WHEN v_cor IN ('azul', 'verde', 'cinza') THEN
        DBMS_OUTPUT.PUT_LINE('COR FRIA');
    ELSE
        DBMS_OUTPUT.PUT_LINE('COR INVALIDA');
    END CASE;
END;


SET SERVEROUTPUT ON
ACCEPT v_cor PROMPT 'Entre com a cor:';
DECLARE
    v_cor VARCHAR2(10) := LOWER('&v_cor');
BEGIN
    IF v_cor IN ('vermelha', 'amarela', 'laranja') THEN
        DBMS_OUTPUT.PUT_LINE('COR QUENTE');
    ELSIF v_cor IN ('azul', 'verde', 'cinza') THEN
        DBMS_OUTPUT.PUT_LINE('COR FRIA');
    ELSE
        DBMS_OUTPUT.PUT_LINE('COR INVALIDA');
    END IF;
END;
