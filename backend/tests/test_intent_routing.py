from core.agents.workflow import route_intent


def test_disease_questions_route_to_disease_intent():
    state = {
        "user_query": "Should I spray fungicide on my paddy field today?",
        "files": [],
    }

    result = route_intent(state)

    assert result["intent"] == "disease_question"


def test_market_queries_route_to_market_intent():
    state = {
        "user_query": "What is the paddy mandi price in Vizag today?",
        "files": [],
    }

    result = route_intent(state)

    assert result["intent"] == "market_question"
