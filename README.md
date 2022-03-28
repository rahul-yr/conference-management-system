# conference-management-system

## Important information

        Please update `_address` variable according to your SQL server details at api/config/database.py

        Use `queries.sql` file for Creating required tables

## Available endpoints

        Create a conference   http://127.0.0.1:8000/api/conferences/create
        Edit a Conference     http://127.0.0.1:8000/api/conferences/update
        Get all conferences   http://127.0.0.1:8000/api/conferences/all

        Create a Talk                   http://127.0.0.1:8000/api/talk/create
        Edit a Talk                     http://127.0.0.1:8000/api/talk/update
        Get all Talks by Conference ID  http://127.0.0.1:8000/api/talk/all/{id}

        Add a Speaker to Talk           http://127.0.0.1:8000/api/talk/addspeaker
        Delete a Speaker from Talk      http://127.0.0.1:8000/api/talk/deletespeaker/{id}
        Get all speakers by TalkID      http://127.0.0.1:8000/api/talk/speakers/{id}

        Add a Participant to Talk       http://127.0.0.1:8000/api/talk/addparticipant
        Delete a Participant to Talk    http://127.0.0.1:8000/api/talk/deleteparticipant/{id}
        Get all Participants by TalkID  http://127.0.0.1:8000/api/talk/participants/{id}

## Commands

        ### Create virtual venv

        Python -m venv venv

        ### Freeze requirements

        pip freeze > requirements.txt

        ###Clean unwanted python files
        pyclean .

        # Execution

        uvicorn main:app --reload

## Additional Info

        http://127.0.0.1:8000/docs   - Interactive editor
        http://127.0.0.1:8000/redoc  - All Endpoints documentation

## References

        Refer docs/QUESTION.md
        Refer https://pydantic-docs.helpmanual.io/usage/types/#datetime-types for pydantic date validations
