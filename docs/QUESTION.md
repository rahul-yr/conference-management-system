## Let’s build a simple conference management system.

    ● Conference
    o Properties
      ▪ Title
      ▪ Description
      ▪ Start & End Date

    ● Talk
      o A conference can have multiple talks under it.
      o Properties
        ▪ Title
        ▪ Description
        ▪ Duration
        ▪ Date & Time
        ▪ Speakers *
        ▪ Participants *

    ● Speaker/Participant
        o Each talk will have a list of speakers and participants
        o A speaker/participant is defined by their username & email.

    ● Create APIs
        o To create/edit a conference
        o To add/edit a talk
        o To add/remove speaker/participant from a talk.
        o To list talks in a conference
        o To list conferences.
        ● Please use SQLAlchemy as the ORM with Mysql/Postgres as the DB. Please
        push your commits to a private repository on Github.
        ● Assume real world scenarios and design the system accordingly.
