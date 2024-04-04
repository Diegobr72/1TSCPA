SET SERVEROUTPUT ON
ACCEPT n PROMPT 'Entre com o valor inteiro: ';
DECLARE
    n NUMBER := &n;
BEGIN
    IF n >=1 AND n<=20 THEN
        IF n BETWEEN 1 AND 10 THEN
            DBMS_OUTPUT.PUT_LINE('Primeira Faixa');
        END IF;
        IF n BETWEEN 11 AND 20 THEN
            DBMS_OUTPUT.PUT_LINE('Segunda Faixa');
        END IF;
    ELSE
        DBMS_OUTPUT.PUT_LINE('Faixa Invalida');
    END IF;
END;