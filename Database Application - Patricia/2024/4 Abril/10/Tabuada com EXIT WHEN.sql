SET SERVEROUTPUT ON
ACCEPT n NUMBER PROMPT 'Entre com o valor da tabuada: '
DECLARE
    n NUMBER :=&n;
    i NUMBER :=1;
    tab NUMBER;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Tabuada com EXIT');
    LOOP
        tab:=n*i;
        DBMS_OUTPUT.PUT_LINE(n||' X '||i||' = '||tab);
        i:=i+1;
        EXIT WHEN i > 10; -- equivale a um "break" condicional
    END LOOP;
END;