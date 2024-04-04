SET SERVEROUTPUT ON
ACCEPT idade PROMPT 'Qual sua idade: ';

DECLARE
    idade NUMBER := &idade ;

BEGIN
    IF idade >= 16 THEN
        DBMS_OUTPUT.PUT_LINE('Você pode votar');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Você não pode votar');
    END IF;
END;
