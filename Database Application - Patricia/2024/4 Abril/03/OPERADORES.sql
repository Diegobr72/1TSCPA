SET SERVEROUTPUT ON 

DECLARE 

    resultado NUMBER :=0; 

BEGIN 

    resultado := 1/2; 

    --NA CONVERSAO PARA STRING ELE TIRA O ZERO DA FRENTE QDO NUMERO <1 

    DBMS_OUTPUT.PUT_LINE(resultado); 

    --MOD EH O RESTO DA DIVISAO 

    resultado := 10 mod 3; 

    DBMS_OUTPUT.PUT_LINE(resultado); 

    -- O SIMBOLO DE DESIGUALDADE EH <> 

    IF resultado <> 4 THEN 

        DBMS_OUTPUT.PUT_LINE('Resultado diferente de 4'); 

    END IF; 

END; 
