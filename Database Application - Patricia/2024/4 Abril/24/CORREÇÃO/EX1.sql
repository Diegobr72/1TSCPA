--1) Imagine que você está criando um programa para um simulador de clima. Este programa precisa classificar as cores com base em suas associações com temperaturas. Quando alguém inserir uma cor, o programa deverá determinar se ela é quente ou fria, com base em seu relacionamento com a sensação de temperatura.
--Quando alguém insere uma cor associada ao calor, como VERMELHA, AMARELA ou LARANJA, o programa responde com 'COR QUENTE', evocando a sensação de calor e fogo. Por outro lado, quando a cor inserida está associada ao frio, como AZUL, VERDE ou CINZA, o programa responde com 'COR FRIA', fazendo referência à sensação de frescor e gelo.
--Escreva um bloco anônimo em PL/SQL que simule essa interação, pedindo ao usuário que insira uma cor e dando a resposta correspondente com base na associação da cor com a temperatura


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
