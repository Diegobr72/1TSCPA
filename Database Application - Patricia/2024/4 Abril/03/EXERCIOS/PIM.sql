SET SERVEROUTPUT ON 

ACCEPT valor_num PROMPT 'Digite um número para o limite: '; 

DECLARE 
    num NUMBER := &valor_num;
    i NUMBER := 1;
BEGIN
    WHILE i <= num LOOP
        IF MOD(i, 4) = 0 THEN 
            DBMS_OUTPUT.PUT_LINE('PIM');
        ELSE
            DBMS_OUTPUT.PUT_LINE(i);
        END IF;
        i := i + 1;
    END LOOP;
END;
