from backend.agents.memory import memory


session = "user1"


memory.add_messages(

    session,

    ["A"]

)


memory.add_messages(

    session,

    ["B"]

)


memory.add_messages(

    session,

    ["C"]

)


print(

    memory.get_history(

        session

    )

)