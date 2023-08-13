-- stored procedure AddBonus that adds a new correction for a student.

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER //

CREATE PROCEDURE ADDBONUS(IN USER_ID INT, IN PROJECT_NAME 
VARCHAR(255), IN SCORE FLOAT) BEGIN DECLARE 
	DECLARE project_id INT;
	IF (
	    SELECT COUNT(*)
	    FROM projects
	    WHERE
	        name = project_name
	) = 0 THEN
	INSERT INTO
	    projects (name)
	VALUES (project_name);
	END IF;


SET project_id = (
        SELECT id
        FROM projects
        WHERE name = project_name
        LIMIT 1
    );

INSERT INTO
    corrections (user_id, project_id, score)
VALUES
(user_id, project_id, score);

END //

DELIMITER ;
