
SET SERVEROUTPUT ON 

ACCEPT numero PROMPT 'Entre com um numero:'; 

DECLARE 

    numero NUMBER := &numero; 

BEGIN 

    IF (numero MOD 2) = 0 THEN 

    --IF numero % 2 == 0 THEN, invalido por ser uma construcao do Python 

        DBMS_OUTPUT.PUT_LINE('Numero Par'); 

    ELSE 

        DBMS_OUTPUT.PUT_LINE('Numero Impar'); 

    END IF; 

END; 

 

 