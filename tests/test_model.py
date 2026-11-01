rom unittest.mock import patch

import pytest

from model import analyze_text


def test_empty_text_is_not_allowed():
    with pytest.raises(ValueError, match="Введите текст"):
        analyze_text("   ")


@patch("model.get_model")
def test_analyze_text_returns_prediction(mock_get_model):
    mock_get_model.return_value.return_value = [
        {
            "label": "POSITIVE",
            "score": 0.98765,
        }
    ]

    result = analyze_text("I love this movie")

    assert result == {
        "label": "POSITIVE",
        "score": 0.9877,
    }

    mock_get_model.return_value.assert_called_once_with(
        "I love this movie"
    )
