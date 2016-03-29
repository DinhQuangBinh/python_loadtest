CREATE TABLE `survey_type_groups` (
	`id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(50) NOT NULL,
	`created` DATETIME NULL DEFAULT NULL,
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;

ALTER TABLE `survey_questions`
	ADD COLUMN `type_group_id` INT NULL DEFAULT NULL AFTER `type`;
	
	
ALTER TABLE `survey_questions`
	ALTER `type_group_id` DROP DEFAULT;
ALTER TABLE `survey_questions`
	CHANGE COLUMN `type_group_id` `type_group_id` INT(11) NOT NULL AFTER `type`;