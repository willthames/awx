
# Python
import pytest

from awx.main.tests.factories import (
    create_organization,
    create_job_template,
    create_notification_template,
    create_survey_spec,
)

@pytest.fixture
def job_template_factory():
    return create_job_template

@pytest.fixture
def organization_factory():
    return create_organization

@pytest.fixture
def notification_template_factory():
    return create_notification_template

@pytest.fixture
def survey_spec_factory():
    return create_survey_spec

@pytest.fixture
def job_with_secret_key_factory(job_template_factory):
    def rf(persisted):
        "Returns job with linked JT survey with password survey questions"
        objects = job_template_factory('jt', organization='org1', survey=[
            {'variable': 'submitter_email', 'type': 'text', 'default': 'foobar@redhat.com'},
            {'variable': 'secret_key', 'default': '6kQngg3h8lgiSTvIEb21', 'type': 'password'},
            {'variable': 'SSN', 'type': 'password'}], jobs=[1], persisted=persisted)
        return objects.jobs[1]
    return rf

@pytest.fixture
def job_with_secret_key_unit(job_with_secret_key_factory):
    return job_with_secret_key_factory(persisted=False)