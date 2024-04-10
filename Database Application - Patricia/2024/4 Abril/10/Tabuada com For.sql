SET SERVEROUTPUT ON
ACCEPT n NUMBER PROMPT 'Entre com o valor da tabuada: '
DECLARE
    n NUMBER:= &n;
    i NUMBER;
    tab NUMBER;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Tabuada com FOR');
    FOR i IN 1..10
    LOOP
        tab:=n*i;
        DBMS_OUTPUT.PUT_LINE(n||' X '||i||' = '||tab);
    END LOOP;
END;