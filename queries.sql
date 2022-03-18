-- Create table


DROP TABLE conferences;
DROP TABLE talks;
DROP TABLE speakers;
DROP TABLE participants;

CREATE TABLE conferences (
      id int NOT NULL AUTO_INCREMENT,
      title varchar(255) NOT NULL,
      description varchar(255) NOT NULL,
      start_date date NOT NULL,
      end_date date NOT NULL,
      PRIMARY KEY(id)
);

CREATE TABLE talks (
        id int NOT NULL AUTO_INCREMENT,
        title varchar(255) NOT NULL,
        description varchar(255) NOT NULL,
        duration int NOT NULL,
        start_datetime datetime NOT NULL,
        conference_id int NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (conference_id) REFERENCES conferences(id)
) ;


CREATE TABLE speakers (
        id int NOT NULL AUTO_INCREMENT,
        username varchar(255) NOT NULL,
        email varchar(255) NOT NULL,
        talk_id int NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (talk_id) REFERENCES talks(id)
) ;

CREATE TABLE participants (
        id int NOT NULL AUTO_INCREMENT,
        username varchar(255) NOT NULL,
        email varchar(255) NOT NULL,
        talk_id int NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (talk_id) REFERENCES talks(id)
) ;