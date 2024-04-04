SET SERVEROUTPUT ON

ACCEPT saldo_conta NUMBER PROMPT 'Qual o saldo da conta corrente? ';
ACCEPT prestacao_carro NUMBER PROMPT 'Qual o valor da presta��o do carro? ';

DECLARE
    novo_saldo NUMBER;
    mes NUMBER := 1;
BEGIN
    novo_saldo := &saldo_conta;

    WHILE novo_saldo >= &prestacao_carro LOOP
        novo_saldo := novo_saldo - &prestacao_carro;
        DBMS_OUTPUT.PUT_LINE('Ao final do m�s ' || mes || ' voc� ter� ' || novo_saldo || ' reais');
        mes := mes + 1;
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE('A partir do m�s ' || mes || ' voc� n�o conseguir� mais pagar a presta��o');
END;
