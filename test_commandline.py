from unittest.mock import Mock

import pytest

from commandline import Commandline
from paginator import Paginator
from renderer import Renderer


@pytest.fixture
def commandline():
    Renderer.render = Mock()
    return Commandline("test.csv")


def test_call_get_first_page_on_start(commandline):
    fun = Mock()
    Paginator.get_first_page = fun
    commandline.start()

    assert fun.called


@pytest.mark.parametrize("user_input", ["f", "F"])
def test_call_last_page_for_f(user_input, commandline):
    fun = Mock()
    Paginator.get_first_page = fun

    commandline.execute(user_input)

    assert fun.called


@pytest.mark.parametrize("user_input", ["l", "L"])
def test_call_last_page_for_l(user_input, commandline):
    fun = Mock()
    Paginator.get_last_page = fun

    commandline.execute(user_input)

    assert fun.called


def test_unknown_user_input(commandline):
    with pytest.raises(AttributeError):
        commandline.execute("unknown")
