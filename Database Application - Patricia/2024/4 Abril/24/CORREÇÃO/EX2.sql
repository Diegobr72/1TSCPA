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
