SET SERVEROUTPUT ON 

ACCEPT valor_num PROMPT 'Digite um número para calcular a tabuada'; 

DECLARE 
    num NUMBER := &valor_num;
    i NUMBER;
    tab NUMBER;
BEGIN
    i:=0;
    LOOP
        tab:=num*i;
        DBMS_OUTPUT.PUT_LINE(num||'x'||i||' = ' || tab);
        i:=i+1;
        EXIT WHEN i>10;
    END LOOP;
END;