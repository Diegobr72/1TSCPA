SET SERVEROUTPUT ON
ACCEPT salario PROMPT 'Digite o valor do salario: ';

DECLARE
    sl NUMBER := &salario ;
    ferias NUMBER;
BEGIN
    ferias := sl * 1.3;
    
    DBMS_OUTPUT.PUT_LINE('O valor do salario � ' || sl || ' voc� receberar nas f�rias : ' || ferias);
END;
