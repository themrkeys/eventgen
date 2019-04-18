import pytest

from utils.eventgen_test_helper import EventgenTestHelper


@pytest.fixture
def eventgen_test_helper():
    """Returns a function to create EventgenTestHelper instance based on config file"""
    created_instances = []

    def _create_eventgen_test_helper_instance(conf, timeout=None):
        instance = EventgenTestHelper(conf, timeout)
        created_instances.append(instance)
        return instance
    yield _create_eventgen_test_helper_instance

    for instance in created_instances:
        instance.tear_down()