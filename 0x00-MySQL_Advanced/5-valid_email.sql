-- Email validation to sent
-- creates a trigger that resets the attribute valid_email only
-- when the email has been changed.

DELIMITER $$

CREATE TRIGGER CHANGE_EMAIL BEFORE UPDATE ON USERS 
FOR EACH ROW BEGIN IF 
	IF NEW.email <> OLD.email THEN SET NEW.valid_email = 0;
	END IF;
	END $$ 


DELIMITER;