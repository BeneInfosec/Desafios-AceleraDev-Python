import yaml

from main import doc


document = yaml.load(doc)


def test_418():
    assert document.get('securitySchemes').get('JWT')


def test_50():
    assert document.get('types').get('Auth')


def test_122():
    assert document.get('types').get('Agent')


def test_98():
    assert document.get('types').get('Event')


def test_758():
    assert document.get('types').get('Group')


def test_522():
    assert document.get('types').get('User')


def test_86():
    assert document.get('/auth/token').get('post')


def test_560():
    assert document.get('/agents').get('post')


def test_968():
    assert document.get('/agents').get('get')


def test_664():
    assert document.get('/agents').get('/{id}')


def test_182():
    assert document.get('/agents').get('/{id}/events')


def test_810():
    assert document.get('/users').get('post')


def test_500():
    assert document.get('/users').get('get')


def test_918():
    assert document.get('/users').get('/{id}')


def test_4():
    assert document.get('/groups').get('post')


def test_920():
    assert document.get('/groups').get('get')


def test_466():
    assert document.get('/groups').get('/{id}')
    
