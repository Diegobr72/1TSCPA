SET SERVEROUTPUT ON
ACCEPT pais PROMPT 'Digite o país de nascimento (Brasil, México ou Canadá): ';

DECLARE
    pais_nascimento VARCHAR2(50) := UPPER('&pais');
BEGIN
    CASE pais_nascimento
        WHEN 'BRASIL' THEN
            DBMS_OUTPUT.PUT_LINE('O Brasil está localizado na América do Sul.');
        WHEN 'MÉXICO' THEN
            DBMS_OUTPUT.PUT_LINE('O México está localizado na América do Norte.');
        WHEN 'CANADÁ' THEN
            DBMS_OUTPUT.PUT_LINE('O Canadá está localizado na América do Norte.');
        ELSE
            DBMS_OUTPUT.PUT_LINE('País não reconhecido.');
    END CASE;
END;
