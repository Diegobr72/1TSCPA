SET SERVEROUTPUT ON
ACCEPT n PROMPT 'Digite um n�mero: ';

DECLARE
    n1 NUMBER := &n;
BEGIN
    IF n1 >= 1 AND n1 <= 20 THEN
        IF n1 >= 1 AND n1 <= 10 THEN
            DBMS_OUTPUT.PUT_LINE('O n�mero ' || n1 || ' est� na primeira faixa');
        ELSE
            DBMS_OUTPUT.PUT_LINE('O n�mero ' || n1 || ' est� na segunda faixa');
        END IF;
    ELSE
        DBMS_OUTPUT.PUT_LINE('Faixa inv�lida');
    END IF;
END;
