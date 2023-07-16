-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student
DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
  IN user_id INT
)
BEGIN
	DECLARE average_weighted_score DECIMAL(10, 2);

  -- Compute the average weighted score for the user
  SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO average_weighted_score
  FROM corrections
  INNER JOIN projects
  ON projects.id = corrections.project_id
  WHERE corrections.user_id = user_id;

  -- Update the average_weighted_score in the users table
  UPDATE users
  SET average_score = average_weighted_score
  WHERE users.id = user_id;

END //

DELIMITER ;

