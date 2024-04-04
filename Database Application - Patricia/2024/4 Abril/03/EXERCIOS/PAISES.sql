SET SERVEROUTPUT ON
ACCEPT pais PROMPT 'Digite o pa�s de nascimento (Brasil, M�xico ou Canad�): ';

DECLARE
    pais_nascimento VARCHAR2(50) := UPPER('&pais');
BEGIN
    CASE pais_nascimento
        WHEN 'BRASIL' THEN
            DBMS_OUTPUT.PUT_LINE('O Brasil est� localizado na Am�rica do Sul.');
        WHEN 'M�XICO' THEN
            DBMS_OUTPUT.PUT_LINE('O M�xico est� localizado na Am�rica do Norte.');
        WHEN 'CANAD�' THEN
            DBMS_OUTPUT.PUT_LINE('O Canad� est� localizado na Am�rica do Norte.');
        ELSE
            DBMS_OUTPUT.PUT_LINE('Pa�s n�o reconhecido.');
    END CASE;
END;
