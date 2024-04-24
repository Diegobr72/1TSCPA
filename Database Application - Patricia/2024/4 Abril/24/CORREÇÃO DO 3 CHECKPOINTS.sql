--  CORRE��O DO 3 CHECKPOINTS


--------------------------------------------------------------------------------------------------------------------------------------------------


/*

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

*/


--------------------------------------------------------------------------------------------------------------------------------------------------


/*
--2) Imagine que voc� est� modelando o crescimento populacional de coelhos em uma reserva natural. 
--Voc� sabe que, em condi��es ideais, a popula��o de coelhos cresce 50% a cada ano.
--Escreva um bloco anonimo que determine em quantos anos a popula��o de coelhos 
--atingir� ou ultrapassar� 1000 indiv�duos, iniciando com uma popula��o inicial de 100 coelhos. 
--Use um loop para iterar sobre os anos at� que a popula��o alcance ou exceda o limite de 1000.

SET SERVEROUTPUT ON
DECLARE
    v_pop_ini NUMBER := 100; -- populacao inicial
    v_tx_cresc NUMBER := 0.5; --tx de crescimento
    v_limite_pop NUMBER := 1000;
    v_anos NUMBER := 0;
    v_pop_ano_a_ano NUMBER := v_pop_ini;

BEGIN
    WHILE v_pop_ano_a_ano < v_limite_pop LOOP
        v_pop_ano_a_ano := v_pop_ano_a_ano + (v_pop_ano_a_ano * v_tx_cresc);
        v_anos := v_anos + 1;
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('A populacao de coelhos ultrapassa ' || v_limite_pop || ' em ' || v_anos || ' anos : '||TRUNC(v_pop_ano_a_ano));

END;
*/


--------------------------------------------------------------------------------------------------------------------------------------------------


/*

--3) Escreva um bloco anonimo para calcular a efici�ncia de um sistema de energia, 
--onde a efici�ncia � definida como a raz�o entre a energia �til gerada e a energia total consumida. 
--Trate exce��es. Lance uma exce��o personalizada quando a energia consumida for negativa.

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

*/

--------------------------------------------------------------------------------------------------------------------------------------------------


/*

--4. (2 pontos) Escreva um bloco anonimo que recupere o nome da disciplina de codigo = 1 e imprima o seu nome

DECLARE
--    v_nm_disciplina VARCHAR2(30);
    v_nm_disciplina T_DISCIPLINA.NM_DISCIPLINA%TYPE;
BEGIN
    SELECT nm_disciplina
    INTO v_nm_disciplina
    FROM t_disciplina
    WHERE cd_disciplina = 1;
    DBMS_OUTPUT.PUT_LINE('O nome da disciplina de codigo 1 eh ' ||v_nm_disciplina);
END;

*/

--------------------------------------------------------------------------------------------------------------------------------------------------

/*

--5. (2 pontos) Escreva um bloco anonimo que recupere todos os nomes, cpfs e  
--quantidade total de avalia��es de cada aluno e imprima essas informa��es. 
--Ao final imprima tamb�m a quantidade total de avalia��es feitas por todos os alunos.  
--Considere montar uma view com as informa��es de ROWNUM, nome, cpf, quantidade avalia��es antes de fazer o bloco an�nimo.

--SELECT CD_ALUNO,nm_aluno, cpf_aluno, qt_total_avaliacao
--FROM T_ALUNO;

--CREATE OR REPLACE VIEW VW_ALUNOS AS
--SELECT ROWNUM as nro_seq ,nm_aluno, cpf_aluno, qt_total_avaliacao
--FROM T_ALUNO;
--
--SELECT * FROM VW_ALUNOS;

SET SERVEROUTPUT ON
DECLARE
    v_qt_alunos NUMBER := 0;
    v_nm_aluno VARCHAR2(60);
    v_nm_aluno T_ALUNO.NM_ALUNO%TYPE;
    v_linha_vw_alunos VW_ALUNOS%ROWTYPE;
    i INTEGER;
BEGIN
    SELECT count(*) INTO v_qt_alunos FROM VW_ALUNOS;
    FOR i IN 1.. v_qt_alunos LOOP
        SELECT NRO_SEQ, NM_ALUNO, CPF_ALUNO, QT_TOTAL_AVALIACAO  
        INTO v_linha_vw_alunos 
        FROM VW_ALUNOS
        WHERE nro_seq = i;
        DBMS_OUTPUT.PUT_LINE('-----------------------');
        DBMS_OUTPUT.PUT_LINE('Aluno:' || v_linha_vw_alunos.nm_aluno );
        DBMS_OUTPUT.PUT_LINE('CPF:' || v_linha_vw_alunos.cpf_aluno );
        DBMS_OUTPUT.PUT_LINE('QT AVALIACAO:' || v_linha_vw_alunos.qt_total_avaliacao);
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('-----------------------');
END;

*/