DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
  IN p_user_id INT
)
BEGIN
  DECLARE average_score DECIMAL(10, 2);

  -- Compute the average score for the user
  SELECT AVG(score) INTO average_score
  FROM corrections
  WHERE user_id = p_user_id;

  -- Update the average_score in the users table
  UPDATE users
  SET average_score = average_score
  WHERE id = p_user_id;
END //

DELIMITER ;

