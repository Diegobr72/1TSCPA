--5. (2 pontos) Escreva um bloco anonimo que recupere todos os nomes, cpfs e
--quantidade total de avalia��es de cada aluno e imprima essas informa��es.
--Ao final imprima tamb�m a quantidade total de avalia��es feitas por todos os alunos.
--Considere montar uma view com as informa��es de ROWNUM, nome, cpf, quantidade avalia��es antes de fazer o bloco an�nimo.

--SELECT CD_ALUNO,nm_aluno, cpf_aluno, qt_total_avaliacao
--FROM T_ALUNO;

--CREATE OR REPLACE VIEW VW_ALUNOS AS
--SELECT ROWNUM as nro_seq ,nm_aluno, cpf_aluno, qt_total_avaliacao
--FROM T_ALUNO;
--
--SELECT * FROM VW_ALUNOS;

SET SERVEROUTPUT ON
DECLARE
    v_qt_alunos NUMBER := 0;
    v_nm_aluno VARCHAR2(60);
    v_nm_aluno T_ALUNO.NM_ALUNO%TYPE;
    v_linha_vw_alunos VW_ALUNOS%ROWTYPE;
    i INTEGER;
BEGIN
    SELECT count(*) INTO v_qt_alunos FROM VW_ALUNOS;
    FOR i IN 1.. v_qt_alunos LOOP
        SELECT NRO_SEQ, NM_ALUNO, CPF_ALUNO, QT_TOTAL_AVALIACAO
        INTO v_linha_vw_alunos
        FROM VW_ALUNOS
        WHERE nro_seq = i;
        DBMS_OUTPUT.PUT_LINE('-----------------------');
        DBMS_OUTPUT.PUT_LINE('Aluno:' || v_linha_vw_alunos.nm_aluno );
        DBMS_OUTPUT.PUT_LINE('CPF:' || v_linha_vw_alunos.cpf_aluno );
        DBMS_OUTPUT.PUT_LINE('QT AVALIACAO:' || v_linha_vw_alunos.qt_total_avaliacao);
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('-----------------------');
END;