-- Safe division

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //

CREATE FUNCTION SAFEDIV(A INT, B INT) RETURNS FLOAT 
DETERMINISTIC BEGIN IF 
	IF (b = 0) THEN RETURN (0);
	ELSE RETURN (a / b);
	END IF;


END //

DELIMITER ;