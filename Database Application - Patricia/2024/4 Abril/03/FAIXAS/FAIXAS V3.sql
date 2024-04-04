SET SERVEROUTPUT ON
ACCEPT n PROMPT 'Digite um número: ';

DECLARE
    n1 NUMBER := &n;
BEGIN
    IF n1 BETWEEN 1 AND 10 THEN
        DBMS_OUTPUT.PUT_LINE('O número ' || n1 || ' está na primeira faixa');
    ELSIF n1 BETWEEN 11 AND 20 THEN
        DBMS_OUTPUT.PUT_LINE('O número ' || n1 || ' está na segunda faixa');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Faixa inválida');
    END IF;
END;
