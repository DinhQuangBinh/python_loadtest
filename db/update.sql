ALTER TABLE `sg_mission_players` ADD COLUMN `finished` DATETIME NULL DEFAULT NULL AFTER `created`;
ALTER TABLE `sg_mission_players` ADD COLUMN `duration` INT(11) NULL DEFAULT NULL AFTER `finished`;
update sg_mission_players set duration = 0;
update sg_mission_players set finished = created;
