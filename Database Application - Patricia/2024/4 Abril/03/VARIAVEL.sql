SET SERVEROUTPUT ON
DECLARE
    n1 NUMBER;
    nome VARCHAR2(10);
    segundo_nome VARCHAR2(10) := 'Alves';
BEGIN
    -- o DBMS_OUTPUT.PUT_LINE é equivalente ao PRINT em Python
    DBMS_OUTPUT.PUT_LINE('Meu primeiro programa em PL/SQL');
    --utilizando as variaveis
    nome := 'Diego';
    DBMS_OUTPUT.PUT_LINE('Bom dia' || ' ' || nome || ' ' || segundo_nome);
    
    n1 := 20;
    
    DBMS_OUTPUT.PUT_LINE('Dias para acustumar com uma outra linguagem: ' || n1);
    
END;
