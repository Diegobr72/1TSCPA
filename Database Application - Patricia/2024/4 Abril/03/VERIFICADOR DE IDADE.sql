SET SERVEROUTPUT ON
ACCEPT idade PROMPT 'Qual sua idade: ';

DECLARE
    idade NUMBER := &idade ;

BEGIN
    IF idade >= 16 THEN
        DBMS_OUTPUT.PUT_LINE('Voc� pode votar');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Voc� n�o pode votar');
    END IF;
END;
