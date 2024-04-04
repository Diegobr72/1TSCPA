SET SERVEROUTPUT ON
ACCEPT n PROMPT 'Digite um número: ';

DECLARE
    n1 NUMBER := &n;
BEGIN
    IF n1 >= 1 AND n1 <= 20 THEN
        IF n1 >= 1 AND n1 <= 10 THEN
            DBMS_OUTPUT.PUT_LINE('O número ' || n1 || ' está na primeira faixa');
        ELSE
            DBMS_OUTPUT.PUT_LINE('O número ' || n1 || ' está na segunda faixa');
        END IF;
    ELSE
        DBMS_OUTPUT.PUT_LINE('Faixa inválida');
    END IF;
END;
