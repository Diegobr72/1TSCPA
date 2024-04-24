--4. (2 pontos) Escreva um bloco anonimo que recupere o nome da disciplina de codigo = 1 e imprima o seu nome

DECLARE
--    v_nm_disciplina VARCHAR2(30);
    v_nm_disciplina T_DISCIPLINA.NM_DISCIPLINA%TYPE;
BEGIN
    SELECT nm_disciplina
    INTO v_nm_disciplina
    FROM t_disciplina
    WHERE cd_disciplina = 1;
    DBMS_OUTPUT.PUT_LINE('O nome da disciplina de codigo 1 eh ' ||v_nm_disciplina);
END;