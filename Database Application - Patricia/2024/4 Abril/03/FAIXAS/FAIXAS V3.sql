SET SERVEROUTPUT ON
ACCEPT n PROMPT 'Digite um n�mero: ';

DECLARE
    n1 NUMBER := &n;
BEGIN
    IF n1 BETWEEN 1 AND 10 THEN
        DBMS_OUTPUT.PUT_LINE('O n�mero ' || n1 || ' est� na primeira faixa');
    ELSIF n1 BETWEEN 11 AND 20 THEN
        DBMS_OUTPUT.PUT_LINE('O n�mero ' || n1 || ' est� na segunda faixa');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Faixa inv�lida');
    END IF;
END;
