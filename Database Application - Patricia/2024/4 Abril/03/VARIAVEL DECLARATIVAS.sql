SET SERVEROUTPUT ON
ACCEPT valor3 PROMPT 'Digite o terceiro valor: ';
ACCEPT valor4 PROMPT 'Digite o quarto valor: ';

DECLARE
    -- Criando constantes
    n1 NUMBER := 7;
    n2 NUMBER;
    
    -- Trazendo as variaveis da entrada de dados
    n3 NUMBER := &valor3 ;
    n4 NUMBER := &valor4 ;
    media NUMBER;
BEGIN
    n2 := 16;
    media := (n1 + n2 + n3 + n4) / 2;
    
    DBMS_OUTPUT.PUT_LINE('A média entre ' || n1 || ' e ' || n2 || ' é ' || media);
    
    DBMS_OUTPUT.PUT_LINE('Agora a média entre os valores ' || n1 || ' e ' || n2 || ' e ' || n3 || ' e ' || n4 || ' = ' || media);
END;
