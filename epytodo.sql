use epytodo
DROP TABLE IF EXISTS user;
CREATE TABLE user (
            user_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
       );

DROP TABLE IF EXISTS task;
CREATE TABLE task (
            task_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            title VARCHAR(100) NOT NULL,
            begin DATETIME DEFAULT NOW() NOT NULL,
            end DATETIME DEFAULT NULL,
            status VARCHAR(100) DEFAULT 'not started' NOT NULL
       );

DROP TABLE IF EXISTS user_has_task;
CREATE TABLE user_has_task (
            fk_user_id INT NOT NULL,
            fk_task_id INT NOT NULL,
            FOREIGN KEY (fk_user_id) REFERENCES user (user_id),
            FOREIGN KEY	(fk_task_id) REFERENCES	task (task_id)
       );
